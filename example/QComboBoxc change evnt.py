# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QCombobox.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(739, 455)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(250, 80, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(280, 130, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 130, 72, 15))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 170, 72, 15))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 170, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        # label '2' and line edit '2' is closed by default.
        self.label_2.close()
        self.lineEdit_2.close()
        # add QCombobox index change event
        self.comboBox.currentTextChanged.connect(self.comboBox_changed)

    # current text change function
    def comboBox_changed(self):
        if self.comboBox.currentIndex() == 0:
            self.label.show()
            self.lineEdit.show()
            self.label_2.close()
            self.lineEdit_2.close()
        else:
            self.label.close()
            self.lineEdit.close()
            self.label_2.show()
            self.lineEdit_2.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "显示1"))
        self.comboBox.setItemText(1, _translate("Form", "显示2"))
        self.lineEdit.setText(_translate("Form", "1"))
        self.label.setText(_translate("Form", "1"))
        self.label_2.setText(_translate("Form", "2"))
        self.lineEdit_2.setText(_translate("Form", "2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())