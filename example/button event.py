import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
    def __init__(self):
        super().__init__()
        #設定變數
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()
    
    def initUI(self):
        #設定視窗名稱
        self.setWindowTitle(self.title)
        #設定視窗大小
        self.setGeometry(self.left, self.top, self.width, self.height)

        #創建一個按鈕
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(200,70)
        #按下按鈕後的功能on_click()
        button.clicked.connect(self.on_click)
        
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())