#!/usr/bin/env python3
import sys
import cv2
import rclpy
import numpy as np
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from std_msgs.msg import Int32
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QLabel

class CameraThread(QThread):
    frame_signal = Signal(QPixmap)  

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.running = True

    def run(self):
        cap = cv2.VideoCapture(self.url)
        if not cap.isOpened():
            print("Error: Could not open camera stream!")
            return
        
        while self.running:
            ret, frame = cap.read()
            if not ret:
                print("Error: Couldn't read frame")
                break

          
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.frame_signal.emit(pixmap)

        cap.release()

 


