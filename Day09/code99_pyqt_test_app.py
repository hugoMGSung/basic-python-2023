import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *


class MainScreen(QMainWindow):

    def __init__(self, wid, hei):
        super().__init__()

        self.setWindowTitle("PYQT Project")  # 프로젝트 타이틀 설정
        self.setGeometry(0, 0, int(wid), int(hei*.9))    # 화면 사이즈 설정

        self.mainWidget = QWidget()                         # 메인 위젯 생성
        self.mainLayout = QVBoxLayout(self.mainWidget)      # 메인 레이아웃 생성 및 메인 위젯 연결
        self.mainTab = QTabWidget()                         # 탭 위젯 생성

        self.mainLayout.addWidget(self.mainTab)             # 메인 레이아웃에 텝 위젯 추가
        self.setCentralWidget(self.mainWidget)              # 메인윈도우 센트럴위젯에 메인 위젯 연결


        self.addWidget = QWidget()                          # 탭에 추가할 위젯 생성
        self.addLayout = QVBoxLayout(self.addWidget)        # 탭에 추가할 래이아웃 생성 및 위젯 연결

        # 스타일 설정
        lbl_red = QLabel('Red') 
        lbl_red.setStyleSheet('color: red;'
                              'border-style: solid;'
                              'border-width: 5px;'
                              'border-color: #FA8072;' 
                              'border-radius: 10px')
        lbl_green = QLabel('Green')
        lbl_green.setStyleSheet('color: green;'
                              'border-style: dashed;'
                              'border-width: 5px;'
                              'border-color: #7FFFD4;')
        # QVBoxLayout 세로로 / QHBoxLayout 가로로 위치
        vbox = QVBoxLayout() # 세로 구분짓는 레이아웃
        vbox.addWidget(lbl_red) # 위젯 추가
        vbox.addWidget(lbl_green)
        
        self.addWidget1 = QWidget()
        self.addWidget1.setLayout(vbox)
                                 # 탭에 추가할 위젯 생성
        self.addLayout1 = QVBoxLayout(self.addWidget1)      # 탭에 추가할 래이아웃 생성 및 위젯 연결

        self.mainTab.addTab(self.addWidget, 'ADD TAB 1')   # 탭에 추가
        self.mainTab.addTab(self.addWidget1, 'ADD TAB 2')   # 탭에 추가

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    size: QSize = app.primaryScreen().size()    # 모니터 사이즈

    main = MainScreen(size.width()/2, size.height())
    sys.exit(app.exec_())