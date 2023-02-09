import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('Simple Window')
        # 아이콘 추가
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        # self.move(1440 // 2 - 200, 900 // 2 - 100) # 정중앙 위치잡기
        self.resize(400, 200)
        self.show() # 핵심!!

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp() 
    sys.exit(app.exec_())