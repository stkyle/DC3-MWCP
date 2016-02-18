#!/usr/bin/env python
"""Install mwcp
"""
import os
import re
import sys
from codecs import open
from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
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

packages = [
    'mwcp',
]

requires = []

test_requirements = ['pytest>=2.8.0', ]

# Retrieve version from package variable __version__
with open('mwcp/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.md', 'r', 'utf-8') as f:
    history = f.read()


setup(
    name = 'mwcp',
    version = version,
    author = "DC3",
    description = 'A framework malware configuration parsers.',
    long_description = readme + '\n\n' + history,
    license = "MIT",
    keywords = "malware",
    url = "http://github.com/Defense-Cyber-Crime-Center/DC3-MWCP/",
    packages = find_packages(),
    package_data = {
        '': ['*.txt', '*.json', 'resources/*.txt', 'resources/*.json']
        },
    scripts = [ "mwcp-tool.py", "mwcp-client.py", "mwcp-server.py", "mwcp-test.py" ],
    extra_require = {'recommended': ['pefile', 'yara', 'pyCrypto', 'pydasm']
    },
)
