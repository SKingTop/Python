import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

list_of_numbers = []


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main_ui.ui', self)

        self.setWindowTitle('Работа с массивами и файлами в Python')
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))

        self.btn_upload_data.clicked.connect(self.upload_data_from_file)
        self.btn_process_data.clicked.connect(self.process_data)
        self.btn_save_data.clicked.connect(self.save_data_in_file)
        self.btn_clear.clicked.connect(self.clear)

    def upload_data_from_file(self):
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '',
                                                   "Text Files (*.txt)")[0]

        if path_to_file:
            file = open(path_to_file, 'r')

            data = file.read()
            self.plainTextEdit.appendPlainText("Полученные данные: \n" +
                                               data + "\n")

            global list_of_numbers, array_of_numbers
            list_of_numbers = []
            array_of_numbers = []
            # \b -- ищет границы слов
            # [0-9] -- описывает что ищем
            # + -- говорит, что искать нужно минимум от 1 символа
            for num in re.findall(r'\b[0-9]+\b', data):
                list_of_numbers.append(num)

            for index,value in enumerate(list_of_numbers):
                if index % 5:

    def process_data(self):
        if validation_of_data():
            min_num, min_pos = find_min()
            # if(min_pos):

        else:
            self.plainTextEdit.appendPlainText("Неправильно введены данные! "
                                               "Таблица должна быть размером "
                                               "5х6 и состоять из чисел! \n")

    def save_data_in_file(self):

        if path_to_file:
            file = open('output.txt', 'w')

            for i in list_of_numbers:
                file.write(i + " ")
                if int(i) % 6 == 0:
                    file.write("\n")

            file.close()

            self.plainTextEdit.appendPlainText(
                "Файл был успешно загружен! \n")
        else:
            self.plainTextEdit.appendPlainText("Для начала загрузите файл!")

    def clear(self):
        self.plainTextEdit.clear()


def find_min():
    state = False
    min_num = int(list_of_numbers[0])
    count = 1
    min_pos = 0
    for i in list_of_numbers:
        if min_num > int(i):
            min_num = int(i)
            min_pos = count
        count += 1

    if (min_pos == 2 or min_pos == 8 or min_pos == 14 or min_pos == 20 or min_pos == 26):
        state = True

    return [min_num, state]


def validation_of_data():

    if len(list_of_numbers) == 30:
        for i in list_of_numbers:
            try:
                float(i)
            except Exception:
                return False

        return True
    else:
        return False


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()