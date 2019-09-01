# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os


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
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(32, 74, 135);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 190, 291, 131))
        font = QtGui.QFont()
        font.setPointSize(90)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 340, 89, 25))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(32, 74, 135);\n"
"background-color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 550, 141, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuHow_it_work = QtGui.QMenu(self.menuHelp)
        self.menuHow_it_work.setObjectName(_fromUtf8("menuHow_it_work"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuAbout_us = QtGui.QMenu(self.menuAbout)
        self.menuAbout_us.setObjectName(_fromUtf8("menuAbout_us"))
        MainWindow.setMenuBar(self.menubar)
        self.actionUse_socket_for_P2P_apps = QtGui.QAction(MainWindow)
        self.actionUse_socket_for_P2P_apps.setObjectName(_fromUtf8("actionUse_socket_for_P2P_apps"))
        self.actionUse_Socket_server = QtGui.QAction(MainWindow)
        self.actionUse_Socket_server.setObjectName(_fromUtf8("actionUse_Socket_server"))
        self.actionUse_Firefox_proxy = QtGui.QAction(MainWindow)
        self.actionUse_Firefox_proxy.setObjectName(_fromUtf8("actionUse_Firefox_proxy"))
        self.actionUse_it_to_Apps = QtGui.QAction(MainWindow)
        self.actionUse_it_to_Apps.setObjectName(_fromUtf8("actionUse_it_to_Apps"))
        self.actioniVPN_created_by_razyar_saeedian_and_mohammad_goli_and_iSpace_corpration_Licence_Phantom_OWNF = QtGui.QAction(MainWindow)
        self.actioniVPN_created_by_razyar_saeedian_and_mohammad_goli_and_iSpace_corpration_Licence_Phantom_OWNF.setObjectName(_fromUtf8("actioniVPN_created_by_razyar_saeedian_and_mohammad_goli_and_iSpace_corpration_Licence_Phantom_OWNF"))
        self.actionIf_you_want_tunnel_all_the_network_connection_you_have_to_click_on_Connect_button_on_Main_Screen_and_if_you_want_use_another_setting_and_options_go_to_Settings_Menu = QtGui.QAction(MainWindow)
        self.actionIf_you_want_tunnel_all_the_network_connection_you_have_to_click_on_Connect_button_on_Main_Screen_and_if_you_want_use_another_setting_and_options_go_to_Settings_Menu.setObjectName(_fromUtf8("actionIf_you_want_tunnel_all_the_network_connection_you_have_to_click_on_Connect_button_on_Main_Screen_and_if_you_want_use_another_setting_and_options_go_to_Settings_Menu"))
        self.menuSettings.addSeparator()
        self.menuSettings.addSeparator()
        self.menuSettings.addSeparator()
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionUse_socket_for_P2P_apps)
        self.menuSettings.addAction(self.actionUse_Socket_server)
        self.menuSettings.addAction(self.actionUse_Firefox_proxy)
        self.menuSettings.addAction(self.actionUse_it_to_Apps)
        self.menuHow_it_work.addAction(self.actionIf_you_want_tunnel_all_the_network_connection_you_have_to_click_on_Connect_button_on_Main_Screen_and_if_you_want_use_another_setting_and_options_go_to_Settings_Menu)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.menuHow_it_work.menuAction())
        self.menuAbout_us.addSeparator()
        self.menuAbout_us.addAction(self.actioniVPN_created_by_razyar_saeedian_and_mohammad_goli_and_iSpace_corpration_Licence_Phantom_OWNF)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.menuAbout_us.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), execute)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    global execute
    def execute():
	os.system('python execute.bin')




    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "iVPN", None))
        self.label.setText(_translate("MainWindow", "iVPN", None))
        self.pushButton.setText(_translate("MainWindow", "Connect", None))
        self.label_2.setText(_translate("MainWindow", "Github.com/razyar", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuHow_it_work.setTitle(_translate("MainWindow", "How it work?", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menuAbout_us.setTitle(_translate("MainWindow", "About us", None))
        self.actionUse_socket_for_P2P_apps.setText(_translate("MainWindow", "Use socket for P2P apps", None))
        self.actionUse_Socket_server.setText(_translate("MainWindow", "Use Socket server", None))
        self.actionUse_Firefox_proxy.setText(_translate("MainWindow", "Use Firefox proxy", None))
        self.actionUse_it_to_Apps.setText(_translate("MainWindow", "Use it to Apps", None))
        self.actioniVPN_created_by_razyar_saeedian_and_mohammad_goli_and_iSpace_corpration_Licence_Phantom_OWNF.setText(_translate("MainWindow", "iVPN created by razyar saeedian and mohammad goli and iSpace corpration. Licence: Phantom OWNF", None))
        self.actionIf_you_want_tunnel_all_the_network_connection_you_have_to_click_on_Connect_button_on_Main_Screen_and_if_you_want_use_another_setting_and_options_go_to_Settings_Menu.setText(_translate("MainWindow", "If you want tunnel all the network connection, you have to click on Connect button on Main Screen. and if you want use another setting and options go to Settings  Menu.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

