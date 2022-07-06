#!/usr/bin/env python3

import rospy
from moveit_commander import MoveGroupCommander
import rospy
import geometry_msgs.msg
rospy.init_node('robot_controller_moveit')



group = MoveGroupCommander('tool_0')

pos = [0.2, 0.3, 0.1]

group.set_position_target(pos,'tip')

plan = group.go()

group.stop()
