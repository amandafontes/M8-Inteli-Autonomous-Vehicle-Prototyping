import os
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import ExecuteProcess, IncludeLaunchDescription, TimerAction

def generate_launch_description():

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch'),
            '/turtlebot3_world.launch.py'
        ])
    )

    rviz = ExecuteProcess(
            cmd=['ros2', 'launch', 'turtlebot3_navigation2', 'navigation2.launch.py', 'use_sim_time:=True', 'map:=mapa.yaml'],
            name='navigator_ros2',
            output='screen'
        )

    delay = ExecuteProcess(
        cmd=["sleep", "4"],
        output="screen",
    )

    waypoints = Node(
        package='navigation',
        executable='script',
        output='screen',
    )

    return LaunchDescription([
        gazebo,
        rviz,
        delay,
        waypoints
    ])