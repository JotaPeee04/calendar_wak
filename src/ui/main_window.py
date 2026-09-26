from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout,QVBoxLayout, QWidget, QCalendarWidget, QPushButton, QTableWidget, QTableWidgetItem
from PySide6.QtCore import QDate
from PySide6.QtGui import QColor, QPalette
from src.storage.db import fetch_events, insert_event, delete_event, update_event


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

        l_panel = QVBoxLayout()
        r_panel = QVBoxLayout() #prov
        
        #LEFT PANEL
        button_panel = QHBoxLayout()

        ## calendario
        self.calendar = QCalendarWidget()
        self.calendar.setSelectedDate(QDate.currentDate())
        

        self.new_event_button = QPushButton(text="Create New Event")

        self.month_button, self.week_button, self.day_button = QPushButton(text="month"), QPushButton(text="week"), QPushButton(text="day")
        
        button_panel.addWidget(self.month_button)
        button_panel.addWidget(self.week_button)
        button_panel.addWidget(self.day_button)

        l_panel.addLayout(button_panel)
        l_panel.addWidget(self.calendar)
        l_panel.addWidget(self.new_event_button)

        #RIGHT PANEL
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Fecha","Hora",  "Título", "Categoría", "Descripción"])

        r_panel.addWidget(self.table) #prov

        layout = QHBoxLayout()
        layout.addLayout(l_panel,1)
        layout.addLayout(r_panel,3 ) #prov
        
        self.setLayout(layout)

        #signals
        self.calendar.selectionChanged.connect(self.date_selection)
        self.new_event_button.clicked.connect(self.create_event)
        self.month_button.clicked.connect(lambda _: self.change_calendar_display(0))
        self.week_button.clicked.connect(lambda _: self.change_calendar_display(1))
        self.day_button.clicked.connect(lambda _: self.change_calendar_display(2))

        self.date_selection()

    def create_event(self):
        print("nuevo evento")

    def change_calendar_display(self, period:int):
        #0 month, #1 week, 2 day
        print(str(period))

    def date_selection(self):
        date = self.calendar.selectedDate()
        events = fetch_events(date.toPython())
        self.update_table(events)


    def update_table(self, events):
        self.table.clearContents()
        size = len(events)
        self.table.setRowCount(size)
        for index, event in enumerate(events, start=0):
            #"Fecha","Hora",  "Título", "Categoría", "Descripción"
            date = QTableWidgetItem(event.s_date.isoformat())
            time = QTableWidgetItem(event.s_time.isoformat())
            title = QTableWidgetItem(event.title)
            cat = QTableWidgetItem(str(event.category_id))
            description = QTableWidgetItem(event.description)
            self.table.setItem(index,0,date)
            self.table.setItem(index,1,time)
            self.table.setItem(index,2,title)
            self.table.setItem(index,3,cat)
            self.table.setItem(index,4,description)

            