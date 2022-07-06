#!/usr/bin/env python3

import rospy
from moveit_commander import MoveGroupCommander
from sensor_msgs.msg import JointState

rospy.init_node('robot_controller_moveit')



group = MoveGroupCommander('tool_0')

msg = JointState()

msg.name = ['base_link1', 'link1_link2', 'link2_link3', 'link3_link4', 'link4_link5', 'link5_link6']
msg.position = [1.57, 0, -1.57, 1.57, 0, 0]

group.set_joint_value_target(msg)

group.go()