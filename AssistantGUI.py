from PySide2 import sys
from AssistantUI import Ui_Form
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
import Assistant
import sys
import time
import datetime
import socket
import wolframalpha
from requests import get



class mainT(QThread):

    def __init__(self):
        super(mainT,self).__init__()

    def run(self): 
        Assistant.Task_Gui()


startExec = mainT()

class Main_window(QMainWindow):

    def __init__(self):
        super().__init__()


        self.gui = Ui_Form()
        self.gui.setupUi(self)

        self.gui.exit.clicked.connect(self.close)


        self.date = time.strftime("%A, %d %B")
        self.gui.date.setText("<font color='#fff833'><p style='font-size:27px,'>"+self.date+"</font>")
        self.gui.date.setFont(QFont(QFont('Poor Richard')))

        self.gui.name.setText("<font color='white'><p style='text-align:center;font-size:90px,'><b><em>Gideon</font></p></b><em>")
        self.gui.name.setFont(QFont(QFont('Forte')))

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)  
        self.showTime()
        self.Temperature()
        self.IP()
        startExec.start() 
        self.showMaximized()
        
    def showTime(self):
  
        current_time = QTime.currentTime()
  
        label_time = current_time.toString('hh:mm:ss')
  
        self.gui.time.setText("<font color='#57ff78'><p style='font-size:65px,'>"+label_time+"</font></p>")
        self.gui.time.setFont(QFont(QFont('DS-Digital')))

    def Temperature(self):

        try:
            app = wolframalpha.Client("48RLHU-QAT37WAXH8")
        except Exception as e:
            print(e)

        query = "Temperature"
        res = app.query(query)
        temperature = next(res.results).text[:5]
        
        self.gui.temp.setText("<font color='#fff833'><p style='font-size:40px,'>"+temperature+"</font></p>")
        self.gui.temp.setFont(QFont(QFont('Poor Richard')))

    def IP(self):

        try:
            ip = get('https://api.ipify.org').text
        
        except Exception as e:
            print(e)

        self.gui.label_ip.setText("<font color='#fff833'><p style='font-size:30px,'>""IP :  "+ip+"</font></p>")
        self.gui.label_ip.setFont(QFont(QFont('Poor Richard')))

app = QtWidgets.QApplication(sys.argv)
assistant_gui = Main_window()
assistant_gui.show()
sys.exit(app.exec_()) 

