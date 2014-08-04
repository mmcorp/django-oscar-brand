#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='django-oscar-brands',
    version="0.0.1",
    url='https://github.com/tangentlabs/django-oscar-brands',
    author="Milkov Vladimir",
    author_email="vladimir@milkov.pro",
    description="An extension for Oscar to include brands",
    long_description=open(
        os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    keywords="django, oscar, e-commerce",
    license='BSD',
    platforms=['linux'],
    packages=find_packages(exclude=["sandbox*", "tests*"]),
    include_package_data=True,
    install_requires=[
        'django-oscar>=0.5',
        'requests>=1.1',
    ],
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ])
