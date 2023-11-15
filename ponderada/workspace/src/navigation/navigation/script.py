#! /usr/bin/env python3

import rclpy
from math import pi
import tf_transformations
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler
from nav2_simple_commander.robot_navigator import BasicNavigator

def create_pose_stamped(navigator, pos_x, pos_y, rot_z):
    q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, rot_z)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()
    pose.pose.position.x = pos_x
    pose.pose.position.y = pos_y
    pose.pose.position.z = pos_x
    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w
    return pose

def main():
    
    rclpy.init()

    navigator = BasicNavigator()

    initial_pose = create_pose_stamped(navigator, -1.23, -2.4, 0.0)
    goal_pose = create_pose_stamped(navigator, 2.5, 2.5, 0.00247)

    waypoints = [initial_pose, goal_pose, initial_pose]

    navigator.waitUntilNav2Active()
    
    navigator.followWaypoints(waypoints)

    while not navigator.isTaskComplete():
        print(navigator.getFeedback())

    rclpy.shutdown()

if __name__ == '__main__':
    main()