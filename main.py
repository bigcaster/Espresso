import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.loadTable()

    def loadTable(self):
        con = sqlite3.connect('coffee.db')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM info""").fetchall()
        title = ['ID', 'Название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса',
                 'цена', 'объем упаковки']
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        for i, line in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            id, name, degree, type, description, price, volume = line
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(id)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(name))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(degree))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(type))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(description))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(volume))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
