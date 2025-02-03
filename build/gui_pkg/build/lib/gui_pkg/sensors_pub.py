#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random
class Sensors(Node):
  def __init__(self):
    super().__init__('sensors_pub')
    

    ### implement the sensors publisher 



     
def main(args=None):
    
    rclpy.init(args=args)
    sensorsPublisher=Sensors()
    rclpy.spin(sensorsPublisher)
    rclpy.shutdown()




