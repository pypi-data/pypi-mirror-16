#!/usr/bin/env python
"""Build versioned Sphinx docs for every branch and tag pushed to origin.

DESTINATION is the path to the directory that will hold all generated docs for
all versions.

REL_SOURCE is the path to the docs directory relative to the git root. If the
source directory has moved around between git tags you can specify additional
directories.

DST_BRANCH is the branch name where generated docs will be committed to. The
branch will then be pushed to origin. If there is a race condition with another
job pushing to origin the docs will be re-generated and pushed again.

REL_DST is the path to the directory that will hold all generated docs for
all versions relative to the git roof of DST_BRANCH.

To pass options to sphinx-build (run for every branch/tag) use a double hyphen
(e.g. {program} build /tmp/out docs -- -D setting=value).

Usage:
    {program} [options] build DESTINATION REL_SOURCE...
    {program} [options] [-e F...] push DST_BRANCH REL_DST REL_SOURCE...
    {program} -h | --help
    {program} -V | --version

Options:
    -c DIR --chdir=DIR      cd into this directory before running.
    -C --no-colors          Disable colors in terminal output.
    -e F --grm-exclude=FILE Push only. If specified "git rm" will delete all
                            files in REL_DEST except for these. Specify
                            multiple times for more. Paths are relative to
                            REL_DEST in DST_BRANCH.
    -h --help               Show this screen.
    -i --invert             Invert/reverse order of versions.
    -p K --prioritize=KIND  Set to "branches" or "tags" to group those kinds
                            of versions at the top (for themes that don't
                            separate them).
    -r REF --root-ref=REF   The branch/tag at the root of DESTINATION. All
                            others are in subdirectories [default: master].
    -S OPTS --sort=OPTS     Sort versions by one or more (comma separated):
                            semver, alpha, chrono
    -t --greatest-tag       Override root-ref to be the tag with the highest
                            version number.
    -T --recent-tag         Override root-ref to be the most recent committed
                            tag.
    -v --verbose            Debug logging.
    -V --version            Print sphinxcontrib-versioning version.
"""

import logging
import os
import shutil
import sys
import time

from docopt import docopt

from sphinxcontrib.versioning import __version__
from sphinxcontrib.versioning.git import clone, commit_and_push, get_root, GitError
from sphinxcontrib.versioning.lib import HandledError, TempDir
from sphinxcontrib.versioning.routines import build_all, gather_git_info, pre_build
from sphinxcontrib.versioning.setup_logging import setup_logging
from sphinxcontrib.versioning.versions import multi_sort, Versions

PUSH_RETRIES = 3
PUSH_SLEEP = 3  # Seconds.


def get_arguments(argv, doc):
    """Get command line arguments.

    :param iter argv: Arguments to pass (e.g. sys.argv).
    :param str doc: Docstring to pass to docopt.

    :return: Parsed options with overflow options in the "overflow" key.
    :rtype: dict
    """
    if '--' in argv:
        pos = argv.index('--')
        argv, overflow = argv[:pos], argv[pos + 1:]
    else:
        argv, overflow = argv, list()
    docstring = doc.format(program='sphinx-versioning')
    config = docopt(docstring, argv=argv[1:], version=__version__)
    config['overflow'] = overflow
    return config


