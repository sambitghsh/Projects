import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize    
     
class MainWindow(QMainWindow):
    def __init__(self,store):
        QMainWindow.__init__(self)
        self.store=store
        self.clickMethod()      
    
    def clickMethod(self):
        QMessageBox.about(self, "Warning", self.store)
 
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow("WARNING")
    
    sys.exit( app.exec_() )
