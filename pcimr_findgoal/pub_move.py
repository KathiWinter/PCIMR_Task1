#!/usr/bin/env python

import rospy
from std_msg.msg import String
from pcimr_findgoal import * 

def talker():
    pub = rospy.Publisher('move', String, queue_size=10)
    rospy.init_node('talker', anonymoud=True)
    rate = rospy.Rate(10)
    while not rospy._is_shutdown():
        direction = "N"
        rospy.loginfo(direction)
        pub.publish(direction)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass