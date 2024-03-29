# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'capturarObservaciones.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import vistas.images

class Ui_capturarObservaciones(object):
    def setupUi(self, capturarObservaciones):
        capturarObservaciones.setObjectName("capturarObservaciones")
        capturarObservaciones.resize(477, 626)
        self.frame = QtWidgets.QFrame(capturarObservaciones)
        self.frame.setGeometry(QtCore.QRect(0, 0, 531, 61))
        self.frame.setStyleSheet("background-color: rgb(200, 198, 223);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(410, 10, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("image: url(:/newPrefix/archivo.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_2 = QtWidgets.QLabel(capturarObservaciones)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"font: 75 19pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.frame_4 = QtWidgets.QFrame(capturarObservaciones)
        self.frame_4.setGeometry(QtCore.QRect(0, 60, 531, 10))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 10))
        self.frame_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_24 = QtWidgets.QLabel(capturarObservaciones)
        self.label_24.setGeometry(QtCore.QRect(0, 70, 480, 591))
        self.label_24.setMinimumSize(QtCore.QSize(480, 60))
        self.label_24.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(210, 220, 220), stop:1 rgba(100, 130, 190));\n"
"\n"
"")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.teObservaciones = QtWidgets.QTextEdit(capturarObservaciones)
        self.teObservaciones.setGeometry(QtCore.QRect(20, 400, 431, 151))
        self.teObservaciones.setObjectName("teObservaciones")
        self.label_3 = QtWidgets.QLabel(capturarObservaciones)
        self.label_3.setGeometry(QtCore.QRect(0, 360, 461, 31))
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(capturarObservaciones)
        self.pushButton.setGeometry(QtCore.QRect(230, 570, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(capturarObservaciones)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 570, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(capturarObservaciones)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 121, 31))
        self.label_4.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(capturarObservaciones)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 161, 31))
        self.label_5.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(capturarObservaciones)
        self.label_6.setGeometry(QtCore.QRect(20, 280, 241, 31))
        self.label_6.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(capturarObservaciones)
        self.label_7.setGeometry(QtCore.QRect(20, 320, 311, 31))
        self.label_7.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(capturarObservaciones)
        self.label_8.setGeometry(QtCore.QRect(0, 80, 461, 31))
        self.label_8.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.lbPuntos = QtWidgets.QLabel(capturarObservaciones)
        self.lbPuntos.setGeometry(QtCore.QRect(140, 200, 121, 31))
        self.lbPuntos.setStyleSheet("\n"
"font: 87 8pt \"Arial Black\";")
        self.lbPuntos.setObjectName("lbPuntos")
        self.lbPromedioPotencias = QtWidgets.QLabel(capturarObservaciones)
        self.lbPromedioPotencias.setGeometry(QtCore.QRect(180, 240, 121, 31))
        self.lbPromedioPotencias.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.lbPromedioPotencias.setObjectName("lbPromedioPotencias")
        self.lbNumUmbral = QtWidgets.QLabel(capturarObservaciones)
        self.lbNumUmbral.setGeometry(QtCore.QRect(260, 280, 121, 31))
        self.lbNumUmbral.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.lbNumUmbral.setObjectName("lbNumUmbral")
        self.lbTiempoUmbralObtenido = QtWidgets.QLabel(capturarObservaciones)
        self.lbTiempoUmbralObtenido.setGeometry(QtCore.QRect(330, 320, 121, 31))
        self.lbTiempoUmbralObtenido.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.lbTiempoUmbralObtenido.setObjectName("lbTiempoUmbralObtenido")
        self.label_13 = QtWidgets.QLabel(capturarObservaciones)
        self.label_13.setGeometry(QtCore.QRect(20, 160, 151, 31))
        self.label_13.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.lbDuracioSesion = QtWidgets.QLabel(capturarObservaciones)
        self.lbDuracioSesion.setGeometry(QtCore.QRect(170, 160, 121, 31))
        self.lbDuracioSesion.setStyleSheet("font: 87 8pt \"Arial Black\";")
        self.lbDuracioSesion.setObjectName("lbDuracioSesion")

        self.retranslateUi(capturarObservaciones)
        QtCore.QMetaObject.connectSlotsByName(capturarObservaciones)

    def retranslateUi(self, capturarObservaciones):
        _translate = QtCore.QCoreApplication.translate
        capturarObservaciones.setWindowTitle(_translate("capturarObservaciones", "Dialog"))
        self.label_2.setText(_translate("capturarObservaciones", "Capturar Observaciones"))
        self.label_3.setText(_translate("capturarObservaciones", "Observaciones"))
        self.pushButton.setText(_translate("capturarObservaciones", "Cancelar"))
        self.pushButton_2.setText(_translate("capturarObservaciones", "Capturar"))
        self.label_4.setText(_translate("capturarObservaciones", "Puntos obtenidos:"))
        self.label_5.setText(_translate("capturarObservaciones", "Promedio de potencias:"))
        self.label_6.setText(_translate("capturarObservaciones", "Num. Veces que alcanzo el umbral:"))
        self.label_7.setText(_translate("capturarObservaciones", "Porcentaje de tiempo que mantuvo el umbral:"))
        self.label_8.setText(_translate("capturarObservaciones", "Datos de la sesión"))
        self.lbPuntos.setText(_translate("capturarObservaciones", "7"))
        self.lbPromedioPotencias.setText(_translate("capturarObservaciones", "23.876"))
        self.lbNumUmbral.setText(_translate("capturarObservaciones", "35"))
        self.lbTiempoUmbralObtenido.setText(_translate("capturarObservaciones", "3 Minutos"))
        self.label_13.setText(_translate("capturarObservaciones", "Duración de la terapia:"))
        self.lbDuracioSesion.setText(_translate("capturarObservaciones", "20 Minutos"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    capturarObservaciones = QtWidgets.QDialog()
    ui = Ui_capturarObservaciones()
    ui.setupUi(capturarObservaciones)
    capturarObservaciones.show()
    sys.exit(app.exec_())

