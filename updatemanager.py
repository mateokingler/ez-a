# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update-manager.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QFileDialog,
    QTextEdit,
    QPushButton,
    QLabel,
    QVBoxLayout,
)

import webbrowser
import requests
import win32api
import threading

VERSION = "1.0"


class Ui_Form(object):
    def check_updates(self):
        self.update_button.setEnabled(False)
        self.update_button.setText("No Update Available")
        QApplication.processEvents()
        try:
            response = requests.get(
                "https://github.com/mateokingler/ez-a/raw/main/releases/version.txt"
            )
            data = response.text

            if float(data) > float(VERSION):
                self.update_notifier.setText(
                    "There is a new version of EZ-A available! " + "Version: " + data
                )
                self.update_button.setText("Update Now")
                self.update_button.setEnabled(True)
                QApplication.processEvents()
            else:
                self.update_notifier.setText(
                    "Congrats! You have the latest version of EZ-A! "
                    + "Version: "
                    + VERSION
                )
                self.update_button.setText("No Update Available")
                self.update_button.setEnabled(False)
                QApplication.processEvents()
        except Exception as e:
            self.update_notifier.setText("Error downloading latest update")
            QApplication.processEvents()

    def download_update(self):
        webbrowser.open_new_tab(
            "https://github.com/mateokingler/ez-a/raw/main/releases/EZ-A.zip"
        )

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 200)
        Form.setMinimumSize(QtCore.QSize(500, 200))
        Form.setMaximumSize(QtCore.QSize(500, 200))
        Form.setStyleSheet("QtWidget {\n" "    background-color: #081e3f ;\n" "}")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 510, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setStyleSheet("QFrame {\n" "    background-color: #081e3f ;\n" "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.update_notifier = QtWidgets.QLabel(self.frame)
        self.update_notifier.setGeometry(QtCore.QRect(0, 30, 500, 40))
        self.update_notifier.setMinimumSize(QtCore.QSize(500, 40))
        self.update_notifier.setMaximumSize(QtCore.QSize(500, 40))
        self.update_notifier.setStyleSheet(
            "QLabel\n"
            "{\n"
            "    font-family: Verdana;\n"
            "    font-size: 15px;\n"
            "    color: white;\n"
            "    font-weight: bold;\n"
            "}"
        )
        self.update_notifier.setAlignment(QtCore.Qt.AlignCenter)
        self.update_notifier.setObjectName("update_notifier")
        self.update_button = QtWidgets.QPushButton(self.frame)
        self.update_button.setGeometry(QtCore.QRect(160, 110, 170, 35))
        self.update_button.setMinimumSize(QtCore.QSize(170, 35))
        self.update_button.setMaximumSize(QtCore.QSize(170, 35))
        self.update_button.setStyleSheet(
            "QPushButton\n"
            "{    \n"
            "    margin-top: 4px;\n"
            "    margin-left: 3px;\n"
            "    background-color: #f8c93e;\n"
            "    color: #081e3f;\n"
            "    border: none;\n"
            "    padding-bottom: 1px;\n"
            "    font-size: 17px;\n"
            "}\n"
            "QPushButton:hover\n"
            "{\n"
            "    font-weight: 500;\n"
            "    font-size: 17px;\n"
            "    padding-bottom: 1px;\n"
            "}"
        )
        self.update_button.setObjectName("update_button")
        self.update_button.clicked.connect(self.download_update)
        self.verticalLayout.addWidget(self.frame)

        self.check_updates()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "EZ-A Update Manager"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
