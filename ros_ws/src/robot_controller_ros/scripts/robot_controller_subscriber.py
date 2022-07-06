#!/usr/bin/env python3

from geometry_msgs.msg import Pose
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg



def callback(self):

    ## First initialize `moveit_commander`_ and a `rospy`_ node:
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = 'tool_0'
    move_group = moveit_commander.MoveGroupCommander(group_name)

    ## Create a `DisplayTrajectory`_ ROS publisher which is used to display
    ## trajectories in Rviz:
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=1)

    pose_goal = Pose()

    pose_goal.orientation.w = self.orientation.w
    pose_goal.orientation.x = self.orientation.x
    pose_goal.orientation.y = self.orientation.y
    pose_goal.orientation.z = self.orientation.z

    pose_goal.position.x = self.position.x
    pose_goal.position.y = self.position.y
    pose_goal.position.z = self.position.z

    rospy.loginfo(pose_goal)

    move_group.set_pose_target(pose_goal)
    plan = move_group.go(wait=True)
    # Calling `stop()` ensures that there is no residual movement
    move_group.stop()
    # It is always good to clear your targets after planning with poses.
    move_group.clear_pose_targets()


def subscriber():

	rospy.init_node('Subscriber',anonymous=True)
	rospy.Subscriber('pose', Pose, callback)
	rospy.spin()

if __name__ == '__main__':
  subscriber()