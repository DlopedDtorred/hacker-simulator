#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Setup script for Hacker Simulator 2077
"""

from setuptools import setup, find_packages
import os

# Read README.md for long description
try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except:
    long_description = "Hacker Simulator 2077 - Terminal-based hacking game"

setup(
    name="hacker-simulator-2077",
    version="10.0.0",
    author="DlopedDtorred",
    author_email="tu-email@ejemplo.com",
    description="Hacker Simulator 2077 - Terminal-based hacking game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DlopedDtorred/hacker-simulator",
    project_urls={
        "Bug Reports": "https://github.com/DlopedDtorred/hacker-simulator/issues",
        "Source": "https://github.com/DlopedDtorred/hacker-simulator",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    install_requires=[
        "colorama>=0.4.4",
    ],
    entry_points={
        "console_scripts": [
            "hacker-simulator=cyberdex:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    py_modules=["cyberdex"],
)