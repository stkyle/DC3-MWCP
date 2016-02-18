#!/usr/bin/env python
"""Install mwcp
"""
import os
import re
import sys
from codecs import open as codecs_open
from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    """Use Pytest for setup option `test`.
    """
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

# Upload to Repo
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

REQUIRES = []

REQUIRES_TEST = ['pytest>=2.8.0', ]

# Retrieve version from package variable __version__
with codecs_open('mwcp/__init__.py', 'r') as fd:
    VERSION = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not VERSION:
    raise RuntimeError('Cannot find version information')

with codecs_open('README.md', 'r', 'utf-8') as f:
    README = f.read()
with codecs_open('HISTORY.md', 'r', 'utf-8') as f:
    HISTORY = f.read()


setup(
    name='mwcp',
    version=VERSION,
    author="DC3",
    description='A framework malware configuration parsers.',
    long_description=README + '\n\n' + HISTORY,
    license="MIT",
    keywords="malware",
    url="http://github.com/Defense-Cyber-Crime-Center/DC3-MWCP/",
    packages=find_packages(),
    package_data={'': ['*.txt', '*.json',
                       'resources/*.txt', 'resources/*.json']},
    scripts=["mwcp-tool.py", "mwcp-client.py",
             "mwcp-server.py", "mwcp-test.py"],
    extras_require={'recommended': ['pefile', 'yara', 'pyCrypto', 'pydasm']},
)
