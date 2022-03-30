# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recuperarTerapeutas.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import vistas.images

class Ui_RecuperarTerapeutas(object):
    def setupUi(self, RecuperarTerapeutas):
        RecuperarTerapeutas.setObjectName("RecuperarTerapeutas")
        RecuperarTerapeutas.resize(639, 618)
        RecuperarTerapeutas.setMinimumSize(QtCore.QSize(639, 618))
        self.label = QtWidgets.QLabel(RecuperarTerapeutas)
        self.label.setGeometry(QtCore.QRect(0, 80, 641, 541))
        self.label.setMinimumSize(QtCore.QSize(10, 10))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(210, 220, 220), stop:1 rgba(100, 130, 190));\n"
"\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(RecuperarTerapeutas)
        self.frame.setGeometry(QtCore.QRect(0, 0, 641, 81))
        self.frame.setStyleSheet("background-color: rgb(200, 198, 223);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"font: 75 19pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(560, 0, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("image: url(:/newPrefix/terapeuta.png);")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.frame_2 = QtWidgets.QFrame(RecuperarTerapeutas)
        self.frame_2.setGeometry(QtCore.QRect(0, 80, 651, 14))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 14))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tvRecuperarTerapeutas = QtWidgets.QTableWidget(RecuperarTerapeutas)
        self.tvRecuperarTerapeutas.setGeometry(QtCore.QRect(20, 200, 611, 401))
        self.tvRecuperarTerapeutas.setMinimumSize(QtCore.QSize(200, 200))
        self.tvRecuperarTerapeutas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tvRecuperarTerapeutas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tvRecuperarTerapeutas.setDragEnabled(False)
        self.tvRecuperarTerapeutas.setRowCount(0)
        self.tvRecuperarTerapeutas.setColumnCount(6)
        self.tvRecuperarTerapeutas.setObjectName("tvRecuperarTerapeutas")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tvRecuperarTerapeutas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tvRecuperarTerapeutas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 255, 127))
        self.tvRecuperarTerapeutas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 248, 53))
        self.tvRecuperarTerapeutas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 170, 127))
        self.tvRecuperarTerapeutas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tvRecuperarTerapeutas.setHorizontalHeaderItem(5, item)
        self.cbfiltrar = QtWidgets.QComboBox(RecuperarTerapeutas)
        self.cbfiltrar.setGeometry(QtCore.QRect(20, 160, 131, 31))
        self.cbfiltrar.setObjectName("cbfiltrar")
        self.cbfiltrar.addItem("")
        self.cbfiltrar.addItem("")
        self.cbfiltrar.addItem("")
        self.btnBuscarTerapeutas = QtWidgets.QPushButton(RecuperarTerapeutas)
        self.btnBuscarTerapeutas.setGeometry(QtCore.QRect(160, 160, 31, 31))
        self.btnBuscarTerapeutas.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscarTerapeutas.setIcon(icon)
        self.btnBuscarTerapeutas.setObjectName("btnBuscarTerapeutas")
        self.label_2 = QtWidgets.QLabel(RecuperarTerapeutas)
        self.label_2.setGeometry(QtCore.QRect(20, 137, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnRecuperarTerapeuta = QtWidgets.QPushButton(RecuperarTerapeutas)
        self.btnRecuperarTerapeuta.setGeometry(QtCore.QRect(350, 160, 171, 28))
        self.btnRecuperarTerapeuta.setObjectName("btnRecuperarTerapeuta")
        self.btnRefrescar = QtWidgets.QPushButton(RecuperarTerapeutas)
        self.btnRefrescar.setGeometry(QtCore.QRect(530, 160, 101, 28))
        self.btnRefrescar.setObjectName("btnRefrescar")

        self.retranslateUi(RecuperarTerapeutas)
        QtCore.QMetaObject.connectSlotsByName(RecuperarTerapeutas)

    def retranslateUi(self, RecuperarTerapeutas):
        _translate = QtCore.QCoreApplication.translate
        RecuperarTerapeutas.setWindowTitle(_translate("RecuperarTerapeutas", "Dialog"))
        self.label_3.setText(_translate("RecuperarTerapeutas", "Recuperar terapeutas eliminados"))
        item = self.tvRecuperarTerapeutas.horizontalHeaderItem(0)
        item.setText(_translate("RecuperarTerapeutas", "IdTerapeuta"))
        item = self.tvRecuperarTerapeutas.horizontalHeaderItem(1)
        item.setText(_translate("RecuperarTerapeutas", "Usuario"))
        item = self.tvRecuperarTerapeutas.horizontalHeaderItem(2)
        item.setText(_translate("RecuperarTerapeutas", "Nombre"))
        item = self.tvRecuperarTerapeutas.horizontalHeaderItem(3)
        item.setText(_translate("RecuperarTerapeutas", "Paterno"))
        item = self.tvRecuperarTerapeutas.horizontalHeaderItem(4)
        item.setText(_translate("RecuperarTerapeutas", "Materno"))
        item = self.tvRecuperarTerapeutas.horizontalHeaderItem(5)
        item.setText(_translate("RecuperarTerapeutas", "Tipo"))
        self.cbfiltrar.setItemText(0, _translate("RecuperarTerapeutas", "Todos"))
        self.cbfiltrar.setItemText(1, _translate("RecuperarTerapeutas", "Administrador"))
        self.cbfiltrar.setItemText(2, _translate("RecuperarTerapeutas", "Normal"))
        self.label_2.setText(_translate("RecuperarTerapeutas", "Buscar terapeuta: "))
        self.btnRecuperarTerapeuta.setText(_translate("RecuperarTerapeutas", "Recuperar terapeuta"))
        self.btnRefrescar.setText(_translate("RecuperarTerapeutas", "Refrescar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RecuperarTerapeutas = QtWidgets.QDialog()
    ui = Ui_RecuperarTerapeutas()
    ui.setupUi(RecuperarTerapeutas)
    RecuperarTerapeutas.show()
    sys.exit(app.exec_())
