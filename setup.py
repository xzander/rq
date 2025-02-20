"""
rq is a simple, lightweight, library for creating background jobs, and
processing them.
"""
import os
from setuptools import setup, find_packages


def get_version():
    basedir = os.path.dirname(__file__)
    try:
        with open(os.path.join(basedir, 'rq/version.py')) as f:
            locals = {}
            exec(f.read(), locals)
            return locals['VERSION']
    except FileNotFoundError:
        raise RuntimeError('No version info found.')


def get_requirements():
    basedir = os.path.dirname(__file__)
    try:
        with open(os.path.join(basedir, 'requirements.txt')) as f:
            return f.readlines()
    except FileNotFoundError:
        raise RuntimeError('No requirements info found.')


setup(
    name='rq',
    version=get_version(),
    url='https://github.com/nvie/rq/',
    license='BSD',
    author='Vincent Driessen',
    author_email='vincent@3rdcloud.com',
    description='RQ is a simple, lightweight, library for creating background '
                'jobs, and processing them.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data = {"rq": ["py.typed"]},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=get_requirements(),
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'rq = rq.cli:main',

            # NOTE: rqworker/rqinfo are kept for backward-compatibility,
            # remove eventually (TODO)
            'rqinfo = rq.cli:info',
            'rqworker = rq.cli:worker',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Monitoring',

    ]
)
