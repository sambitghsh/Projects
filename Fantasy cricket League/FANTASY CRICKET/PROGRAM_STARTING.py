# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
import side_sql
import sample
import back
class Ui_MainWindow(object):
    def fetch_data(self):
        if self.rb1.isChecked()==True:
            self.lw1.clear()
            self.record=side_sql.fetch_bat()
            for data in self.record:
                self.lw1.addItem(data[0])
        else:
            pass
        if self.rb2.isChecked()==True:
            self.lw1.clear()
            self.record=side_sql.fetch_ball()
            for data in self.record:
                self.lw1.addItem(data[0])
        else:
            pass
        if self.rb4.isChecked()==True:
            self.lw1.clear()
            self.record=side_sql.fetch_wk()
            for data in self.record:
                self.lw1.addItem(data[0])
        else:
            pass
        if self.rb3.isChecked()==True:
           self.lw1.clear()
           self.record=side_sql.fetch_ar()
           for data in self.record:
                self.lw1.addItem(data[0])
        else:
            pass
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(747, 588)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.l1 = QtWidgets.QLineEdit(self.centralwidget)
        self.l1.setReadOnly(True)
        self.l1.setObjectName("l1")
        self.horizontalLayout.addWidget(self.l1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.l2 = QtWidgets.QLineEdit(self.centralwidget)
        self.l2.setReadOnly(True)
        self.l2.setObjectName("l2")
        self.horizontalLayout.addWidget(self.l2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.l3 = QtWidgets.QLineEdit(self.centralwidget)
        self.l3.setReadOnly(True)
        self.l3.setObjectName("l3")
        self.horizontalLayout.addWidget(self.l3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.l4 = QtWidgets.QLineEdit(self.centralwidget)
        self.l4.setReadOnly(True)
        self.l4.setObjectName("l4")
        self.horizontalLayout.addWidget(self.l4)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.l5 = QtWidgets.QLineEdit(self.centralwidget)
        self.l5.setReadOnly(True)
        self.l5.setObjectName("l5")
        self.horizontalLayout_2.addWidget(self.l5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.l6 = QtWidgets.QLineEdit(self.centralwidget)
        self.l6.setReadOnly(True)
        self.l6.setObjectName("l6")
        self.horizontalLayout_3.addWidget(self.l6)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rb1 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb1.setFont(font)
        self.rb1.setObjectName("rb1")
        self.horizontalLayout_4.addWidget(self.rb1)
        self.rb2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb2.setFont(font)
        self.rb2.setObjectName("rb2")
        self.horizontalLayout_4.addWidget(self.rb2)
        self.rb3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb3.setFont(font)
        self.rb3.setObjectName("rb3")
        self.horizontalLayout_4.addWidget(self.rb3)
        self.rb4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb4.setFont(font)
        self.rb4.setObjectName("rb4")
        self.horizontalLayout_4.addWidget(self.rb4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.lw1 = QtWidgets.QListWidget(self.centralwidget)
        self.lw1.setObjectName("lw1")
        self.verticalLayout.addWidget(self.lw1)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.l7 = QtWidgets.QLineEdit(self.centralwidget)
        self.l7.setReadOnly(True)
        self.l7.setObjectName("l7")
        self.horizontalLayout_5.addWidget(self.l7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.lw2 = QtWidgets.QListWidget(self.centralwidget)
        self.lw2.setObjectName("lw2")
        self.verticalLayout_2.addWidget(self.lw2)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 747, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage = QtWidgets.QMenu(self.menubar)
        self.menuManage.setObjectName("menuManage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.actionNew_Team.setFont(font)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpeb_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.actionOpeb_Team.setFont(font)
        self.actionOpeb_Team.setObjectName("actionOpeb_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.actionSave_Team.setFont(font)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.actionEvaluate_Team.setFont(font)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage.addAction(self.actionNew_Team)
        self.menuManage.addAction(self.actionOpeb_Team)
        self.menuManage.addAction(self.actionSave_Team)
        self.menuManage.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage.menuAction())
        self.rb1.setCheckable(False)
        self.rb2.setCheckable(False)
        self.rb3.setCheckable(False)
        self.rb4.setCheckable(False)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.rb1.toggled.connect(self.fetch_data)
        self.rb2.toggled.connect(self.fetch_data)
        self.rb3.toggled.connect(self.fetch_data)
        self.rb4.toggled.connect(self.fetch_data)
        self.lw1.itemDoubleClicked.connect(self.removelist1)
        self.lw2.itemDoubleClicked.connect(self.removelist2)
        self.menuManage.triggered[QtWidgets.QAction].connect(self.menufunction)

    def cal_points1(self,item):
        val=side_sql.fetch_value(item.text())
        print(val)
        self.v=int(self.l5.text())
        self.v-=val[0]
        self.v1=int(self.l6.text())
        self.v1+=val[0]
        self.l6.setText(str(self.v1))
        self.l5.setText(str(self.v))

    def removelist1(self,item):
        date=side_sql.fetch_roll(item.text())
        val=side_sql.fetch_value(item.text())
        if date[0]=="Bat":
           print(int(self.l1.text()))
           self.d=int(self.l1.text())
           if self.d<3:
                self.d+=1
                self.l1.setText(str(self.d))
                self.lw1.takeItem(self.lw1.row(item))
                self.lw2.addItem(item.text())
                self.cal_points1(item)
           else:
                 store="Only three batsman can be present"
                 sample.MainWindow(store) 
        if date[0]=="Ball":
           print(int(self.l2.text()))
           self.d=int(self.l2.text())
           if self.d<3:
                self.d+=1
                self.l2.setText(str(self.d))
                self.lw1.takeItem(self.lw1.row(item))
                self.lw2.addItem(item.text())
                self.cal_points1(item)
           else:
                 store="Only three bowlers can be present"
                 sample.MainWindow(store) 

        if date[0]=="AR":
          print(int(self.l4.text()))
          self.d=int(self.l4.text())
          if self.d<2:
                self.d+=1
                self.l4.setText(str(self.d))
                self.lw1.takeItem(self.lw1.row(item))
                self.lw2.addItem(item.text())
                self.cal_points1(item)

          else:
                 store="Only two all rounder can be present"
                 sample.MainWindow(store) 

        if date[0]=="WK":
         print(int(self.l3.text()))
         self.d=int(self.l3.text())
         if self.d==0:
                self.d+=1
                self.l3.setText(str(self.d))
                self.lw1.takeItem(self.lw1.row(item))
                self.lw2.addItem(item.text())
                self.cal_points1(item)

         else:
                 store="Only one wcket keeper can be present"
                 sample.MainWindow(store)
    def choose(self):
         store="Now Choose your team"
         sample.MainWindow(store)


    def menufunction(self,action):
        txt=(action.text())
        if txt=="Evaluate Team":
               self.lw1.clear()
               self.lw2.clear()
               self.l5.setText(str(1000))
               self.l7.clear()
               self.l7.setReadOnly(True)
               self.l1.setText(str(0))
               self.l2.setText(str(0))
               self.l3.setText(str(0))
               self.l4.setText(str(0))
               self.l6.setText(str(0))
               self.rb1.setCheckable(False)
               self.rb2.setCheckable(False)
               self.rb3.setCheckable(False)
               self.rb4.setCheckable(False)
               self.lw2.setEnabled(True)
               record=side_sql.fetch_teamname()
               if record==[]:
                    store="Enter the Teams first."
                    sample.MainWindow(store)
               else:
                   self.Form = QtWidgets.QWidget()
                   self.ui = back.Ui_Form()
                   self.ui.setupUi(self.Form)
                   self.Form.show()

        if txt=="New Team":
            self.l7.clear()
            store="Enter the name of the team at team name line and choose your players:"
            self.lw2.setEnabled(True)
            sample.MainWindow(store)
            self.l7.setReadOnly(False)
            self.rb1.setCheckable(True)
            self.rb2.setCheckable(True)
            self.rb3.setCheckable(True)
            self.rb4.setCheckable(True)
            self.lw2.clear()
            self.lw1.clear()
            
        if txt=="Save Team":
            record=side_sql.fetch_teamname()
            self.lw2.setEnabled(True)
            print(record)
            for i in range(len(record)):
                if self.l7.text().strip()==record[i][0]:
                    store="Team Already Exist."
                    sample.MainWindow(store)
                    self.lw1.clear()
                    self.lw2.clear()
                    self.l5.setText(str(1000))
                    self.l7.clear()
                    self.l7.setReadOnly(True)
                    self.l1.setText(str(0))
                    self.l2.setText(str(0))
                    self.l3.setText(str(0))
                    self.l4.setText(str(0))
                    self.l6.setText(str(0))
                    self.rb1.setCheckable(False)
                    self.rb2.setCheckable(False)
                    self.rb3.setCheckable(False)
                    self.rb4.setCheckable(False)
                    
            if self.l7.text().strip()=="":
                store="enter valid name."
                sample.MainWindow(store)
                self.lw1.clear()
                self.lw2.clear()
                self.l5.setText(str(1000))
                self.l7.clear()
                self.l7.setReadOnly(True)
                self.l1.setText(str(0))
                self.l2.setText(str(0))
                self.l3.setText(str(0))
                self.l4.setText(str(0))
                self.l6.setText(str(0))
                self.rb1.setCheckable(False)
                self.rb2.setCheckable(False)
                self.rb3.setCheckable(False)
                self.rb4.setCheckable(False)

            else:
                items=[]
                for index in range(self.lw2.count()):
                    items.append(self.lw2.item(index).text())
                side_sql.store_team(self.l7.text(),items)
                self.lw1.clear()
                self.lw2.clear()
                self.l5.setText(str(1000))
                self.l7.clear()
                self.l7.setReadOnly(True)
                self.l1.setText(str(0))
                self.l2.setText(str(0))
                self.l3.setText(str(0))
                self.l4.setText(str(0))
                self.l6.setText(str(0))
                self.rb1.setCheckable(False)
                self.rb2.setCheckable(False)
                self.rb3.setCheckable(False)
                self.rb4.setCheckable(False)

        if txt=="Open Team":
            self.lw2.clear()
            store="Enter Team name.And press Enter"
            sample.MainWindow(store)
            self.l7.setReadOnly(False)
            self.l7.returnPressed.connect(self.openning)
            
    def openning(self):
            record=side_sql.retrieve_team(self.l7.text())
            self.lw2.clear()
            self.lw1.clear()
            self.l5.setText(str(1000))
            self.l1.setText(str(0))
            self.l2.setText(str(0))
            self.l3.setText(str(0))
            self.l4.setText(str(0))
            self.l6.setText(str(0))
            self.rb1.setCheckable(False)
            self.rb2.setCheckable(False)
            self.rb3.setCheckable(False)
            self.rb4.setCheckable(False)
            if record==[]:
                store="Team doesnot exist."
                sample.MainWindow(store)
            else:
                for i in range(len(record)):
                    self.lw2.addItem(record[i][0])
                store="You cant change the team,so dont click on players,if you did you will crash."
                self.l7.setReadOnly(True)
                self.lw2.setEnabled(False)

    def cal_points(self,item):
        val=side_sql.fetch_value(item.text())
        print(val)
        self.v=int(self.l5.text())
        self.v+=val[0]
        self.v1=int(self.l6.text())
        self.v1-=val[0]
        self.l6.setText(str(self.v1))
        self.l5.setText(str(self.v))

    def removelist2(self,item):
        date=side_sql.fetch_roll(item.text())
        val=side_sql.fetch_value(item.text())
        if date[0]=="Bat":
           print(int(self.l1.text()))
           self.d=int(self.l1.text())
           self.d-=1
           self.l1.setText(str(self.d))
           self.lw2.takeItem(self.lw2.row(item))
           self.lw1.addItem(item.text())
           self.cal_points(item)
           
        if date[0]=="Ball":
               print(int(self.l2.text()))
               self.d=int(self.l2.text())
               self.d-=1
               self.l2.setText(str(self.d))
               self.lw2.takeItem(self.lw2.row(item))
               self.lw1.addItem(item.text())
               self.cal_points(item)
    

        if date[0]=="AR":
              print(int(self.l4.text()))
              self.d=int(self.l4.text())
              self.d-=1
              self.l4.setText(str(self.d))
              self.lw2.takeItem(self.lw2.row(item))
              self.lw1.addItem(item.text())
              self.cal_points(item)

          
        if date[0]=="WK":
              self.d=int(self.l3.text())
              self.d-=1
              self.l3.setText(str(self.d))
              self.lw2.takeItem(self.lw2.row(item))
              self.lw1.addItem(item.text())
              self.cal_points(item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Yours Selection"))
        self.label_2.setText(_translate("MainWindow", "Batsman"))
        self.l1.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Bowler"))
        self.l2.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Wicket keeper"))
        self.l3.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "All Rounder"))
        self.l4.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "Points Available"))
        self.l5.setText(_translate("MainWindow", "1000"))
        self.l5.setPlaceholderText(_translate("MainWindow", "1000"))
        self.label_7.setText(_translate("MainWindow", "Points Used"))
        self.l6.setText(_translate("MainWindow", "0"))
        self.rb1.setText(_translate("MainWindow", "Bats"))
        self.rb2.setText(_translate("MainWindow", "Ball"))
        self.rb3.setText(_translate("MainWindow", "all"))
        self.rb4.setText(_translate("MainWindow", "Wk"))
        self.label_8.setText(_translate("MainWindow", "Team Name:"))
        self.menuManage.setTitle(_translate("MainWindow", "Manage"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpeb_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

