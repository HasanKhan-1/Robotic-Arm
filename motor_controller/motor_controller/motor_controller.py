import time 
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

import board
import rclpy
from rclpy import Node
import dataclasses
from std_msgs.msg import Float64

# @dataclasses
# class MotorController_Parameters():
#     frequency : int

# Define the Motor Controller
class MG996R_Controller(Node): #TODO: 1.Why do we need to pass in node? 

    def __init__(self,channel): # TODO: 2.Why do we pass self here again? 
        super().__init__('motor_controller_G996R')# TODO: 3.What does super() and init do lmoa
        # self.publisher = self.create_publisher(Float64,'topic',10)
        self.channel = channel
        # time_period = 0.5
        i2c_communication = board.I2C()
        pca_9685_instance = PCA9685(i2c_communication)
        pca_9685_instance.frequency = 50 #TODO: ADD THIS TO DATA CLASS
        self.new_servo = servo.Servo(pca_9685_instance.channels[self.channel])#Assign to the correct channel

        # self.timer = self.create_timer(time_period,self.timer_callback)
    
    def move_motor(self,angle):
        for i in range(180):
            self.new_servo.angle = i
            time.sleep(0.03)
        for i in range(180):
            self.new_servo = 180 - i
            time.sleep(0.03)

        
    # def timer_callback(self):
    #     msg = String()
    #     msg.data = 
        
        
        

    # def motor_speed_callback(self):
    #     return None 
    





def main(args=None):
    rclpy.init(args=args)
    motor = MG996R_Controller(3)
    motor.move_motor()
    rclpy.spin(motor)
    motor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

    # return 0
