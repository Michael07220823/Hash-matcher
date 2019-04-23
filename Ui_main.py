# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ASIA-I627-A\Desktop\hash\main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import  hashlib

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 316)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("magnifier.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 20, 711, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.choose_file_button = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choose_file_button.setFont(font)
        self.choose_file_button.setAutoDefault(True)
        self.choose_file_button.setObjectName("choose_file_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.choose_file_button)
        self.choose_file_button.clicked.connect(self.read_file)

        self.choose_hash_1 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.choose_hash_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_hash_1.sizePolicy().hasHeightForWidth())
        self.choose_hash_1.setSizePolicy(sizePolicy)
        self.choose_hash_1.setMaximumSize(QtCore.QSize(79, 24))
        self.choose_hash_1.setBaseSize(QtCore.QSize(79, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choose_hash_1.setFont(font)
        self.choose_hash_1.setEditable(False)
        self.choose_hash_1.setCurrentText("")
        self.choose_hash_1.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.choose_hash_1.setObjectName("choose_hash_1")
        self.sha_item = ["sha256","sha384","sha512"]
        self.choose_hash_1.addItems(iter(self.sha_item))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.choose_hash_1)

        self.read_hash_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.read_hash_label.setFont(font)
        self.read_hash_label.setAlignment(QtCore.Qt.AlignCenter)
        self.read_hash_label.setObjectName("read_hash_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.read_hash_label)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(70, 120, 711, 41))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.choos_hash_2 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choos_hash_2.setFont(font)
        self.choos_hash_2.setObjectName("choos_hash_2")
        self.choos_hash_2.addItems(iter(self.sha_item))

        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.choos_hash_2)
        self.author_hash_code_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.author_hash_code_lineEdit.setFont(font)
        self.author_hash_code_lineEdit.setObjectName("author_hash_code_lineEdit.")

        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.author_hash_code_lineEdit)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(360, 180, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.match_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.match_button.setFont(font)
        self.match_button.setObjectName("match_button")
        self.match_button.clicked.connect(self.result_message)

        self.verticalLayout.addWidget(self.match_button)
        self.exit_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 893, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def read_file(self):
        global data
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dlg.setFilter(QtCore.QDir.Files)
        if dlg.exec_():
            filenames= dlg.selectedFiles()
            with open(filenames[0], mode='rb') as f: 
                data = f.read()
            # while True:
                if self.choose_hash_1.currentText() == "sha256":
                    self.hash_sha256(data)
                elif self.choose_hash_1.currentText() == "sha384":
                    self.hash_sha384(data)
                elif self.choose_hash_1.currentText() == "sha512":
                    self.hash_sha512(data)
                # print(data)
                # print(type(self.choose_hash_1.currentText()))
                # self.hash_sha256(data)

    def hash_sha256(self, data):
        global sha256
        sha256 = hashlib.sha256(data).hexdigest()
        self.read_hash_label.setText(str(sha256))
        self.read_hash_label.adjustSize()

    def hash_sha384(self, data):
        global sha384
        sha384 = hashlib.sha384(data).hexdigest()
        self.read_hash_label.setText(str(sha384))
        self.read_hash_label.adjustSize()

    def hash_sha512(self, data):
        global sha512
        sha512 = hashlib.sha512(data).hexdigest()
        self.read_hash_label.setText(str(sha512))
        self.read_hash_label.adjustSize()
    
    def match_button_click(self):
        print(type(self.choose_hash_1.currentText()))
        print(self.choos_hash_2.currentText())
        self.result_message()
        if self.choose_hash_1.currentText() != self.choos_hash_2.currentText():
            print("Here is 'if self.choose_hash_1.currentText() != self.choos_hash_2.currentText():'")
            self.result_message()
        elif self.choose_hash_1.currentText() == self.choos_hash_2.currentText():
            if self.choose_hash_1.currentText == "sha256":
                print(self.author_hash_code_lineEdit.text())
                if sha256 == self.author_hash_code_lineEdit.text():
                    print(self.author_hash_code_lineEdit.text())

    def result_message(self):
        # reply = QtWidgets.QMessageBox.information(QtWidgets, "Result", "消息", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
         
        buttonReply = QtWidgets.QMessageBox.question(QtWidgets, 'PyQt5 message', "Do you like PyQt5?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            print('Yes clicked.')
        else:
            print('No clicked.')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hash File Matcher"))
        self.choose_file_button.setText(_translate("MainWindow", "Choose file"))
        self.choose_file_button.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.read_hash_label.setText(_translate("MainWindow", "No choose file yet."))
        self.match_button.setText(_translate("MainWindow", "Match"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QWidget()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
