# 레이아웃 절대적배치
import sys
from PyQt5.QtWidgets import *

class YourApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)

        # 필수 설정
        self.setWindowTitle('절대 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YourApp()
    sys.exit(app.exec_())