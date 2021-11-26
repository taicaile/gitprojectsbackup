import os
import logging

import git
from pathlib import Path
from setting import config

GIT_PROJECTS_ROOT = Path(config["GIT_PROJECTS_ROOT"])

if not GIT_PROJECTS_ROOT.exists():
    GIT_PROJECTS_ROOT.mkdir(parents=True)

logger = logging.getLogger()

for subfolder in GIT_PROJECTS_ROOT.iterdir():
    if not subfolder.is_dir():
        continue
    try:
        repo = git.Repo(subfolder)
        for remote in repo.remotes:
            assert remote.exists()
            remote.fetch()
            logger.info("%s fetch %s: %s", subfolder.name, remote.name, remote.url)
    except AssertionError as err:
        logger.exception(err)
