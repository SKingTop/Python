import math
import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main_ui.ui', self)

        self.setWindowTitle('Сложные табличные вычисления в Python')

        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        self.label_img.setPixmap(QPixmap('task.png'))
        self.label_img.setScaledContents(True)

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.exit)

    def fill_random_numbers(self):
        i = 0
        while i < self.tableWidget.rowCount():
            random_num = randint(0, 101)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(random_num)))
            i += 1

    def solve(self):
        if validation_of_data(self.tableWidget):
            i = 0
            j = 1

            while i < self.tableWidget.rowCount():
                item = self.tableWidget.item(i, 0).text()
                try:
                    Ki = int(item)
                    Ki_minus_1 = int(self.tableWidget.item(i - 1, 0).text())
                    sin_Ki = math.sin(Ki)
                    sin_Ki_kvadrat = math.sin(math.pow(Ki, 2))
                    factorial_I = math.factorial(i)
                    cos_3_Ki_minus_1 = (3 * math.cos(Ki_minus_1) + math.cos(3 * Ki_minus_1)) / 4

                    answer = format(
                        (math.sqrt(sin_Ki_kvadrat / factorial_I) + (math.tan(cos_3_Ki_minus_1) / (3.5 * sin_Ki))), ".5f")

                    self.tableWidget.setItem(i, j,
                                             QTableWidgetItem(str(answer)))
                except Exception:
                    self.tableWidget.setItem(i, j, QTableWidgetItem('none'))

                i += 1

            self.label_error.setText('')
        else:
            self.label_error.setText('Введены некорректные данные!')

    def clear(self):
        self.tableWidget.clearContents()

    def exit(self):
        self.close()


def validation_of_data(table_widget):
    i = 0
    while i < table_widget.rowCount():
        try:
            float(table_widget.item(i, 0).text())
            i += 1
        except Exception:
            return False

    return True


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()