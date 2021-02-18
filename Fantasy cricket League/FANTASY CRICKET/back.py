# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'back.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import side_sql
import sqlite3
import sample
import random as rd
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(606, 520)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cb1 = QtWidgets.QComboBox(Form)
        self.cb1.setObjectName("cb1")
        self.horizontalLayout.addWidget(self.cb1)
        self.cb2 = QtWidgets.QComboBox(Form)
        self.cb2.setObjectName("cb2")
        self.horizontalLayout.addWidget(self.cb2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lw1 = QtWidgets.QListWidget(Form)
        self.lw1.setObjectName("lw1")
        self.horizontalLayout_2.addWidget(self.lw1)
        self.lw2 = QtWidgets.QListWidget(Form)
        self.lw2.setObjectName("lw2")
        self.horizontalLayout_2.addWidget(self.lw2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.b1 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.verticalLayout_2.addWidget(self.b1)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        record=side_sql.fetch_teamname()
        for i in range(len(record)):
            self.cb1.addItem(record[i][0])
        self.cb2.addItem("Match 1")
        self.cb2.addItem("Match 2")
        self.cb2.addItem("Match 3")
        self.b1.clicked.connect(self.create_table)
       
    def create_table(self):
        self.demo=sqlite3.connect("fantasy_cricket.db")
        self.uemo=self.demo.cursor()
        self.name=self.cb1.currentText()+"_"+self.cb2.currentText()
        self.uemo.execute("drop table if exists '"+self.name+"';")
        self.uemo.execute("create table if not exists '"+self.name+"'(player text,scored integer,faced integer,fours integer,sixes integer,bowled integer,maiden integer,given integer,wkts integer,catches integer,stumping integer,RO integer);")
        self.demo.commit()
        self.insert_value()

    def insert_value(self):
        record=side_sql.retrieve_team(self.cb1.currentText())
        self.name=self.cb1.currentText()+"_"+self.cb2.currentText()
        self.lw1.clear()
        for i in range(len(record)):
            self.demo=sqlite3.connect("fantasy_cricket.db")
            self.lw1.addItem(record[i][0])
            self.uemo=self.demo.cursor()
            self.player=str(record[i][0])
            self.scored=rd.randint(0,200)
            self.faced=rd.randint(1,120)
            self.fours=rd.randint(0,50)
            self.sixes=rd.randint(0,50)
            self.bowled=rd.randint(0,9)
            self.maiden=rd.randint(0,10)
            self.given=rd.randint(0,50)
            self.wkts=rd.randint(0,9)
            self.catches=rd.randint(0,9)
            self.stumping=rd.randint(0,9)
            self.RO=rd.randint(0,9)
            self.uemo.execute("insert into '"+self.name+"' values(?,?,?,?,?,?,?,?,?,?,?,?);",(self.player,self.scored,self.faced,self.fours,self.sixes,self.bowled,self.maiden,self.given,self.wkts,self.catches,self.stumping,self.RO))
            self.demo.commit()
        self.calculate_points()

    def calculate_points(self):
        record=side_sql.retrieve_team(self.cb1.currentText())
        self.name=self.cb1.currentText()+"_"+self.cb2.currentText()
        self.lw2.clear()
        for i in range(len(record)):
            self.roll=side_sql.fetch_roll(str(record[i][0]))
            self.demo=sqlite3.connect("fantasy_cricket.db")
            self.uemo=self.demo.cursor()
            if self.roll[0]=="Bat":
                self.uemo.execute("select scored, faced,fours,sixes,catches,stumping,RO from '"+self.name+"'where player=?;",(record[i][0],))
                answer=self.uemo.fetchall()
                run=int(answer[0][0])
                balls=int(answer[0][1])
                fours=int(answer[0][2])
                six=int(answer[0][3])
                fields=int(answer[0][4])+int(answer[0][5])+int(answer[0][6])
                points=run//2
                if run>50:
                            points+=5
                else:
                            pass
                if run>100:
                            points+=10
                else:
                            pass
                if 0.8<(run/balls)<1:
                            points+=2
                elif (run/balls)>=1:
                            points+=4
                points=points+(fours*1)+(six*2)+(fields*10)
                self.lw2.addItem(str(points))

            elif self.roll[0]=="Ball":
                self.uemo.execute("select bowled,given,wkts,catches,stumping,RO from '"+self.name+"' where player=?;",(record[i][0],))
                answer=self.uemo.fetchall()
                wkts=int(answer[0][2])+int(answer[0][0])
                fields=int(answer[0][3])+int(answer[0][4])+int(answer[0][5])
                runs=int(answer[0][1])
                overs=rd.randint(6,20)
                points=wkts*10
                if wkts==3:
                            points+=5
                else:
                            pass
                if wkts>=5:
                            points+=10
                else:
                            pass
                if 3.5<(runs/overs)<=4.5:
                            points+=4
                elif 2<=(runs/overs)<=3.5:
                            points+=7
                elif (runs/overs)<2:
                            points=+10
                points=points+(fields*10)
                self.lw2.addItem(str(points))

            else:
                self.uemo.execute("select bowled,given,wkts,catches,stumping,RO,scored, faced,fours,sixes from '"+self.name+"' where player=?;",(record[i][0],))
                answer=self.uemo.fetchall()
                wkts=int(answer[0][2])+int(answer[0][0])
                fields=int(answer[0][3])+int(answer[0][4])+int(answer[0][5])
                runs=int(answer[0][1])
                overs=rd.randint(6,20)
                points=wkts*10
                if wkts==3:
                            points+=5
                else:
                            pass
                if wkts>=5:
                            points+=10
                else:
                            pass
                if 3.5<(runs/overs)<=4.5:
                            points+=4
                elif 2<=(runs/overs)<=3.5:
                            points+=7
                elif (runs/overs)<2:
                            points=+10
                points=points+(fields*10)
                run=int(answer[0][6])
                balls=int(answer[0][7])
                fours=int(answer[0][8])
                six=int(answer[0][9])
                point=run//2
                if run>50:
                            point+=5
                else:
                            pass
                if run>100:
                            point+=10
                else:
                            pass
                if 0.8<(run/balls)<1:
                            point+=2
                elif (run/balls)>=1:
                            point+=4
                total=points+point
                self.lw2.addItem(str(points))
        self.demo.close()
        self.terminate()

    def terminate(self):
        value=0
        self.name=self.cb1.currentText()+"_"+self.cb2.currentText()
        for i in range(self.lw2.count()):
            value=value+int(self.lw2.item(i).text())
        store="The total scored is %d"%value
        sample.MainWindow(store)

               
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Evaluate the performace of your team"))
        self.label_2.setText(_translate("Form", "Players"))
        self.label_3.setText(_translate("Form", "Points"))
        self.b1.setText(_translate("Form", "CHECK TOTAL POINTS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