def main_build(config, root, destination):
    """Main function for build sub command.

    :raise HandledError: If function fails with a handled error. Will be logged before raising.

    :param dict config: Parsed command line arguments (get_arguments() output).
    :param str root: Root directory of repository.
    :param str destination: Value of config['DESTINATION'].

    :return: Versions class instance.
    :rtype: sphinxcontrib.versioning.versions.Versions
    """
    log = logging.getLogger(__name__)

    # Gather git data.
    log.info('Gathering info about the remote git repository...')
    conf_rel_paths = [os.path.join(s, 'conf.py') for s in config['REL_SOURCE']]
    root, remotes = gather_git_info(root, conf_rel_paths)
    if not remotes:
        log.error('No docs found in any remote branch/tag. Nothing to do.')
        raise HandledError
    versions = Versions(
        remotes,
        sort=(config['--sort'] or '').split(','),
        prioritize=config['--prioritize'],
        invert=config['--invert'],
    )

    # Get root ref.
    root_ref = None
    if config['--greatest-tag'] or config['--recent-tag']:
        candidates = [r for r in versions.remotes if r['kind'] == 'tags']
        if not candidates:
            log.warning('No git tags with docs found in remote. Falling back to --root-ref value.')
        else:
            multi_sort(candidates, ['semver' if config['--greatest-tag'] else 'chrono'])
            root_ref = candidates[0]['name']
    if not root_ref:
        root_ref = config['--root-ref']
        if config['--root-ref'] not in [r[1] for r in remotes]:
            log.error('Root ref %s not found in: %s', config['--root-ref'], ' '.join(r[1] for r in remotes))
            raise HandledError
    versions.set_root_remote(root_ref)

    # Pre-build.
    log.info('Pre-running Sphinx to determine URLs.')
    exported_root = pre_build(root, versions, config['overflow'])

    # Build.
    build_all(exported_root, destination, versions, config['overflow'])

    # Cleanup.
    log.debug('Removing: %s', exported_root)
    shutil.rmtree(exported_root)

    return versions


def main_push(config, root, temp_dir):
    """Main function for push sub command.

    :raise HandledError: On unrecoverable errors. Will be logged before raising.

    :param dict config: Parsed command line arguments (get_arguments() output).
    :param str root: Root directory of repository.
    :param str temp_dir: Local path empty directory in which branch will be cloned into.

    :return: If push succeeded.
    :rtype: bool
    """
    log = logging.getLogger(__name__)

    log.info('Cloning %s into temporary directory...', config['DST_BRANCH'])
    try:
        clone(root, temp_dir, config['DST_BRANCH'], config['REL_DST'], config['--grm-exclude'])
    except GitError as exc:
        log.error(exc.message)
        log.error(exc.output)
        raise HandledError

    log.info('Building docs...')
    versions = main_build(config, root, os.path.join(temp_dir, config['REL_DST']))

    log.info('Attempting to push to branch %s on remote repository.', config['DST_BRANCH'])
    try:
        return commit_and_push(temp_dir, versions)
    except GitError as exc:
        log.error(exc.message)
        log.error(exc.output)
        raise HandledError


def main(config):
    """Main function.

    :raise HandledError: If function fails with a handled error. Will be logged before raising.

    :param dict config: Parsed command line arguments (get_arguments() output).
    """
    log = logging.getLogger(__name__)
    log.info('Running sphinxcontrib-versioning v%s', __version__)

    # chdir.
    if config['--chdir']:
        try:
            os.chdir(config['--chdir'])
        except OSError as exc:
            log.debug(str(exc))
            if exc.errno == 2:
                log.error('Path not found: %s', config['--chdir'])
            else:
                log.error('Path not a directory: %s', config['--chdir'])
            raise HandledError
    log.debug('Working directory: %s', os.getcwd())

    # Get root.
    try:
        root = get_root(os.getcwd())
    except GitError as exc:
        log.error(exc.message)
        log.error(exc.output)
        raise HandledError
    log.info('Working in git repository: %s', root)

    # Run build sub command.
    if config['build']:
        main_build(config, root, config['DESTINATION'])
        return

    # Clone, build, push.
    for _ in range(PUSH_RETRIES):
        with TempDir() as temp_dir:
            if main_push(config, root, temp_dir):
                return
        log.warning('Failed to push to remote repository. Retrying in %d seconds...', PUSH_SLEEP)
        time.sleep(PUSH_SLEEP)

    # Failed if this is reached.
    log.error('Ran out of retries, giving up.')
    raise HandledError


def entry_point():
    """Entry-point from setuptools."""
    try:
        config = get_arguments(sys.argv, __doc__)
        setup_logging(verbose=config['--verbose'], colors=not config['--no-colors'])
        main(config)
        logging.info('Success.')
    except HandledError:
        logging.critical('Failure.')
        sys.exit(1)
