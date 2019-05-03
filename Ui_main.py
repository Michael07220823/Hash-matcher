# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ASIA-I627-A\Downloads\Hash-matcher-master\main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy
# hashlib套件用於建算雜湊值
import  hashlib
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # 重設視窗大小
        MainWindow.resize(1600, 350)
        # 設定視窗最大大小
        MainWindow.setMaximumSize(1600, 350)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("magnifier.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 建立formLayoutWidget表格佈局元件
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        # 設定表格佈局大小
        # setGeometry(QtCore.QRect(x position, y position, width, height))
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1600, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        # 建立choose file按鈕
        self.choose_file_button = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choose_file_button.setFont(font)
        self.choose_file_button.setAutoDefault(True)
        self.choose_file_button.setObjectName("choose_file_button")
        # 設定choose file按鈕擺在左邊，LabelRole左邊，FieldRole右邊
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.choose_file_button)
        # 當按下choose file按鈕時，執行read_file()方法
        self.choose_file_button.clicked.connect(self.read_file)


        # 建立choose_hash_menu雜湊選單
        self.choose_hash_menu = QtWidgets.QComboBox(self.formLayoutWidget)
        self.choose_hash_menu.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_hash_menu.sizePolicy().hasHeightForWidth())
        self.choose_hash_menu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choose_hash_menu.setFont(font)
        self.choose_hash_menu.setEditable(False)
        self.choose_hash_menu.setCurrentText("")
        self.choose_hash_menu.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.choose_hash_menu.setObjectName("choose_hash_menu")
        # sha_item用於建立choose_hash_menu選單的選項
        self.sha_item = ["sha256","sha384","sha512"]
        # 將選項放入choose_hash_menu選單裡
        self.choose_hash_menu.addItems(iter(self.sha_item))
        # 當choose_hash_menu選項改變時，執行choose_hash_menu_change()方法
        self.choose_hash_menu.currentTextChanged.connect(self.choose_hash_menu_change)
        # 設定雜湊選單擺在左邊，LabelRole左邊，FieldRole右邊
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.choose_hash_menu)


        # 建立read_hash_label標籤，用於顯示計算後的雜湊碼
        self.read_hash_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.read_hash_label.setFont(font)
        self.read_hash_label.setText("")
        # 設定read_hash_label文字靠左對齊
        self.read_hash_label.setAlignment(QtCore.Qt.AlignLeft)
        self.read_hash_label.setObjectName("read_hash_label")
        # 讓read_hash_label顯式的雜湊碼可以複製。
        self.read_hash_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        # 自動調整read_hash_label標籤至適合大小
        self.read_hash_label.adjustSize()
        # self.read_hash_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # 設定read_hash_label標籤在右邊，LabelRole左邊，FieldRole右邊
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.read_hash_label)


        # 建立formLayoutWidget_2表格佈局元件
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 120, 1520, 61))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
    

        # 建立author_hash_code_lineEdit，用於貼上作者提供的雜湊碼
        font = QtGui.QFont()
        font.setPointSize(12)
        self.author_hash_code_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.author_hash_code_lineEdit.setFont(font)
        self.author_hash_code_lineEdit.setObjectName("author_hash_code_lineEdit")
        # self.author_hash_code_lineEdit.setGeometry(10, 140, 600, 61)
        # self.author_hash_code_lineEdit.adjustSize()
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.author_hash_code_lineEdit)


        # 建立Author標籤
        self.author_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.author_label.setFont(font)
        self.author_label.setText("author code")
        # 設定author_label文字靠左對齊
        self.author_label.setAlignment(QtCore.Qt.AlignLeft)
        self.author_label.setObjectName("author_label")
        # self.author_label.setGeometry(10, 140, 500, 61)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.author_label)


        # 建立verticalLayoutWidget垂直排版，用於排序display_result_label標籤、Match以及Exit按紐
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 200, 800, 120))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")


        # 建立display_result_label標籤，用於顯示匹配的結果
        self.display_result_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        # 設定display_result_label文字大小
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(200)
        self.display_result_label.setFont(font)
        self.display_result_label.setText("")
        # 設定display_result_label標籤文字置中
        self.display_result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.display_result_label.setObjectName("label")
        self.verticalLayout.addWidget(self.display_result_label)


        # 建立Match按鈕
        self.match_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.match_button.setFont(font)
        self.match_button.setObjectName("match_button")
        # 當按下Match按鈕時，執行match_button_click()方法
        self.match_button.clicked.connect(self.match_button_click)
        self.verticalLayout.addWidget(self.match_button)


        # 建立Exit按鈕
        self.exit_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button)
        # 當Exit按鈕被點擊時，執行exit_click()方法，用以關閉程式
        self.exit_button.clicked.connect(self.exit_click)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # read_file()用於選擇要計算雜湊的檔案
    def read_file(self):
        global data
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
        dlg.setFilter(QtCore.QDir.Files)
        if dlg.exec_():
            filenames= dlg.selectedFiles()
            with open(filenames[0], mode='rb') as f: 
                data = f.read()
                # 如果選擇sha256，則使用hash_sha256()計算雜湊
                if self.choose_hash_menu.currentText() == "sha256":
                    self.hash_sha256(data)
                # 如果選擇sha384，則使用hash_sha384()計算雜湊
                elif self.choose_hash_menu.currentText() == "sha384":
                    self.hash_sha384(data)
                # 如果選擇sha512，則使用hash_sha512()計算雜湊
                elif self.choose_hash_menu.currentText() == "sha512":
                    self.hash_sha512(data)

    # choose_hash_menu_change()用於監聽雜湊選單事件，當選項改變時，執行此方法
    def choose_hash_menu_change(self):
        try:
            # 如果選項是sha256，則執行hash_sha256()
            if self.choose_hash_menu.currentIndex() == 0:
                self.hash_sha256(data)
            # 如果選項是sha384，則執行hash_sha384()
            elif self.choose_hash_menu.currentIndex() == 1:
                self.hash_sha384(data)
            else:
                # 如果選項是sha512，則執行hash_sha512()
                self.hash_sha512(data)
        # 當雜湊選單都沒選時，會出現data變數沒有給予的問題
        except NameError as error:
            pass
            # self.read_hash_label.setText("you are not choose file yet !")
            # print("[INFO] Error message: %s" % error)
    
    # hash_sha256()用於計算sha256雜湊，並設定顯示結果於read_hash_label標籤
    def hash_sha256(self, data):
        sha256 = hashlib.sha256(data).hexdigest()
        self.read_hash_label.setText(str(sha256))

    # hash_sha384()用於計算sha384雜湊，並設定顯示結果於read_hash_label標籤
    def hash_sha384(self, data):
        sha384 = hashlib.sha384(data).hexdigest()
        self.read_hash_label.setText(str(sha384))

    # hash_sha512()用於計算sha512雜湊，並設定顯示結果於read_hash_label標籤
    def hash_sha512(self, data):
        sha512 = hashlib.sha512(data).hexdigest()
        self.read_hash_label.setText(str(sha512))
    
    # match_button_click()用於Match按鈕按下後的動作
    def match_button_click(self):
        # 如果read_hash_label標籤或author_hash_code_lineEdit的值為空的，則顯示"Not choose file or no hash code can compare !"
        if self.read_hash_label.text() == "" or self.author_hash_code_lineEdit.text() == "":
            # 將display_result_label標籤文字設成紅色
            self.display_result_label.setStyleSheet("QLabel {color : red }")
            self.display_result_label.setText("Not choose file or no author code can compare !")
        else:
            # 將author_hash_code_lineEdit的文字先轉英文字母小寫，因為檔案計算出的雜湊碼也是英文字母小寫
            word = self.author_hash_code_lineEdit.text().lower()
            # 將轉換後的雜湊碼顯示於author_hash_code_lineEdit
            self.author_hash_code_lineEdit.setText(word)
            # 如果read_hash_label標籤的文字與author_hash_code_lineEdit的文字相同就執行以下的程式
            if self.read_hash_label.text() == self.author_hash_code_lineEdit.text():
                # 將display_result_label標籤的文字設成綠色
                self.display_result_label.setStyleSheet("QLabel {color : green }")
                self.display_result_label.setText("Correct")
            else:
                # 將display_result_label標籤的文字設成紅色
                self.display_result_label.setStyleSheet("QLabel {color : red; }")
                self.display_result_label.setText("Incorrect")

    # 當Exit按鈕被按下時，執行exit_click()
    def exit_click(self):
        # 離開程式
        sys.exit()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # 設定程式標題名稱
        MainWindow.setWindowTitle(_translate("MainWindow", "Hash Matcher"))
        # 設定按鈕名稱
        self.choose_file_button.setText(_translate("MainWindow", "Choose filec(ctrl+o)"))
        self.match_button.setText(_translate("MainWindow", "Match(ctrl+m)"))
        self.exit_button.setText(_translate("MainWindow", "Exit(ctrl+e)"))
        # 設定choose file按鈕的快捷鍵
        self.choose_file_button.setShortcut(_translate("MainWindow", "ctrl+o"))
        self.match_button.setShortcut(_translate("MainWindow", "ctrl+m"))
        self.exit_button.setShortcut(_translate("MainWindow", "ctrl+e"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # 建立一個ui物件
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # 將視窗控制項顯示於螢幕
    MainWindow.show()
    '''app.exec_()為程式主迴圈，事件處理從本行開始，主迴圈接收事件訊息，再將其分發給程式個個控制項
    如果呼叫exit()或主控制項被銷毀，主迴圈就結束'''
    sys.exit(app.exec_())

# 參考來源:https://www.books.com.tw/products/0010787989?gclid=CjwKCAjwza_mBRBTEiwASDWVvprr0EKQnonk1q_qQk7gA2UykFD2X6IiA4okYvzLw0KGoJLC0Z8mrRoCngEQAvD_BwE