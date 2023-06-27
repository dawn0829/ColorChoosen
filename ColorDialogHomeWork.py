from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("超級無敵調色名牌!")
        self.setWindowIcon(QIcon('drawnpalette.jpg'))

        extractAction = QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        openEditor = QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        mainMenu = self.menuBar()
        
        editorMenu = mainMenu.addMenu("&Editor")
        editorMenu.addAction(openEditor)

        self.home()

    def home(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(200,250)

        extractAction =  QAction(QIcon('drawnpalette.jpg'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.color_picker)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        fontChoice = QAction('選擇字體', self)
        fontChoice.triggered.connect(self.font_choice)
        #self.toolBar = self.addToolBar("Font")
        self.toolBar.addAction(fontChoice)

        color = QColor(0, 0, 0)

        fontColor =  QAction('選擇背景顏色', self)
        fontColor.triggered.connect(self.color_picker)

        self.toolBar.addAction(fontColor)

        checkBox = QCheckBox('擴大視窗', self)
        checkBox.move(300, 25)
        checkBox.stateChanged.connect(self.enlarge_window)

        #print(self.style().objectName())
        label_1= QLabel("我是小東", self)
        label_1.setGeometry(20,100,10000,100)
        self.styleChoice = label_1

        comboBox = QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")

        comboBox.move(50, 250)
        #self.styleChoice.move(20,100)
        comboBox.activated[str].connect(self.style_choice)

        cal = QCalendarWidget(self)
        cal.move(500,200)
        cal.resize(200,200)

        self.show()

    def color_picker(self):
        color = QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)


    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)


    def style_choice(self, text):
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50,50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)
        
    def close_application(self):
        choice =  QMessageBox.question(self, '警告',
                                            "確定要離開超級無敵調色名牌",
                                             QMessageBox.Yes |  QMessageBox.No)
        if choice ==  QMessageBox.Yes:
            print("Bye-Bye!!!!")
            sys.exit()
        else:
            pass
        
  
def run():
    app =  QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()