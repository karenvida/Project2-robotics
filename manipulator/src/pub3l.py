#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import Float64  # dada el tipo de dato de las dependencias


class Pub():
    def __init__(self):

        self.sp_publisher0 = rospy.Publisher('/manipulator/joint0_position_controller/command', Float64, queue_size=1)
        self.sp_publisher1 = rospy.Publisher('/manipulator/joint1_position_controller/command', Float64, queue_size=1)
        self.sp_publisher2 = rospy.Publisher('/manipulator/joint2_position_controller/command', Float64, queue_size=1)
        #self.command = Float64()
        self.command0 = 0.0
        self.command1 = 0.0
        self.command2 = 0.0
        self.rate = rospy.Rate(10)  # 10hz
        self.ctrl_c = False

        rospy.on_shutdown(self.shutdownhook)

    
    def move_robot(self):
        while not self.ctrl_c: 
            self.command0 = 90.0
            self.command1 = 180.0
            self.command2 = 5.0
            self.command0 = self.command0*math.pi/180
            self.sp_publisher0.publish(self.command0)
            self.command1 = self.command1*math.pi/180
            self.sp_publisher1.publish(self.command1)
            self.command2 = self.command2*math.pi/180
            self.sp_publisher2.publish(self.command2)
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