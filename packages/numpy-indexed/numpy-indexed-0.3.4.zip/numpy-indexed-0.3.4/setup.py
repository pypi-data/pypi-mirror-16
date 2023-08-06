from setuptools import find_packages
from distutils.core import setup

import pkg_conf


setup(
    keywords = "numpy group_by set-operations indexing",
    name=pkg_conf.PKG_NAME,
    version=pkg_conf.get_version(),
    packages=find_packages(),
    install_requires=['pyyaml', 'future'],
    description=pkg_conf.get_recipe_meta()['about']['summary'],
    long_description=pkg_conf.get_readme_rst(),
    author=pkg_conf.AUTHOR,
    author_email=pkg_conf.AUTHOR_EMAIL,
    url=pkg_conf.get_recipe_meta()['about']['home'],
    license=pkg_conf.get_recipe_meta()['about']['license'],
    platforms='any',
    classifiers=[
        "Development Status :: 4 - Beta",
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        "Topic :: Utilities",
        'Topic :: Scientific/Engineering',
        'License :: {}'.format(pkg_conf.get_recipe_meta()['about']['license']),
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
)