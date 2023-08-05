#!/usr/bin/env python
"""
Distutils setup file, used to install or test 'setuptools'
"""

import io
import os
import sys
import textwrap

# Allow to run setup.py from another directory.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

src_root = None

from distutils.util import convert_path

command_ns = {}
init_path = convert_path('setuptools/command/__init__.py')
with open(init_path) as init_file:
    exec(init_file.read(), command_ns)

SETUP_COMMANDS = command_ns['__all__']

import setuptools

scripts = []

def _gen_console_scripts():
    yield "easy_install = setuptools.command.easy_install:main"

    # Gentoo distributions manage the python-version-specific scripts
    # themselves, so those platforms define an environment variable to
    # suppress the creation of the version-specific scripts.
    var_names = (
        'SETUPTOOLS_DISABLE_VERSIONED_EASY_INSTALL_SCRIPT',
        'DISTRIBUTE_DISABLE_VERSIONED_EASY_INSTALL_SCRIPT',
    )
    if any(os.environ.get(var) not in (None, "", "0") for var in var_names):
        return
    yield ("easy_install-{shortver} = setuptools.command.easy_install:main"
        .format(shortver=sys.version[:3]))

console_scripts = list(_gen_console_scripts())

readme_file = io.open('README.rst', encoding='utf-8')

with readme_file:
    long_description = readme_file.read()

package_data = {
        'setuptools': ['script (dev).tmpl', 'script.tmpl', 'site-patch.py']}
force_windows_specific_files = (
    os.environ.get("SETUPTOOLS_INSTALL_WINDOWS_SPECIFIC_FILES")
    not in (None, "", "0")
)
if (sys.platform == 'win32' or (os.name == 'java' and os._name == 'nt')) \
        or force_windows_specific_files:
    package_data.setdefault('setuptools', []).extend(['*.exe'])
    package_data.setdefault('setuptools.command', []).extend(['*.xml'])

needs_pytest = set(['ptr', 'pytest', 'test']).intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []
needs_wheel = set(['release', 'bdist_wheel']).intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

setup_params = dict(
    name="setuptools",
    version="24.0.2",
    description="Easily download, build, install, upgrade, and uninstall "
                "Python packages",
    author="Python Packaging Authority",
    author_email="distutils-sig@python.org",
    long_description=long_description,
    keywords="CPAN PyPI distutils eggs package management",
    url="https://github.com/pypa/setuptools",
    src_root=src_root,
    packages=setuptools.find_packages(exclude=['*.tests']),
    package_data=package_data,

    py_modules=['easy_install'],

    zip_safe=True,

    entry_points={
        "distutils.commands": [
            "%(cmd)s = setuptools.command.%(cmd)s:%(cmd)s" % locals()
            for cmd in SETUP_COMMANDS
        ],
        "distutils.setup_keywords": [
            "eager_resources        = setuptools.dist:assert_string_list",
            "namespace_packages     = setuptools.dist:check_nsp",
            "extras_require         = setuptools.dist:check_extras",
            "install_requires       = setuptools.dist:check_requirements",
            "tests_require          = setuptools.dist:check_requirements",
            "setup_requires         = setuptools.dist:check_requirements",
            "entry_points           = setuptools.dist:check_entry_points",
            "test_suite             = setuptools.dist:check_test_suite",
            "zip_safe               = setuptools.dist:assert_bool",
            "package_data           = setuptools.dist:check_package_data",
            "exclude_package_data   = setuptools.dist:check_package_data",
            "include_package_data   = setuptools.dist:assert_bool",
            "packages               = setuptools.dist:check_packages",
            "dependency_links       = setuptools.dist:assert_string_list",
            "test_loader            = setuptools.dist:check_importable",
            "test_runner            = setuptools.dist:check_importable",
            "use_2to3               = setuptools.dist:assert_bool",
            "convert_2to3_doctests  = setuptools.dist:assert_string_list",
            "use_2to3_fixers        = setuptools.dist:assert_string_list",
            "use_2to3_exclude_fixers = setuptools.dist:assert_string_list",
        ],
        "egg_info.writers": [
            "PKG-INFO = setuptools.command.egg_info:write_pkg_info",
            "requires.txt = setuptools.command.egg_info:write_requirements",
            "entry_points.txt = setuptools.command.egg_info:write_entries",
            "eager_resources.txt = setuptools.command.egg_info:overwrite_arg",
            "namespace_packages.txt = setuptools.command.egg_info:overwrite_arg",
            "top_level.txt = setuptools.command.egg_info:write_toplevel_names",
            "depends.txt = setuptools.command.egg_info:warn_depends_obsolete",
            "dependency_links.txt = setuptools.command.egg_info:overwrite_arg",
        ],
        "console_scripts": console_scripts,

        "setuptools.installation":
            ['eggsecutable = setuptools.command.easy_install:bootstrap'],
    },


    classifiers=textwrap.dedent("""
        Development Status :: 5 - Production/Stable
        Intended Audience :: Developers
        License :: OSI Approved :: MIT License
        Operating System :: OS Independent
        Programming Language :: Python :: 2.6
        Programming Language :: Python :: 2.7
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.3
        Programming Language :: Python :: 3.4
        Programming Language :: Python :: 3.5
        Topic :: Software Development :: Libraries :: Python Modules
        Topic :: System :: Archiving :: Packaging
        Topic :: System :: Systems Administration
        Topic :: Utilities
        """).strip().splitlines(),
    extras_require={
        "ssl:sys_platform=='win32'": "wincertstore==0.2",
        "certs": "certifi==2016.2.28",
    },
    dependency_links=[
        'https://pypi.python.org/packages/source/c/certifi/certifi-2016.2.28.tar.gz#md5=5d672aa766e1f773c75cfeccd02d3650',
        'https://pypi.python.org/packages/source/w/wincertstore/wincertstore-0.2.zip#md5=ae728f2f007185648d0c7a8679b361e2',
    ],
    scripts=[],
    tests_require=[
        'setuptools[ssl]',
        'pytest>=2.8',
    ] + (['mock'] if sys.version_info[:2] < (3, 3) else []),
    setup_requires=[
    ] + pytest_runner + wheel,
)

if __name__ == '__main__':
    dist = setuptools.setup(**setup_params)
