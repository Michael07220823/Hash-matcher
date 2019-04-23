import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication)
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):     
 
        self.lbl = QLabel("中国", self)
 
        combo = QComboBox(self)         #创建一个下拉列表框并填充了五个列表项
        combo.addItem("中国")
        combo.addItem("美国")
        combo.addItem("日本")
        combo.addItem("俄罗斯")
        combo.addItem("英国")
 
        combo.move(50, 50)
        self.lbl.move(50, 150)
 
        combo.activated[str].connect(self.onActivated)
                                        #一旦列表项被选中，会调用onActivated()方法
          
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('下拉列表框')
        self.show()
         
         
    def onActivated(self, text):    #把下拉列表框中选中的列表项的文本显示在标签组件上
                                    #并且根据标签文本调整了标签大小
        self.lbl.setText(text)
        self.lbl.adjustSize() 
         
                 
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
