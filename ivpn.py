'''
@author: razyar
@label: OpenKeyboard
'''


import os
import sys


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(524, 447)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(524, 447))
        MainWindow.setMaximumSize(QtCore.QSize(524, 447))
        MainWindow.setBaseSize(QtCore.QSize(281, 328))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../MigMig/bg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(25, 25, 25);\n"
"selection-color: rgb(36, 36, 36);\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 140, 21, 71))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 420, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 220, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(_fromUtf8("\n"
"selection-background-color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 260, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(_fromUtf8("selection-background-color: rgb(255, 255, 255);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 140, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 150, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 390, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 524, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuUpdate = QtGui.QMenu(self.menuBar)
        self.menuUpdate.setObjectName(_fromUtf8("menuUpdate"))
        self.menuOptions = QtGui.QMenu(self.menuUpdate)
        self.menuOptions.setAutoFillBackground(False)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionCheck_for_update_2 = QtGui.QAction(MainWindow)
        self.actionCheck_for_update_2.setObjectName(_fromUtf8("actionCheck_for_update_2"))
        self.actionRoll_back = QtGui.QAction(MainWindow)
        self.actionRoll_back.setObjectName(_fromUtf8("actionRoll_back"))
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionCheck_for_update_2)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionRoll_back)
        self.menuUpdate.addAction(self.menuOptions.menuAction())
        self.menuBar.addAction(self.menuUpdate.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), connect_pch3)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), connect_pch4)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.update)
        QtCore.QObject.connect(self.actionCheck_for_update_2, QtCore.SIGNAL(_fromUtf8("activated()")), check_update)
        QtCore.QObject.connect(self.actionRoll_back, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    global connect_pch3

    def connect_pch3():
    	os.system('proxychains firefox https://google.com')


    global connect_pch4

    def connect_pch4():
    	os.system('proxychains4 firefox https://google.com')

    global check_update
  
  	
    def check_update():
  		try:
  			os.system('git clone https://github.com/razyar/iVPN')
  			os.chdir('iVPN'); os.system('python require.py'); os.system('python update.py')
  			os.system('rm update.py'); sys.exit(0)
  		except Exception as UpdateError:
  			print 'Error while Updateing.'

		


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "iVPN ", None))
        self.label.setText(_translate("MainWindow", "i", None))
        self.label_2.setText(_translate("MainWindow", "Github.com/razyar", None))
        self.pushButton.setText(_translate("MainWindow", "Method 1", None))
        self.pushButton_2.setText(_translate("MainWindow", "Method 2", None))
        self.pushButton_3.setText(_translate("MainWindow", "?", None))
        self.label_3.setText(_translate("MainWindow", "VPN", None))
        self.label_4.setText(_translate("MainWindow", "Github.com/razyar", None))
        self.menuUpdate.setTitle(_translate("MainWindow", "Update", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.actionCheck_for_update_2.setText(_translate("MainWindow", "Check for update", None))
        self.actionRoll_back.setText(_translate("MainWindow", "Roll back", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

