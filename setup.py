#!/usr/bin/env python

from os.path import join
from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib


setup(
    name='crazy-baboon',
    version='0.1.0',
    description='A dummy project to quickly test Baboon project.',
    author='Sandro Munda',
    author_email='munda.sandro@gmail.com',
    license='MIT',
    url='http://baboon-project.org',
    download_url='https://github.com/SeyZ/crazy-baboon/tarball/master',
    packages=find_packages(),
    scripts=['bin/crazy-baboon'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: Other',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Quality Assurance'
    ],
)
