# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregarPaciente.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import vistas.images

class Ui_NuevoPaciente(object):
    def setupUi(self, NuevoPaciente):
        NuevoPaciente.setObjectName("NuevoPaciente")
        NuevoPaciente.resize(736, 540)
        NuevoPaciente.setMinimumSize(QtCore.QSize(736, 540))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/paciente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NuevoPaciente.setWindowIcon(icon)
        self.label_17 = QtWidgets.QLabel(NuevoPaciente)
        self.label_17.setGeometry(QtCore.QRect(30, 510, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.ptDiagnostico = QtWidgets.QPlainTextEdit(NuevoPaciente)
        self.ptDiagnostico.setGeometry(QtCore.QRect(440, 190, 271, 231))
        self.ptDiagnostico.setObjectName("ptDiagnostico")
        self.label_16 = QtWidgets.QLabel(NuevoPaciente)
        self.label_16.setGeometry(QtCore.QRect(530, 160, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_7 = QtWidgets.QLabel(NuevoPaciente)
        self.label_7.setGeometry(QtCore.QRect(0, 80, 741, 521))
        self.label_7.setMinimumSize(QtCore.QSize(480, 510))
        self.label_7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(210, 220, 220), stop:1 rgba(100, 130, 190));\n"
"\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.frame = QtWidgets.QFrame(NuevoPaciente)
        self.frame.setGeometry(QtCore.QRect(0, 0, 741, 81))
        self.frame.setStyleSheet("background-color: rgb(200, 198, 223);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_Tutor = QtWidgets.QLabel(self.frame)
        self.label_Tutor.setGeometry(QtCore.QRect(0, 10, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_Tutor.setFont(font)
        self.label_Tutor.setStyleSheet("\n"
"font: 75 19pt \"Times New Roman\";")
        self.label_Tutor.setObjectName("label_Tutor")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(650, 0, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("image: url(:/newPrefix/paciente.png);")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.frame_3 = QtWidgets.QFrame(NuevoPaciente)
        self.frame_3.setGeometry(QtCore.QRect(0, 80, 741, 8))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 8))
        self.frame_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(214, 225, 229), stop:1 rgba(109, 130, 198));\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btnCancelar = QtWidgets.QPushButton(NuevoPaciente)
        self.btnCancelar.setGeometry(QtCore.QRect(440, 430, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setStyleSheet("background-color: rgb(255, 211, 160);\n"
"background-color: rgb(200, 198, 223);")
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnRegistrar = QtWidgets.QPushButton(NuevoPaciente)
        self.btnRegistrar.setGeometry(QtCore.QRect(610, 430, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setStyleSheet("background-color: rgb(180, 255, 199);\n"
"background-color: rgb(200, 198, 223);")
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.label_8 = QtWidgets.QLabel(NuevoPaciente)
        self.label_8.setGeometry(QtCore.QRect(430, 110, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.cbTutor = QtWidgets.QComboBox(NuevoPaciente)
        self.cbTutor.setGeometry(QtCore.QRect(560, 110, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbTutor.setFont(font)
        self.cbTutor.setObjectName("cbTutor")
        self.cbTutor.addItem("")
        self.label_32 = QtWidgets.QLabel(NuevoPaciente)
        self.label_32.setGeometry(QtCore.QRect(10, 170, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_22 = QtWidgets.QLabel(NuevoPaciente)
        self.label_22.setGeometry(QtCore.QRect(10, 490, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_25 = QtWidgets.QLabel(NuevoPaciente)
        self.label_25.setGeometry(QtCore.QRect(10, 210, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.cbMunicipio = QtWidgets.QComboBox(NuevoPaciente)
        self.cbMunicipio.setGeometry(QtCore.QRect(210, 340, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbMunicipio.setFont(font)
        self.cbMunicipio.setObjectName("cbMunicipio")
        self.cbMunicipio.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(NuevoPaciente)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 200, 221, 41))
        self.groupBox_2.setObjectName("groupBox_2")
        self.rbFemenino = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbFemenino.setGeometry(QtCore.QRect(120, 20, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbFemenino.setFont(font)
        self.rbFemenino.setObjectName("rbFemenino")
        self.rbMasculino = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbMasculino.setGeometry(QtCore.QRect(10, 20, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbMasculino.setFont(font)
        self.rbMasculino.setObjectName("rbMasculino")
        self.label_30 = QtWidgets.QLabel(NuevoPaciente)
        self.label_30.setGeometry(QtCore.QRect(10, 430, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.dateEdit = QtWidgets.QDateEdit(NuevoPaciente)
        self.dateEdit.setGeometry(QtCore.QRect(210, 250, 110, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1921, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1920, 9, 26), QtCore.QTime(1, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.leApellidoPaterno = QtWidgets.QLineEdit(NuevoPaciente)
        self.leApellidoPaterno.setGeometry(QtCore.QRect(210, 110, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leApellidoPaterno.setFont(font)
        self.leApellidoPaterno.setText("")
        self.leApellidoPaterno.setMaxLength(27)
        self.leApellidoPaterno.setDragEnabled(True)
        self.leApellidoPaterno.setObjectName("leApellidoPaterno")
        self.label_26 = QtWidgets.QLabel(NuevoPaciente)
        self.label_26.setGeometry(QtCore.QRect(10, 340, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.leNumeroContacto = QtWidgets.QLineEdit(NuevoPaciente)
        self.leNumeroContacto.setGeometry(QtCore.QRect(210, 460, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leNumeroContacto.setFont(font)
        self.leNumeroContacto.setMaxLength(10)
        self.leNumeroContacto.setObjectName("leNumeroContacto")
        self.label_20 = QtWidgets.QLabel(NuevoPaciente)
        self.label_20.setGeometry(QtCore.QRect(10, 250, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.leNumeroCalle = QtWidgets.QLineEdit(NuevoPaciente)
        self.leNumeroCalle.setGeometry(QtCore.QRect(360, 400, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leNumeroCalle.setFont(font)
        self.leNumeroCalle.setMaxLength(5)
        self.leNumeroCalle.setObjectName("leNumeroCalle")
        self.label_9 = QtWidgets.QLabel(NuevoPaciente)
        self.label_9.setGeometry(QtCore.QRect(10, 140, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.cbEstado = QtWidgets.QComboBox(NuevoPaciente)
        self.cbEstado.setGeometry(QtCore.QRect(210, 310, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbEstado.setFont(font)
        self.cbEstado.setObjectName("cbEstado")
        self.cbEstado.addItem("")
        self.leCalle = QtWidgets.QLineEdit(NuevoPaciente)
        self.leCalle.setGeometry(QtCore.QRect(210, 400, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leCalle.setFont(font)
        self.leCalle.setMaxLength(27)
        self.leCalle.setObjectName("leCalle")
        self.label_27 = QtWidgets.QLabel(NuevoPaciente)
        self.label_27.setGeometry(QtCore.QRect(10, 110, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.leCodigoPostal = QtWidgets.QLineEdit(NuevoPaciente)
        self.leCodigoPostal.setGeometry(QtCore.QRect(210, 430, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leCodigoPostal.setFont(font)
        self.leCodigoPostal.setMaxLength(5)
        self.leCodigoPostal.setObjectName("leCodigoPostal")
        self.label_21 = QtWidgets.QLabel(NuevoPaciente)
        self.label_21.setGeometry(QtCore.QRect(10, 280, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_19 = QtWidgets.QLabel(NuevoPaciente)
        self.label_19.setGeometry(QtCore.QRect(10, 460, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.leNombres = QtWidgets.QLineEdit(NuevoPaciente)
        self.leNombres.setGeometry(QtCore.QRect(210, 170, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leNombres.setFont(font)
        self.leNombres.setMaxLength(27)
        self.leNombres.setObjectName("leNombres")
        self.leApellidoMaterno = QtWidgets.QLineEdit(NuevoPaciente)
        self.leApellidoMaterno.setGeometry(QtCore.QRect(210, 140, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leApellidoMaterno.setFont(font)
        self.leApellidoMaterno.setMaxLength(27)
        self.leApellidoMaterno.setObjectName("leApellidoMaterno")
        self.label_29 = QtWidgets.QLabel(NuevoPaciente)
        self.label_29.setGeometry(QtCore.QRect(10, 310, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_28 = QtWidgets.QLabel(NuevoPaciente)
        self.label_28.setGeometry(QtCore.QRect(10, 370, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_31 = QtWidgets.QLabel(NuevoPaciente)
        self.label_31.setGeometry(QtCore.QRect(10, 400, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.leLoclidad = QtWidgets.QLineEdit(NuevoPaciente)
        self.leLoclidad.setGeometry(QtCore.QRect(210, 370, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leLoclidad.setFont(font)
        self.leLoclidad.setMaxLength(27)
        self.leLoclidad.setObjectName("leLoclidad")
        self.leNacionalidad = QtWidgets.QLineEdit(NuevoPaciente)
        self.leNacionalidad.setGeometry(QtCore.QRect(210, 280, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leNacionalidad.setFont(font)
        self.leNacionalidad.setMaxLength(27)
        self.leNacionalidad.setObjectName("leNacionalidad")
        self.leCorreoElectronico = QtWidgets.QLineEdit(NuevoPaciente)
        self.leCorreoElectronico.setGeometry(QtCore.QRect(210, 490, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leCorreoElectronico.setFont(font)
        self.leCorreoElectronico.setText("")
        self.leCorreoElectronico.setMaxLength(40)
        self.leCorreoElectronico.setObjectName("leCorreoElectronico")
        self.label_7.raise_()
        self.label_17.raise_()
        self.ptDiagnostico.raise_()
        self.label_16.raise_()
        self.frame.raise_()
        self.frame_3.raise_()
        self.btnCancelar.raise_()
        self.btnRegistrar.raise_()
        self.label_8.raise_()
        self.cbTutor.raise_()
        self.label_32.raise_()
        self.label_22.raise_()
        self.label_25.raise_()
        self.cbMunicipio.raise_()
        self.groupBox_2.raise_()
        self.label_30.raise_()
        self.dateEdit.raise_()
        self.leApellidoPaterno.raise_()
        self.label_26.raise_()
        self.leNumeroContacto.raise_()
        self.label_20.raise_()
        self.leNumeroCalle.raise_()
        self.label_9.raise_()
        self.cbEstado.raise_()
        self.leCalle.raise_()
        self.label_27.raise_()
        self.leCodigoPostal.raise_()
        self.label_21.raise_()
        self.label_19.raise_()
        self.leNombres.raise_()
        self.leApellidoMaterno.raise_()
        self.label_29.raise_()
        self.label_28.raise_()
        self.label_31.raise_()
        self.leLoclidad.raise_()
        self.leNacionalidad.raise_()
        self.leCorreoElectronico.raise_()

        self.retranslateUi(NuevoPaciente)
        QtCore.QMetaObject.connectSlotsByName(NuevoPaciente)

    def retranslateUi(self, NuevoPaciente):
        _translate = QtCore.QCoreApplication.translate
        NuevoPaciente.setWindowTitle(_translate("NuevoPaciente", "Agregar Paciente"))
        self.ptDiagnostico.setPlaceholderText(_translate("NuevoPaciente", "Ingresa un disgnostico y los sintomas del paciente"))
        self.label_16.setText(_translate("NuevoPaciente", "Diagnostico"))
        self.label_Tutor.setText(_translate("NuevoPaciente", "Nuevo Paciente"))
        self.btnCancelar.setText(_translate("NuevoPaciente", "Limpiar campos"))
        self.btnRegistrar.setText(_translate("NuevoPaciente", "Registrar"))
        self.label_8.setText(_translate("NuevoPaciente", "Selecionar Tutor"))
        self.cbTutor.setItemText(0, _translate("NuevoPaciente", "Sin Tutor"))
        self.label_32.setText(_translate("NuevoPaciente", "Nombre (*)"))
        self.label_22.setText(_translate("NuevoPaciente", "Correo electrónico (*)"))
        self.label_25.setText(_translate("NuevoPaciente", "Genero (*)"))
        self.cbMunicipio.setItemText(0, _translate("NuevoPaciente", "Ameca"))
        self.groupBox_2.setTitle(_translate("NuevoPaciente", "Selecciona una opción"))
        self.rbFemenino.setText(_translate("NuevoPaciente", "Femenino"))
        self.rbMasculino.setText(_translate("NuevoPaciente", "Masculino"))
        self.label_30.setText(_translate("NuevoPaciente", "Código postal"))
        self.label_26.setText(_translate("NuevoPaciente", "Municipio"))
        self.label_20.setText(_translate("NuevoPaciente", "Fecha de nacimiento (*)"))
        self.label_9.setText(_translate("NuevoPaciente", "Apellido Materno (*)"))
        self.cbEstado.setItemText(0, _translate("NuevoPaciente", "Jalisco"))
        self.label_27.setText(_translate("NuevoPaciente", "Apellido Paterno (*)"))
        self.label_21.setText(_translate("NuevoPaciente", "Nacionalidad"))
        self.label_19.setText(_translate("NuevoPaciente", "Número de contacto (*)"))
        self.label_29.setText(_translate("NuevoPaciente", "Estado"))
        self.label_28.setText(_translate("NuevoPaciente", "Localidad"))
        self.label_31.setText(_translate("NuevoPaciente", "Calle y número"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NuevoPaciente = QtWidgets.QDialog()
    ui = Ui_NuevoPaciente()
    ui.setupUi(NuevoPaciente)
    NuevoPaciente.show()
    sys.exit(app.exec_())

