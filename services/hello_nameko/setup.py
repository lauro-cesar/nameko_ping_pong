#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="hello_nameko",
    version="0.0.1",
    description="Hello nameko",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "marshmallow",
        "dnspython3",
        "nameko==v3.0.0-rc9",
    ],
    extras_require={
        "dev": [
            "tox",
            "pytest==4.5.0",
            "coverage==4.5.3",
            "flake8==3.7.7",
        ],
    },
    zip_safe=True,
)
