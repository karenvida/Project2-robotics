#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import Float64  # dada el tipo de dato de las dependencias


class Pub():
    def __init__(self):

        self.sp_publisher = rospy.Publisher('/brazo/joint0_position_controller/command', Float64, queue_size=1)
        #self.command = Float64()
        self.command0 = 0.0
        self.rate = rospy.Rate(10)  # 10hz
        self.ctrl_c = False

        rospy.on_shutdown(self.shutdownhook)

    
    def move_robot(self):
        while not self.ctrl_c: 
            self.command0 = 90.0
            self.command0 = self.command0*180/math.pi
            self.sp_publisher.publish(self.command0)
            self.rate.sleep()
            #break

    def shutdownhook(self):
        # trabaja mucho mejor que el rospy.is_shutdown()
        self.ctrl_c = True


# Es una buena practica para que puedan usar este coódigo en otro código
if __name__ == '__main__':
    rospy.init_node('publish_test', anonymous=True)
    ros_manipulator = Pub()  # objeto
    try:
        ros_manipulator.move_robot()  # rosbot?object.funcion ejecutable
    except rospy.ROSInterruptException:
        pass