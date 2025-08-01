from setuptools import find_packages, setup

package_name = 'talkrbot_llm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vedantso',
    maintainer_email='ved.06.soni@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'llm_node = talkrbot_llm.llm_node:main',
            'intent_refiner_node = talkrbot_llm.intent_refiner_node:main',
            'groot_planner_node = talkrbot_llm.groot_planner_node:main',
            'memory_node = talkrbot_llm.memory_node:main',
        ],
    },
)
