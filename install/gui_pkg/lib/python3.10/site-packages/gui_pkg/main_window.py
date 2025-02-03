#!/usr/bin/env python3

import sys,rclpy
from PySide6.QtWidgets import QMainWindow,QApplication
from rclpy.executors import MultiThreadedExecutor
from threading import Thread
sys.path.append("src/gui_pkg/gui_pkg/src/ui_files")
from main_window_ui import Ui_MainWindow as View
sys.path.append("src/gui_pkg/gui_pkg/src/logic")
from cameras import Cameras


class GUI(QMainWindow, View):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.setupUi(self)
        rclpy.init()
        self.setWindowTitle("Torpedo GUI")
        self.executor = MultiThreadedExecutor()
        self.cameras_tab = Cameras(executor=self.executor)
        self.tabWidget.addTab(self.cameras_tab, "Cameras Tab")
       

        executor_thread = Thread(target=self.executor.spin, daemon=True)
        executor_thread.start()
    


def main(args=None):
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    app.exec()