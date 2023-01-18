import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="blip",
    version="1.0",
    description="BLIP: A Pretrained Vision-and-Language Model for Image Captioning",
    long_description=open('README.md').read(),
    author="salesforce",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
