import time 
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

import board
import rclpy
from rclpy import Node
import dataclasses
from std_msgs.msg import Float64

@dataclasses
class MotorController_Parameters():
    frequency : int
    active_channels: list
    motor_speed: float



# Define the Motor Controller
class MG996R_Controller(Node): #TODO: 1.Why do we need to pass in node? 

    def __init__(self): # TODO: 2.Why do we pass self here again? 
        super().__init__('motor_controller_G996R')# TODO: 3.What does super() and init do lmoa
        i2c_communication = board.I2C()
        pca_9685_instance = PCA9685(i2c_communication)
        
    def timer_callback(self):
        return None
    def motor_speed_callback(self):
        return None 
    





def main():
    return None

if __name__ == '__main__':
    main()

    # return 0
