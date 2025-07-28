from setuptools import find_packages
from setuptools import setup

setup(
    name='talkrbot_msgs',
    version='0.0.0',
    packages=find_packages(
        include=('talkrbot_msgs', 'talkrbot_msgs.*')),
)
