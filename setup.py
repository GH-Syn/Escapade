#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Escapade",
    version="1.0.0",
    author="Joshua Rose",
    author_email="joshuarose099@gmail.com",
    description="Plot your escape in this thrilling puzzle adventure game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GH-Syn/Escapade",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment :: Puzzle",
    ],
    python_requires='>=3.9',
    install_requires=[
        'pygame',
    ],
    entry_points={
        'console_scripts': [
            'Escapade=game.game:main',
        ],
    },
)
