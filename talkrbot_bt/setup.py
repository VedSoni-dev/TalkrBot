from setuptools import find_packages, setup

package_name = 'talkrbot_bt'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/bt', ['../talkrbot_bt/bring_object.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vedantso',
    maintainer_email='ved.06.soni@gmail.com',
    description='Behavior Tree executor for TalkrBot',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bt_executor_node = talkrbot_bt.bt_executor_node:main',
        ],
    },
) 