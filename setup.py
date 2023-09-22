# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

setup(
    name="omniindex",
    version="0.1.15",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "requests",
        "pandas",
        "pytest",
        "simplejson",
        "delorean"
    ],
    include_package_data=True,
    author="James Stanbridge",
    author_email="james@omniindex.io",
    description="A Python package for interacting with the OmniIndex Homomorphic Encrypted Blockchain API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OmniIndex/python",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
)
