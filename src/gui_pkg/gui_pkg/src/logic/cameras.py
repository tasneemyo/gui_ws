#!/usr/bin/env python3

import sys,rclpy
from rclpy.node import Node
from PySide6.QtWidgets import QWidget
from rclpy.executors import MultiThreadedExecutor
from std_msgs.msg import Int32
sys.path.append("src/gui_pkg/gui_pkg/src/ui_files")
from cameras_ui import Ui_Form as View
from threads import CameraThread

class Cameras(QWidget, View):
    def __init__(self, parent=None, executor: MultiThreadedExecutor = None):
        super(Cameras, self).__init__(parent)
        self.setupUi(self)

       
        self.executor = executor
        # self.sensorsNode = Node("sensors_sub")
        # self.subscriber = self.sensorsNode.create_subscription(Int32, "/sensors_data", self.get_sensorData, 10)
        # self.executor.add_node(self.sensorsNode)

       
        self.leftCamera_thread = None
        self.start_leftCamera()  

    def start_leftCamera(self):
       
        url = 0 
        if self.leftCamera_thread and self.leftCamera_thread.isRunning():
            self.leftCamera_thread.stop()
            self.leftCamera_thread.wait()

        self.leftCamera_thread = CameraThread(url)
        self.leftCamera_thread.frame_signal.connect(self.update_frame) 
        self.leftCamera_thread.start()

    def update_frame(self, pixmap):
        self.left_camera.setPixmap(pixmap)

    def get_sensorData(self, msg: Int32):
        
        pass

 

    
    