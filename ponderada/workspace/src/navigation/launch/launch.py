from launch_ros.actions import Node
from launch import LaunchDescription
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import ExecuteProcess, IncludeLaunchDescription, TimerAction

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'run', 'turtlebot3_gazebo', 'turtlebot3_world.launch.py'],
            output='screen',
        ),

        ExecuteProcess(
            cmd=['ros2', 'launch', 'turtlebot3_navigation2', 'navigation2.launch.py', 'use_sim_time:=True', 'map:=../../map_saver/maps/map.yaml'],
            output='screen',
        ),

        ExecuteProcess(
            cmd=['ros2', 'run', 'navigation', 'script'],
            output='screen',
            prefix = 'gnome-terminal --'
        )
])