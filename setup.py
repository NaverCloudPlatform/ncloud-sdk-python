# coding: utf-8

"""
    sdk

    OpenAPI spec version: 2018-06-21T02:27:10Z

"""

import io
from setuptools import setup, find_packages  # noqa: H301

NAME = "ncloud-sdk"
VERSION = "1.1.7"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15"
            , "six >= 1.10"
            , "certifi"
            , "python-dateutil"
            , "ncloud-apikey >= 1.0.5"
            , "ncloud-server >= 1.1.3"
            , "ncloud-loadbalancer >= 1.1.1"
            , "ncloud-autoscaling >= 1.1.1"
            , "ncloud-monitoring >= 1.1.6"
            , "ncloud-cdn >= 1.1.1"
            , "ncloud-clouddb >= 1.1.1"
            , "ncloud-vserver >= 1.0.1"
            , "ncloud-vnas >= 1.0.1"
            , "ncloud-vpc >= 1.0.1"
            , "ncloud-vautoscaling >= 1.0.0"
            , "ncloud-vloadbalancer >= 1.0.0"]

with io.open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="ncloud-sdk",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=["ncloud-sdk", "ncloud"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True
)
