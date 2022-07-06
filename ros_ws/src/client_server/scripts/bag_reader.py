#!/usr/bin/env python3

import rospy
import rosbag

#initialize node
rospy.init_node("bag_reader")

bag_obj = rosbag.Bag("/home/alynada/ros_ws/src/client_server/bags/publisher.bag")

for topic_name, msg, time in bag_obj:
    if topic_name == '/phrase':
        print('message = ',msg)
        print('time = ', time)

bag_obj.close()