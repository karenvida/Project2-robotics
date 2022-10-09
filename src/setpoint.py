#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64


def talker():
    pub = rospy.Publisher(
        '/brazo/joint0_position_controller/command', Float64, queue_size=10)
    rospy.init_node('brazo_talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        set_point1 = 3.0
        #rospy.loginfo(set_point1)
        pub.publish(set_point1)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
