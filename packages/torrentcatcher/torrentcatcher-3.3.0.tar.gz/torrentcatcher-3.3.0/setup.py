#!/usr/bin/env python
from setuptools import setup

setup(
    name="torrentcatcher",
    packages=['torrentcatcher'],
    version="3.3.0",
    license="GPLv3",
    url="http://archangelic.github.io/torrentcatcher/",
    description=("Takes torrent or magnet links from rss feeds you provide, "
                 "parses them and sends them to transmission."),
    author="Michael Hancock",
    author_email="michaelhancock89@gmail.com",
    download_url=(
        "https://github.com/archangelic/torrentcatcher/tarball/v3.3.0"
    ),
    install_requires=[
        'configobj>=4.7.0',
        'feedparser>=5.1.3',
        'tabulate>=0.7.3',
        'transmissionrpc>=0.11',
    ],
    scripts=['bin/torrentcatcher'],
    keywords=['torrent', 'rss', 'transmission'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Internet',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
    ]
)
