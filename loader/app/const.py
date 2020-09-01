import os

REPOSITORY_URL = os.environ.get('REPOSITORY_URL', None)
REPOSITORY_NAME = os.environ.get('REPOSITORY_NAME', REPOSITORY_URL.split('/')[-1].replace('.git', ''))
GIT_DIR = os.environ.get('REPOSITORY_DIR', '/tmp/git')
REPOSITORY_DIR = os.path.join(GIT_DIR, REPOSITORY_NAME)
OPERATOR_BUNDLE_DIR = os.path.join(REPOSITORY_DIR, os.environ.get('OPERATOR_BUNDLE_DIR', ''))
PACKAGE_FILE = os.environ.get('PACKAGE_FILE', None)
