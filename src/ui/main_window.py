from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout,QVBoxLayout, QWidget, QCalendarWidget
from PySide6.QtGui import QColor, QPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WAKALENDARIO")
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#1e1f31"))
        self.setPalette(palette)
        
        container = Container()
        self.setCentralWidget(container) 


class Container(QWidget):
    def __init__(self):
        super().__init__()
        calendar = QCalendarWidget()
        l_panel = QVBoxLayout()
        r_panel = QWidget() #provb
        l_panel.addWidget()
        layout = QHBoxLayout()
        layout.addLayout(l_panel)
        layout.addLayout(r_panel)

        
        self.setLayout(layout)

       

app = QApplication([])
window = MainWindow()
window.show()
app.exec()