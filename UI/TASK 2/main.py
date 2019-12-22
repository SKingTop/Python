# !/usr/bin/env python3
# coding=utf-8

import sys
import math

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Создание простейшей визуальной '
                            'программы на Python')

        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        self.label_img.setPixmap(QPixmap('main.jpg'))
        self.label_img.setScaledContents(True)

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.close)

    def solve(self):
        a = self.lineEdit_a.text()
        b = self.lineEdit_b.text()
        d = self.lineEdit_d.text()
        x = self.lineEdit_x.text()

        try:
            a = float(a)
            b = float(b)
            d = float(d)
            x = float(x)

            if x < 6:
                y = math.pow((a + b), 2) / (x - 2)
            else:
                y = x * math.pow(d, 3) + math.pow(b, 2)
            self.label_answer.setText('Ответ: ' + str(format(y, '.2f')))
        except:
            self.label_answer.setText('Ошибка!')

    def clear(self):
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')
        self.lineEdit_x.setText('')
        self.lineEdit_d.setText('')
        self.label_answer.setText('Ответ: ')

def main():
    # каждое приложение должно создать объект QApplication
    # sys.argv - список аргументов командной строки
    app = QApplication(sys.argv)
    window = Main()  # базовый класс для всех объектов интерфейса пользователя
    window.show()  # отобразить окно на экране
    sys.exit(app.exec_())  # запуск основного цикла приложения


if __name__ == '__main__':
    main()