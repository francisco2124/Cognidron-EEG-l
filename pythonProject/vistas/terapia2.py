# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'terapia2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import vistas.images

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 710)
        Dialog.setMinimumSize(QtCore.QSize(1000, 700))
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cbPaciente = QtWidgets.QComboBox(Dialog)
        self.cbPaciente.setGeometry(QtCore.QRect(90, 120, 151, 31))
        self.cbPaciente.setObjectName("cbPaciente")
        self.cbPaciente.addItem("")
        self.cbPaciente.addItem("")
        self.cbPaciente.addItem("")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(300, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cbRobot = QtWidgets.QComboBox(Dialog)
        self.cbRobot.setGeometry(QtCore.QRect(380, 120, 131, 31))
        self.cbRobot.setObjectName("cbRobot")
        self.cbRobot.addItem("")
        self.cbRobot.addItem("")
        self.cbRobot.addItem("")
        self.btnEnviarIstruccion = QtWidgets.QPushButton(Dialog)
        self.btnEnviarIstruccion.setGeometry(QtCore.QRect(40, 340, 161, 31))
        self.btnEnviarIstruccion.setObjectName("btnEnviarIstruccion")
        self.btnObtenerDrone = QtWidgets.QPushButton(Dialog)
        self.btnObtenerDrone.setGeometry(QtCore.QRect(40, 670, 161, 31))
        self.btnObtenerDrone.setStyleSheet("background-color: rgb(116, 147, 198);")
        self.btnObtenerDrone.setObjectName("btnObtenerDrone")
        self.btnDecenderDrone = QtWidgets.QPushButton(Dialog)
        self.btnDecenderDrone.setEnabled(False)
        self.btnDecenderDrone.setGeometry(QtCore.QRect(40, 510, 161, 28))
        self.btnDecenderDrone.setObjectName("btnDecenderDrone")
        self.btnIsquierdaDrone = QtWidgets.QPushButton(Dialog)
        self.btnIsquierdaDrone.setEnabled(False)
        self.btnIsquierdaDrone.setGeometry(QtCore.QRect(60, 590, 31, 31))
        self.btnIsquierdaDrone.setObjectName("btnIsquierdaDrone")
        self.btnAdelanteDrone = QtWidgets.QPushButton(Dialog)
        self.btnAdelanteDrone.setEnabled(False)
        self.btnAdelanteDrone.setGeometry(QtCore.QRect(100, 550, 31, 31))
        self.btnAdelanteDrone.setObjectName("btnAdelanteDrone")
        self.btnDerechaDrone = QtWidgets.QPushButton(Dialog)
        self.btnDerechaDrone.setEnabled(False)
        self.btnDerechaDrone.setGeometry(QtCore.QRect(140, 590, 31, 31))
        self.btnDerechaDrone.setObjectName("btnDerechaDrone")
        self.btnAtrasDrone = QtWidgets.QPushButton(Dialog)
        self.btnAtrasDrone.setEnabled(False)
        self.btnAtrasDrone.setGeometry(QtCore.QRect(100, 630, 31, 31))
        self.btnAtrasDrone.setObjectName("btnAtrasDrone")
        self.btnElevarDrone = QtWidgets.QPushButton(Dialog)
        self.btnElevarDrone.setEnabled(False)
        self.btnElevarDrone.setGeometry(QtCore.QRect(40, 470, 161, 31))
        self.btnElevarDrone.setObjectName("btnElevarDrone")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(550, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.cbTiempoSesion = QtWidgets.QComboBox(Dialog)
        self.cbTiempoSesion.setGeometry(QtCore.QRect(630, 120, 91, 31))
        self.cbTiempoSesion.setObjectName("cbTiempoSesion")
        self.cbTiempoSesion.addItem("")
        self.cbTiempoSesion.addItem("")
        self.cbTiempoSesion.addItem("")
        self.cbTiempoSesion.addItem("")
        self.cbTiempoSesion.addItem("")
        self.cbTiempoSesion.addItem("")
        self.cbTiempoSesion.addItem("")
        self.proBarTiempoSesion = QtWidgets.QProgressBar(Dialog)
        self.proBarTiempoSesion.setGeometry(QtCore.QRect(750, 160, 241, 23))
        self.proBarTiempoSesion.setProperty("value", 24)
        self.proBarTiempoSesion.setObjectName("proBarTiempoSesion")
        self.btnResumen = QtWidgets.QPushButton(Dialog)
        self.btnResumen.setGeometry(QtCore.QRect(830, 120, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnResumen.setFont(font)
        self.btnResumen.setObjectName("btnResumen")
        self.btnDetener = QtWidgets.QPushButton(Dialog)
        self.btnDetener.setGeometry(QtCore.QRect(910, 120, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnDetener.setFont(font)
        self.btnDetener.setObjectName("btnDetener")
        self.btnPausar = QtWidgets.QPushButton(Dialog)
        self.btnPausar.setGeometry(QtCore.QRect(870, 120, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnPausar.setFont(font)
        self.btnPausar.setObjectName("btnPausar")
        self.btbCapturarObservaciones = QtWidgets.QPushButton(Dialog)
        self.btbCapturarObservaciones.setGeometry(QtCore.QRect(40, 300, 161, 31))
        self.btbCapturarObservaciones.setObjectName("btbCapturarObservaciones")
        self.labelComandosMentales = QtWidgets.QLabel(Dialog)
        self.labelComandosMentales.setGeometry(QtCore.QRect(230, 670, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelComandosMentales.setFont(font)
        self.labelComandosMentales.setObjectName("labelComandosMentales")
        self.labelEventoDrone = QtWidgets.QLabel(Dialog)
        self.labelEventoDrone.setGeometry(QtCore.QRect(510, 670, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelEventoDrone.setFont(font)
        self.labelEventoDrone.setObjectName("labelEventoDrone")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(310, 500, 141, 101))
        self.label_11.setStyleSheet("image: url(:/newPrefix/EjerElevar.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(230, 220, 461, 431))
        self.label_12.setStyleSheet("background-color: rgb(162, 175, 188);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.progressBar_2 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(890, 680, 71, 20))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_3.setGeometry(QtCore.QRect(750, 680, 71, 20))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(720, 670, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(840, 380, 121, 81))
        self.groupBox.setObjectName("groupBox")
        self.rbInivitorio = QtWidgets.QRadioButton(self.groupBox)
        self.rbInivitorio.setGeometry(QtCore.QRect(10, 20, 95, 20))
        self.rbInivitorio.setObjectName("rbInivitorio")
        self.rdbExitatorio = QtWidgets.QRadioButton(self.groupBox)
        self.rdbExitatorio.setGeometry(QtCore.QRect(10, 60, 95, 20))
        self.rdbExitatorio.setChecked(True)
        self.rdbExitatorio.setObjectName("rdbExitatorio")
        self.cbBanda = QtWidgets.QComboBox(Dialog)
        self.cbBanda.setGeometry(QtCore.QRect(840, 490, 121, 21))
        self.cbBanda.setObjectName("cbBanda")
        self.cbBanda.addItem("")
        self.cbBanda.addItem("")
        self.cbBanda.addItem("")
        self.cbBanda.addItem("")
        self.cbBanda.addItem("")
        self.cbBanda.addItem("")
        self.btnElevarHumbral = QtWidgets.QPushButton(Dialog)
        self.btnElevarHumbral.setGeometry(QtCore.QRect(900, 520, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnElevarHumbral.setFont(font)
        self.btnElevarHumbral.setObjectName("btnElevarHumbral")
        self.btnBajarHumnbral = QtWidgets.QPushButton(Dialog)
        self.btnBajarHumnbral.setGeometry(QtCore.QRect(850, 520, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnBajarHumnbral.setFont(font)
        self.btnBajarHumnbral.setObjectName("btnBajarHumnbral")
        self.progressBar_4 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_4.setGeometry(QtCore.QRect(710, 250, 81, 400))
        self.progressBar_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_4.setStyleSheet("QProgressBar::chunk \"\n"
"                                            \"{\"\n"
"                                            \"background-color: orange;\"\n"
"                                            \"}\n"
"\n"
"")
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setTextVisible(True)
        self.progressBar_4.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_4.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_4.setObjectName("progressBar_4")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(560, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.cbPista = QtWidgets.QComboBox(Dialog)
        self.cbPista.setGeometry(QtCore.QRect(630, 160, 91, 31))
        self.cbPista.setObjectName("cbPista")
        self.cbPista.addItem("")
        self.cbPista.addItem("")
        self.cbPista.addItem("")
        self.cbPista.addItem("")
        self.cbPista.addItem("")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(850, 670, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label_17.setObjectName("label_17")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(840, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_14.setObjectName("label_14")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(840, 270, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(200, 198, 223);")
        self.label_18.setObjectName("label_18")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-20, 0, 1021, 81))
        self.frame.setStyleSheet("background-color: rgb(200, 198, 223);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 0, 501, 61))
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
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(910, 10, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("image: url(:/newPrefix/salud-mental.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(180, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(680, 50, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(0, 80, 1001, 10))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 10))
        self.frame_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 89, 1010, 621))
        self.label.setMinimumSize(QtCore.QSize(1010, 610))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(210, 220, 220), stop:1 rgba(100, 130, 190));\n"
"\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btnIniciarConfigurarConexion = QtWidgets.QPushButton(Dialog)
        self.btnIniciarConfigurarConexion.setGeometry(QtCore.QRect(40, 220, 161, 31))
        self.btnIniciarConfigurarConexion.setStyleSheet("background-color: rgb(112, 142, 191);")
        self.btnIniciarConfigurarConexion.setObjectName("btnIniciarConfigurarConexion")
        self.btnActivarDrone = QtWidgets.QPushButton(Dialog)
        self.btnActivarDrone.setGeometry(QtCore.QRect(40, 420, 161, 31))
        self.btnActivarDrone.setStyleSheet("background-color: rgb(116, 147, 198);")
        self.btnActivarDrone.setObjectName("btnActivarDrone")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(300, 160, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cbEjercicio = QtWidgets.QComboBox(Dialog)
        self.cbEjercicio.setGeometry(QtCore.QRect(380, 160, 131, 31))
        self.cbEjercicio.setObjectName("cbEjercicio")
        self.cbEjercicio.addItem("")
        self.cbEjercicio.addItem("")
        self.cbEjercicio.addItem("")
        self.btnAplicarBandas = QtWidgets.QPushButton(Dialog)
        self.btnAplicarBandas.setGeometry(QtCore.QRect(850, 600, 101, 31))
        self.btnAplicarBandas.setStyleSheet("background-color: rgb(182, 181, 203);")
        self.btnAplicarBandas.setObjectName("btnAplicarBandas")
        self.btnIniciarTerapia = QtWidgets.QPushButton(Dialog)
        self.btnIniciarTerapia.setEnabled(False)
        self.btnIniciarTerapia.setGeometry(QtCore.QRect(40, 260, 161, 31))
        self.btnIniciarTerapia.setStyleSheet("background-color: rgb(182, 181, 203);")
        self.btnIniciarTerapia.setObjectName("btnIniciarTerapia")
        self.btnActivarEmotiv = QtWidgets.QPushButton(Dialog)
        self.btnActivarEmotiv.setGeometry(QtCore.QRect(40, 380, 161, 31))
        self.btnActivarEmotiv.setStyleSheet("background-color: rgb(0, 226, 0);")
        self.btnActivarEmotiv.setObjectName("btnActivarEmotiv")
        self.btnAterrizarDrone = QtWidgets.QPushButton(Dialog)
        self.btnAterrizarDrone.setEnabled(False)
        self.btnAterrizarDrone.setGeometry(QtCore.QRect(100, 590, 31, 31))
        self.btnAterrizarDrone.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.btnAterrizarDrone.setObjectName("btnAterrizarDrone")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(50, 170, 231, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_9.setObjectName("label_9")
        self.lbMinutos = QtWidgets.QLabel(Dialog)
        self.lbMinutos.setGeometry(QtCore.QRect(750, 120, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbMinutos.setFont(font)
        self.lbMinutos.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(200, 198, 223);")
        self.lbMinutos.setObjectName("lbMinutos")
        self.lbUmbral = QtWidgets.QLabel(Dialog)
        self.lbUmbral.setGeometry(QtCore.QRect(780, 500, 51, 51))
        self.lbUmbral.setStyleSheet("image: url(:/newPrefix/lineaIzqu.png);")
        self.lbUmbral.setText("")
        self.lbUmbral.setObjectName("lbUmbral")
        self.edtUmbral = QtWidgets.QLineEdit(Dialog)
        self.edtUmbral.setGeometry(QtCore.QRect(860, 560, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edtUmbral.setFont(font)
        self.edtUmbral.setText("")
        self.edtUmbral.setMaxLength(27)
        self.edtUmbral.setAlignment(QtCore.Qt.AlignCenter)
        self.edtUmbral.setDragEnabled(True)
        self.edtUmbral.setObjectName("edtUmbral")
        self.lbValorUmbral = QtWidgets.QLabel(Dialog)
        self.lbValorUmbral.setGeometry(QtCore.QRect(910, 550, 21, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lbValorUmbral.setFont(font)
        self.lbValorUmbral.setStyleSheet("\n"
"font: 11pt \"MS Serif\";")
        self.lbValorUmbral.setObjectName("lbValorUmbral")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(930, 550, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(480, 580, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(480, 250, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label.raise_()
        self.frame.raise_()
        self.label_12.raise_()
        self.label_2.raise_()
        self.cbPaciente.raise_()
        self.label_4.raise_()
        self.cbRobot.raise_()
        self.btnEnviarIstruccion.raise_()
        self.btnObtenerDrone.raise_()
        self.btnDecenderDrone.raise_()
        self.btnIsquierdaDrone.raise_()
        self.btnAdelanteDrone.raise_()
        self.btnDerechaDrone.raise_()
        self.btnAtrasDrone.raise_()
        self.btnElevarDrone.raise_()
        self.label_8.raise_()
        self.cbTiempoSesion.raise_()
        self.proBarTiempoSesion.raise_()
        self.btnResumen.raise_()
        self.btnDetener.raise_()
        self.btnPausar.raise_()
        self.btbCapturarObservaciones.raise_()
        self.labelComandosMentales.raise_()
        self.labelEventoDrone.raise_()
        self.label_11.raise_()
        self.progressBar_2.raise_()
        self.progressBar_3.raise_()
        self.label_13.raise_()
        self.groupBox.raise_()
        self.cbBanda.raise_()
        self.btnElevarHumbral.raise_()
        self.btnBajarHumnbral.raise_()
        self.progressBar_4.raise_()
        self.label_16.raise_()
        self.cbPista.raise_()
        self.label_17.raise_()
        self.label_14.raise_()
        self.label_18.raise_()
        self.frame_4.raise_()
        self.btnIniciarConfigurarConexion.raise_()
        self.btnActivarDrone.raise_()
        self.label_7.raise_()
        self.cbEjercicio.raise_()
        self.btnAplicarBandas.raise_()
        self.btnIniciarTerapia.raise_()
        self.btnActivarEmotiv.raise_()
        self.btnAterrizarDrone.raise_()
        self.label_9.raise_()
        self.lbMinutos.raise_()
        self.lbUmbral.raise_()
        self.edtUmbral.raise_()
        self.lbValorUmbral.raise_()
        self.label_19.raise_()
        self.label_10.raise_()
        self.label_20.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Terapia"))
        self.label_2.setText(_translate("Dialog", "Paciente:"))
        self.cbPaciente.setItemText(0, _translate("Dialog", "Paciente x"))
        self.cbPaciente.setItemText(1, _translate("Dialog", "Paciente y"))
        self.cbPaciente.setItemText(2, _translate("Dialog", "Paciente z"))
        self.label_4.setText(_translate("Dialog", "Robot:"))
        self.cbRobot.setItemText(0, _translate("Dialog", "Dron Be Boop"))
        self.cbRobot.setItemText(1, _translate("Dialog", "Dron Tello"))
        self.cbRobot.setItemText(2, _translate("Dialog", "Robot Lego"))
        self.btnEnviarIstruccion.setText(_translate("Dialog", "Mostrar Instrucciones"))
        self.btnObtenerDrone.setText(_translate("Dialog", "Obtener Control"))
        self.btnDecenderDrone.setText(_translate("Dialog", "Decender Drone"))
        self.btnIsquierdaDrone.setText(_translate("Dialog", "<"))
        self.btnAdelanteDrone.setText(_translate("Dialog", "^"))
        self.btnDerechaDrone.setText(_translate("Dialog", ">"))
        self.btnAtrasDrone.setText(_translate("Dialog", "v"))
        self.btnElevarDrone.setText(_translate("Dialog", "Elevar Drone"))
        self.label_8.setText(_translate("Dialog", "Tiempo:"))
        self.cbTiempoSesion.setItemText(0, _translate("Dialog", "Sin Seleccion"))
        self.cbTiempoSesion.setItemText(1, _translate("Dialog", "1 Minuto"))
        self.cbTiempoSesion.setItemText(2, _translate("Dialog", "5 Minutos"))
        self.cbTiempoSesion.setItemText(3, _translate("Dialog", "10 Minutos"))
        self.cbTiempoSesion.setItemText(4, _translate("Dialog", "15 Minutos"))
        self.cbTiempoSesion.setItemText(5, _translate("Dialog", "20 Minutos"))
        self.cbTiempoSesion.setItemText(6, _translate("Dialog", "25 Minutos"))
        self.btnResumen.setText(_translate("Dialog", ">"))
        self.btnDetener.setText(_translate("Dialog", "[]"))
        self.btnPausar.setText(_translate("Dialog", "l l"))
        self.btbCapturarObservaciones.setText(_translate("Dialog", "Capturar observaciones"))
        self.labelComandosMentales.setText(_translate("Dialog", "Estado de los comandos mentales"))
        self.labelEventoDrone.setText(_translate("Dialog", "Evento del Drone"))
        self.label_13.setText(_translate("Dialog", "BCI"))
        self.groupBox.setTitle(_translate("Dialog", "Tipo de Ejercicio"))
        self.rbInivitorio.setText(_translate("Dialog", "Inhibitorio"))
        self.rdbExitatorio.setText(_translate("Dialog", "Excitatorio"))
        self.cbBanda.setItemText(0, _translate("Dialog", "Theta/Beta"))
        self.cbBanda.setItemText(1, _translate("Dialog", "Beta Low"))
        self.cbBanda.setItemText(2, _translate("Dialog", "Theta"))
        self.cbBanda.setItemText(3, _translate("Dialog", "Beta High"))
        self.cbBanda.setItemText(4, _translate("Dialog", "Gama"))
        self.cbBanda.setItemText(5, _translate("Dialog", "Alfa"))
        self.btnElevarHumbral.setToolTip(_translate("Dialog", "Solo se permiten umbral entre 5% y 95%"))
        self.btnElevarHumbral.setText(_translate("Dialog", ">"))
        self.btnBajarHumnbral.setToolTip(_translate("Dialog", "Solo se permiten umbral entre 5% y 95%"))
        self.btnBajarHumnbral.setText(_translate("Dialog", "<"))
        self.label_16.setText(_translate("Dialog", "Pista:"))
        self.cbPista.setItemText(0, _translate("Dialog", "Sin Seleccion"))
        self.cbPista.setItemText(1, _translate("Dialog", "Sin Pista"))
        self.cbPista.setItemText(2, _translate("Dialog", "Pista 1"))
        self.cbPista.setItemText(3, _translate("Dialog", "Pista 2"))
        self.cbPista.setItemText(4, _translate("Dialog", "Pista 3"))
        self.label_17.setText(_translate("Dialog", "Robot"))
        self.label_14.setText(_translate("Dialog", "Puntos Obtenidos"))
        self.label_18.setText(_translate("Dialog", "     0"))
        self.label_3.setText(_translate("Dialog", "Nueva Terapia de tipo Neurofeedback"))
        self.label_6.setText(_translate("Dialog", "Terapeuta: nombre:"))
        self.label_15.setText(_translate("Dialog", "Monica Perales"))
        self.label_5.setText(_translate("Dialog", "Martes 17 de Octubre del 2021"))
        self.btnIniciarConfigurarConexion.setText(_translate("Dialog", "Configura tu conexion"))
        self.btnActivarDrone.setText(_translate("Dialog", "Activar robot"))
        self.label_7.setText(_translate("Dialog", "Ejercicio:"))
        self.cbEjercicio.setItemText(0, _translate("Dialog", "Elevar drone"))
        self.cbEjercicio.setItemText(1, _translate("Dialog", "Decender Drone"))
        self.cbEjercicio.setItemText(2, _translate("Dialog", "Modo libre"))
        self.btnAplicarBandas.setText(_translate("Dialog", "Aplicar"))
        self.btnIniciarTerapia.setText(_translate("Dialog", "Iniciar terapia"))
        self.btnActivarEmotiv.setText(_translate("Dialog", "Activar Diadema"))
        self.btnAterrizarDrone.setText(_translate("Dialog", "+"))
        self.label_9.setText(_translate("Dialog", "Elect(s): F3, F4"))
        self.lbMinutos.setText(_translate("Dialog", "00 : 00 "))
        self.edtUmbral.setPlaceholderText(_translate("Dialog", "5-95"))
        self.lbValorUmbral.setText(_translate("Dialog", "30 "))
        self.label_19.setText(_translate("Dialog", "%"))
        self.label_10.setText(_translate("Dialog", "-----Altura Minima --->1 Metro"))
        self.label_20.setText(_translate("Dialog", "-----Altura Minima --->2 Metro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
