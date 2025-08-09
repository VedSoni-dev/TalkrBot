from setuptools import setup

package_name = 'talkrbot_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/demo_pipeline.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vedantso',
    maintainer_email='ved.06.soni@gmail.com',
    description='Unified launch files for TalkrBot',
    license='Apache-2.0',
) 