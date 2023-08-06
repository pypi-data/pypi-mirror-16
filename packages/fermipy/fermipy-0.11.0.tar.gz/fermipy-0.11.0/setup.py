#!/usr/bin/env python
from setuptools import setup, find_packages
from fermipy.version import get_git_version

setup(
    name='fermipy',
    version=get_git_version(),
    author='The Fermipy developers',
    author_email='fermipy.developers@gmail.com',
    description='A Python package for analysis of Fermi-LAT data',
    license='BSD',
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    url="https://github.com/fermiPy/fermipy",
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Development Status :: 4 - Beta',
    ],
    scripts=[],
    entry_points={'console_scripts': [
        'fermipy-dispatch = fermipy.scripts.dispatch:main',
        'fermipy-clone-configs = fermipy.scripts.clone_configs:main',
        'fermipy-collect-sources = fermipy.scripts.collect_sources:main',
        'fermipy-cluster-sources = fermipy.scripts.cluster_sources:main',
    ]},
    install_requires=[
        'numpy >= 1.6.1',
        'astropy >= 1.0',
        'matplotlib >= 1.4.0',
        'scipy >= 0.14',
        'pyyaml',
        'healpy',
        'wcsaxes',
    ],
    extras_require=dict(
        all=[],
    ),
)
