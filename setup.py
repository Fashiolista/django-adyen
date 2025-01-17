#!/usr/bin/env python

from setuptools import setup, find_packages

try:
    README = open('README.rst').read()
except:
    README = None

try: 
    LICENSE = open('LICENSE.txt').read()
except: 
    LICENSE = None

setup(
    name = 'django-adyen',
    version = '0.1.1',
    description='Python/Django interface to the Adyen payment gateway.',
    long_description=README,
    author = 'Mathijs de Bruin',
    author_email = 'mathijs@mathijsfietst.nl',
    license = LICENSE,
    url = 'http://github.com/dokterbob/django-adyen/',
    packages = find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
    ],
)
