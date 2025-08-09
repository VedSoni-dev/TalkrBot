from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    planner_backend_arg = DeclareLaunchArgument(
        'planner_backend', default_value='gemini', description='Planner backend (gemini|groot)'
    )
    use_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time', default_value='true', description='Use simulated time'
    )

    planner_backend = LaunchConfiguration('planner_backend')
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Common params for all nodes
    common_params = [{ 'use_sim_time': use_sim_time }]

    aac_node = Node(
        package='talkrbot_aac',
        executable='aac_node',
        name='aac_node',
        output='screen',
        respawn=True,
        parameters=common_params,
    )

    intent_refiner_node = Node(
        package='talkrbot_llm',
        executable='intent_refiner_node',
        name='intent_refiner_node',
        output='screen',
        respawn=True,
        parameters=common_params,
        remappings=[
            ('/aac_input', '/aac_input'),
            ('/refined_intent', '/refined_intent'),
        ]
    )

    groot_planner_node = Node(
        package='talkrbot_llm',
        executable='groot_planner_node',
        name='groot_planner_node',
        output='screen',
        respawn=True,
        parameters=[{ 'planner_backend': planner_backend }, *common_params],
        remappings=[
            ('/refined_intent', '/refined_intent'),
            ('/skill_plan', '/skill_plan'),
        ]
    )

    skill_executor_node = Node(
        package='talkrbot_planner',
        executable='skill_executor_node',
        name='skill_executor_node',
        output='screen',
        respawn=True,
        parameters=common_params,
        remappings=[
            ('/skill_plan', '/skill_plan'),
            ('/execution_feedback', '/execution_feedback'),
        ]
    )

    # Optional memory/task history. If you want only logger, run task_history_manager
    memory_logger_node = Node(
        package='talkrbot_feedback',
        executable='task_history_manager',
        name='task_history_manager',
        output='screen',
        respawn=True,
        parameters=common_params,
    )

    group = GroupAction([
        aac_node,
        intent_refiner_node,
        groot_planner_node,
        skill_executor_node,
        memory_logger_node,
    ])

    return LaunchDescription([
        planner_backend_arg,
        use_sim_time_arg,
        group,
    ]) 