"""
Copyright 2016-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

    http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
"""

from setuptools import setup, find_packages

setup(
    name="cfn_flip",
    version="1.3.0",
    description="Convert AWS CloudFormation templates between JSON and YAML formats",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bennyandthetuna/cfn-flip",
    author="Ben Lampert",
    author_email="benjamin.j.lampert@gmail.com",
    license="Apache2",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "Click==8.5.1",
        "PyYAML==6.0.3",
        "six==1.17.0",
    ],
    tests_require=[
        'pytest==9.2.0', 
        'pytest-cov==7.1.0',
        'pytest-runner==6.0.1'
    ],
    zip_safe=False,
    entry_points={
        "console_scripts": ["cfn-flip=cfn_flip.main:main"],
    },
)
