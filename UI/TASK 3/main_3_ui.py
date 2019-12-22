#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main_3_ui.ui', self)

        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        row = 0
        col = 0

        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 101)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                item = self.tableWidget.item(row, col).text()
                col += 1
            row += 1
            col = 0

        # находим максимальное и минимальное число и его координаты
        # а также считаем сумму всех элементов
        # [0] - максимальное число, [1] - строка максимума, [2] - столбец максимума
        list_information_max_num = find_max(self.tableWidget)
        list_information_min_num = find_min(self.tableWidget)
        element_summ_count  = summ_calc(self.tableWidget)

        if not list_information_max_num or not list_information_min_num or  not element_summ_count:
            self.label_error.setText('Введены некорректные данные!')
        else:
            # выводим на экран информацию о расположении максимального и минимального числа
            # а также значение суммы всех элементов массива
            self.label_max_el.setText(
                'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1] + 1) + ';' + str(list_information_max_num[2] + 1) + ']')
            # выводим на экран информацию о расположении минимального числа
            self.label_min_el.setText(
                'Минимальный элемент: ' + str(list_information_min_num[0]) + ' [' +
                str(list_information_min_num[1] + 1) + ';' + str(list_information_min_num[2] + 1) + ']')
            self.label_sum.setText("Сумма элементов: " + str(element_summ_count))

        if(element_summ_count > 100):
            self.btn_solve.setEnabled(True)
        else:
            self.btn_solve.setEnabled(False)

    def solve(self):
        list_information_max_num = find_max(self.tableWidget)
        list_information_min_num = find_min(self.tableWidget)
        element_summ_count = summ_calc(self.tableWidget)

        if not list_information_max_num or not list_information_min_num or  not element_summ_count:
            self.label_error.setText('Введены некорректные данные!')
        else:
            self.label_max_el.setText(
                'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1] + 1) + ';' + str(list_information_max_num[2] + 1) + ']')
            self.label_min_el.setText(
                'Минимальный элемент: ' + str(list_information_min_num[0]) + ' [' +
                str(list_information_min_num[1] + 1) + ';' + str(list_information_min_num[2] + 1) + ']')
            self.label_sum.setText("Сумма элементов: " + str(element_summ_count))

            # -*- решение задания -*-
            self.tableWidget.setItem(list_information_min_num[1], list_information_min_num[2], QTableWidgetItem(str(list_information_max_num[0])))
            self.tableWidget.setItem(list_information_max_num[1], list_information_max_num[2], QTableWidgetItem(str(list_information_min_num[0])))

            self.label_max_el.setText(
                'Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_min_num[1] + 1) + ';' + str(list_information_min_num[2] + 1) + ']')
            # выводим на экран информацию о расположении минимального числа
            self.label_min_el.setText(
                'Минимальный элемент: ' + str(list_information_min_num[0]) + ' [' +
                str(list_information_max_num[1] + 1) + ';' + str(list_information_max_num[2] + 1) + ']')

def find_max(table_widget):

    row_max_number = 0
    col_max_number = 0
    max_num = int(table_widget.item(row_max_number, col_max_number).text())

    row = 0
    col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = int(table_widget.item(row, col).text())
                if number > max_num:
                    max_num = number
                    row_max_number = row
                    col_max_number = col
                col += 1
            row += 1
            col = 0
        return [max_num, row_max_number, col_max_number]
    except Exception:
        return None

def summ_calc(table_widget):
    count = 0

    row = 0
    col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = int(table_widget.item(row, col).text())
                count += int(number)
                col += 1
            row += 1
            col = 0
        return count
    except Exception:
        return None

def find_min(table_widget):

    row_min_number = 0
    col_min_number = 0
    min_num = int(table_widget.item(row_min_number, col_min_number).text())

    row = 0
    col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = int(table_widget.item(row, col).text())
                if number <  min_num:
                    min_num = number
                    row_min_number = row
                    col_min_number = col
                col += 1
            row += 1
            col = 0
        return [min_num, row_min_number, col_min_number]
    except Exception:
        return None

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()