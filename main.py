import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                                    'описание вкуса', 'цена', 'объем упаковки(г)'])
        self.generation_table()

    def generation_table(self):
        conn = sqlite3.connect("coffee.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM main")
        rows = cursor.fetchall()
        self.tableWidget.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j in range(7):
                value = QTableWidgetItem(str(row[j]))
                self.tableWidget.setItem(i, j, value)
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
