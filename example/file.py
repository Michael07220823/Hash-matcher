from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("Test")
        self.myButton.clicked.connect(self.msg)
    def msg(self):
        directory1 = QFileDialog.getExistingDirectory(self,
        "get file",
        "./")                 #起始路徑
        print(directory1)
        fileName1, filetype = QFileDialog.getOpenFileName(self,
        "選取檔案",
        "./",
        "All Files (*);;Text Files (*.txt)")  #設定副檔名過濾,注意用雙分號間隔
        print(fileName1,filetype)
        files, ok1 = QFileDialog.getOpenFileNames(self,
        "多檔案選擇",
        "./",
        "All Files (*);;Text Files (*.txt)")
        print(files,ok1)
        fileName2, ok2 = QFileDialog.getSaveFileName(self,
        "檔案儲存",
        "./",
        "All Files (*);;Text Files (*.txt)")

if __name__=="__main__": 
    import sys 
    app=QtWidgets.QApplication(sys.argv) 
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_()) 