import os
import glob
import yaml
import git
from functools import wraps

import const
from messages import registry_pb2, registry_pb2_grpc


def repo_context(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if os.path.isdir(const.REPOSITORY_DIR):
            pull_repository()
        else:
            os.makedirs(const.GIT_DIR)
            clone_repository()
        return f(*args, **kwargs)
    return wrapped


def clone_repository():
    git.Repo.clone_from(const.REPOSITORY_URL, const.GIT_DIR)


def pull_repository():
    g = git.cmd.Git(const.REPOSITORY_DIR)
    g.pull()


@repo_context
def get_package_details():
    pkg_file = const.PACKAGE_FILE
    if const.PACKAGE_FILE is None:
        pkg_file = glob.glob("%s/*.package.yaml" % const.OPERATOR_BUNDLE_DIR)[0]
    with open(pkg_file, 'r') as fobj:
        try:
            y = yaml.safe_load(fobj)
            if 'defaultChannel' not in y:
                y['defaultChannel'] = y['channels'][0]['name']
            channels = []
            for channel in y['channels']:
                channels.append(registry_pb2.Channel(name=channel['name'], csvName=channel['currentCSV']))
            return registry_pb2.Package(name=y['packageName'], channels=channels, defaultChannelName=y['defaultChannel'])
        except yaml.YAMLError as e:
            print(e)


    