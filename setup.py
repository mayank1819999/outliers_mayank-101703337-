# -*- coding: utf-8 -*-
"""
Created on Sun Feb 09 19:49:25 2020

@author: mayank_singh
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outliers_mayank(101703337)", # Replace with your own username
    version="0.0.3",
    author="mayank_singh",
    author_email="mayank1819999@gmail.com",
    description="An outlier removal method (By removing rows)",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/mayank1819999/outliers_mayank(101703337)",
    download_url="https://github.com/mayank1819999/outliers_mayank-101703337-/archive/0.0.3.tar.gz",
    packages=["outliers_mayank(101703337)"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
