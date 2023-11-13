from launch_ros.actions import Node
from launch import LaunchDescription
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import ExecuteProcess, IncludeLaunchDescription, TimerAction

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'run', 'nav2_map_server', 'map_saver_cli', '-f', './src/map_saver/maps/map'],
            output='screen',
        ),

        ExecuteProcess(
            cmd=['ros2', 'run', 'map_saver', 'script'],
            output='screen',
            prefix = 'gnome-terminal --'
        )
])
