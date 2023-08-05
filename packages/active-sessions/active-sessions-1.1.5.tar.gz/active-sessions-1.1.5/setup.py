# -*- coding: utf8 -*-
#
# This file were created by Python Boilerplate. Use boilerplate to start simple
# usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/boilerplate/
#

import os
from setuptools import setup, find_packages


# Meta information
name = 'active-sessions'
project = 'active_sessions'
author = 'Tiago Assuncao'
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)


# Save version and author to __meta__.py
with open(os.path.join(dirname, 'src', project, '__meta__.py'), 'w') as F:
    F.write('__version__ = %r\n__author__ = %r\n' % (version, author))


setup(
    # Basic info
    name=name,
    version=version,
    author=author,
    author_email='tiago@sof2u.com',
    url='https://github.com/DAS2016-1/about_us',
    description='Shows the online users in the system using Django',
    long_description=open('README.rst').read(),

    # Classifiers (see https://pypi.python.org/pypi?%3Aaction=list_classifiers)
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],

    # Packages and depencies
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[],
    extras_require={
        'testing': ['pytest'],
    },

    # Scripts
    entry_points={
        'active_session': [
            'active_session = active_sessions.__main__:main'
            'active-sessions = active_sessions.__main__:get_current_users'
        ],
    },

    # Other configurations
    zip_safe=False,
    platforms='any',
    test_suite='%s.test.test_%s' % (name, name),
)
