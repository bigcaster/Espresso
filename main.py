import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget
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
            coffee_id, name, degree, coffee_type, description, price, volume = line
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(coffee_id)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(name))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(degree))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(coffee_type))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(description))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(volume))
        self.dialog = Dialog()
        self.pushButton.clicked.connect(self.show_dialog)

    def show_dialog(self):
        self.dialog.show()


class Dialog(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.enter)

    def enter(self):
        inputs = [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4,
                  self.lineEdit_5, self.lineEdit_6, self.lineEdit_7]
        if all(map(lambda s: s.text(), inputs)):
            ex.tableWidget.setRowCount(ex.tableWidget.rowCount() + 1)
            print(ex.tableWidget.rowCount())
            for j, answer in enumerate(inputs):
                print(j, answer.text())
                ex.tableWidget.setItem(ex.tableWidget.rowCount() - 1, j,
                                       QTableWidgetItem(answer.text()))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
