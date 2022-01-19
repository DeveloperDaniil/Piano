import sys

import pyglet as pyglet
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QMainWindow, QApplication


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(910, 720)
        self.pushButtonDo = QtWidgets.QPushButton(Dialog)
        self.pushButtonDo.setGeometry(QtCore.QRect(0, 0, 130, 720))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonDo.setFont(font)
        self.pushButtonDo.setObjectName("pushButtonDo")
        self.pushButtonRe = QtWidgets.QPushButton(Dialog)
        self.pushButtonRe.setGeometry(QtCore.QRect(130, 0, 130, 720))
        self.pushButtonRe.setFont(font)
        self.pushButtonRe.setObjectName("pushButtonRe")
        self.pushButtonMi = QtWidgets.QPushButton(Dialog)
        self.pushButtonMi.setGeometry(QtCore.QRect(260, 0, 130, 720))
        self.pushButtonMi.setFont(font)
        self.pushButtonMi.setObjectName("pushButtonMi")
        self.pushButtonFa = QtWidgets.QPushButton(Dialog)
        self.pushButtonFa.setGeometry(QtCore.QRect(390, 0, 130, 720))
        self.pushButtonFa.setFont(font)
        self.pushButtonFa.setObjectName("pushButtonFa")
        self.pushButtonSoli = QtWidgets.QPushButton(Dialog)
        self.pushButtonSoli.setGeometry(QtCore.QRect(520, 0, 130, 720))
        self.pushButtonSoli.setFont(font)
        self.pushButtonSoli.setObjectName("pushButtonSoli")
        self.pushButtonLya = QtWidgets.QPushButton(Dialog)
        self.pushButtonLya.setGeometry(QtCore.QRect(650, 0, 130, 720))
        self.pushButtonLya.setFont(font)
        self.pushButtonLya.setObjectName("pushButtonLya")
        self.pushButtonSi = QtWidgets.QPushButton(Dialog)
        self.pushButtonSi.setGeometry(QtCore.QRect(780, 0, 130, 720))
        self.pushButtonSi.setFont(font)
        self.pushButtonSi.setObjectName("pushButtonSi")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonDo.setText(_translate("Dialog", "[Z]"))
        self.pushButtonRe.setText(_translate("Dialog", "[X]"))
        self.pushButtonMi.setText(_translate("Dialog", "[C]"))
        self.pushButtonFa.setText(_translate("Dialog", "[V]"))
        self.pushButtonSoli.setText(_translate("Dialog", "[B]"))
        self.pushButtonLya.setText(_translate("Dialog", "[N]"))
        self.pushButtonSi.setText(_translate("Dialog", "[M]"))


class Example(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.player = QtMultimedia.QMediaPlayer()
        self.setupUi(self)
        self.logic()

    def logic(self):
        self.pushButtonDo.clicked.connect(self.play)
        self.pushButtonRe.clicked.connect(self.play)
        self.pushButtonMi.clicked.connect(self.play)
        self.pushButtonFa.clicked.connect(self.play)
        self.pushButtonSoli.clicked.connect(self.play)
        self.pushButtonLya.clicked.connect(self.play)
        self.pushButtonSi.clicked.connect(self.play)

    def play(self):
        btn = self.sender().text()
        if btn == "[Z]":
            song = pyglet.media.load('Notes/nota-do.mp3')
        elif btn == "[X]":
            song = pyglet.media.load('Notes/nota-re.mp3')
        elif btn == "[C]":
            song = pyglet.media.load('Notes/nota-mi.mp3')
        elif btn == "[V]":
            song = pyglet.media.load('Notes/nota-fa.mp3')
        elif btn == "[B]":
            song = pyglet.media.load('Notes/nota-soli.mp3')
        elif btn == "[N]":
            song = pyglet.media.load('Notes/nota-lya.mp3')
        elif btn == "[M]":
            song = pyglet.media.load('Notes/nota-si.mp3')
        else:
            return
        song.play()

    def keyPressEvent(self, event):
        if (event.key() == 90) or (event.key() == 1071):
            song = pyglet.media.load('Notes/nota-do.mp3')
        elif (event.key() == 88) or (event.key() == 1063):
            song = pyglet.media.load('Notes/nota-re.mp3')
        elif (event.key() == 67) or (event.key() == 1057):
            song = pyglet.media.load('Notes/nota-mi.mp3')
        elif (event.key() == 86) or (event.key() == 1052):
            song = pyglet.media.load('Notes/nota-fa.mp3')
        elif (event.key() == 66) or (event.key() == 1048):
            song = pyglet.media.load('Notes/nota-soli.mp3')
        elif (event.key() == 78) or (event.key() == 1058):
            song = pyglet.media.load('Notes/nota-lya.mp3')
        elif (event.key() == 77) or (event.key() == 1068):
            song = pyglet.media.load('Notes/nota-si.mp3')
        else:
            return
        song.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
