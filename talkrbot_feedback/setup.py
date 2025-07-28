from setuptools import find_packages, setup

package_name = 'talkrbot_feedback'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/config', ['config/user_profiles.json']),
    ],
    install_requires=['setuptools', 'scikit-learn', 'numpy'],
    zip_safe=True,
    maintainer='vedantso',
    maintainer_email='ved.06.soni@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'failure_handler_node = talkrbot_feedback.failure_handler_node:main',
            'speech_node = talkrbot_feedback.speech_node:main',
            'user_profile_manager = talkrbot_feedback.user_profile_manager:main',
            'task_history_manager = talkrbot_feedback.task_history_manager:main',
            'history_query_node = talkrbot_feedback.history_query_node:main',
            'semantic_history_query_node = talkrbot_feedback.semantic_history_query:main',
        ],
    },
)
