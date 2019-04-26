# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ASIA-I627-A\Downloads\Hash-matcher-master\main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import  hashlib
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 492)
        # MainWindow.setMaximumSize(QtCore.QSize(1000, 492))
        MainWindow.setBaseSize(QtCore.QSize(1350, 492))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("magnifier.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        # 設定介面大小
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1300, 80))
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
        # self.choose_hash_1.setGeometry(100, 100)
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
        # 將選項放入choose_hash_1容器裡。
        self.choose_hash_1.addItems(iter(self.sha_item))
        # 當choose_hash_1選項改變時，執行self.choose_hash_1_change。
        self.choose_hash_1.currentTextChanged.connect(self.choose_hash_1_change)

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.choose_hash_1)
        self.read_hash_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.read_hash_label.setFont(font)
        self.read_hash_label.setText("")
        self.read_hash_label.setAlignment(QtCore.Qt.AlignCenter)
        self.read_hash_label.setObjectName("read_hash_label")
        # 設定read_hash_label文字靠左對齊
        self.read_hash_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.read_hash_label)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 1300, 61))
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
        self.author_hash_code_lineEdit.setObjectName("author_hash_code_lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.author_hash_code_lineEdit)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(600, 260, 160, 120))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.display_result_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.display_result_label.setFont(font)
        self.display_result_label.setText("")
        self.display_result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.display_result_label.setObjectName("label")
        self.verticalLayout.addWidget(self.display_result_label)

        self.match_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.match_button.setFont(font)
        self.match_button.setObjectName("match_button")
        self.verticalLayout.addWidget(self.match_button)
        self.exit_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button)
        # 當exit button被點擊時關閉程式
        self.exit_button.clicked.connect(self.exit_click)

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
                #time.sleep(1)
                    # print(data)
                    # print(type(self.choose_hash_1.currentText()))
                    # self.hash_sha256(data)

    def choose_hash_1_change(self):
        if self.choose_hash_1.currentIndex() == 0:
            self.hash_sha256(data)
        elif self.choose_hash_1.currentIndex() == 1:
            self.hash_sha384(data)
        else:
            self.hash_sha512(data)
        
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
        # self.result_message()
        if self.choose_hash_1.currentText() != self.choos_hash_2.currentText():
            print("Here is 'if self.choose_hash_1.currentText() != self.choos_hash_2.currentText():'")
            self.result_message()
        elif self.choose_hash_1.currentText() == self.choos_hash_2.currentText():
            if self.choose_hash_1.currentText == "sha256":
                print(self.author_hash_code_lineEdit.text())
                if sha256 == self.author_hash_code_lineEdit.text():
                    print(self.author_hash_code_lineEdit.text())

    def exit_click(self):
        sys.exit()

    def result_message(self):
        pass
        # reply = QtWidgets.QMessageBox.information(QtWidgets, "Result", "消息", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
         
        # buttonReply = QtWidgets.QMessageBox.question(QtWidgets, 'PyQt5 message', "Do you like PyQt5?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        # # if buttonReply == QtWidgets.QMessageBox.Yes:
        #     print('Yes clicked.')
        # else:
        #     print('No clicked.')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hash Matcher"))
        self.choose_file_button.setText(_translate("MainWindow", "Choose file"))
        self.choose_file_button.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.match_button.setText(_translate("MainWindow", "Match"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

