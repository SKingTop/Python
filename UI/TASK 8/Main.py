import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView

answers = ['', '', '']

class Form1(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form1, self).__init__()
        uic.loadUi('uis/form1.ui', self)

        self.setWindowTitle('Приветсвтие')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_exit.clicked.connect(self.close)
        self.btn_begin.clicked.connect(self.next)

    def next(self):
        self.switch_window.emit('1>2')

class Form2(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form2, self).__init__()
        uic.loadUi('uis/form2.ui', self)
        answers[0] = ''

        self.setWindowTitle('Детство')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.label_img.setPixmap(QPixmap('images/toys.png'))
        self.label_img.setScaledContents(True)

        self.comboBox.activated.connect(self.handleActivated)
        self.btn_back.clicked.connect(self.back)
        self.btn_next.clicked.connect(self.next)

    def handleActivated(self, index):
        answers[0] = self.comboBox.itemText(index)
        self.label_selected.setText('Выбрано: ' + answers[0])
        if(answers[0] != ''):
            self.btn_next.setEnabled(True)

    def back(self):
        self.switch_window.emit('1<2')

    def next(self):
        self.switch_window.emit('2>3')

class Form3(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form3, self).__init__()
        uic.loadUi('uis/form3.ui', self)
        answers = [1]

        self.setWindowTitle('Отрочество')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.label_img.setPixmap(QPixmap('images/school.png'))
        self.label_img.setScaledContents(True)

        self.radioButton_1.toggled.connect(
            lambda: self.onToggled(self.radioButton_1))
        self.radioButton_2.toggled.connect(
            lambda: self.onToggled(self.radioButton_2))
        self.radioButton_3.toggled.connect(
            lambda: self.onToggled(self.radioButton_3))
        self.radioButton_4.toggled.connect(
            lambda: self.onToggled(self.radioButton_4))

        self.btn_back.clicked.connect(self.back)
        self.btn_next.clicked.connect(self.next)

    def onToggled(self, radiobutton):
        if radiobutton.isChecked():
            answers[1] = radiobutton.text()
            self.label_selected.setText('Выбрано: ' + answers[1])
        if (answers[1] != ''):
            self.btn_next.setEnabled(True)

    def back(self):
        self.switch_window.emit('2<3')

    def next(self):
        self.switch_window.emit('3>4')


class Form4(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form4, self).__init__()
        uic.loadUi('uis/form4.ui', self)
        answers[2] = ''

        self.setWindowTitle('Отрочество')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.label_img.setPixmap(QPixmap('images/hobby.png'))
        self.label_img.setScaledContents(True)

        self.checkBox_1.clicked.connect(self.item_click)
        self.checkBox_2.clicked.connect(self.item_click)
        self.checkBox_3.clicked.connect(self.item_click)
        self.checkBox_4.clicked.connect(self.item_click)
        self.btn_back.clicked.connect(self.back)
        self.btn_next.clicked.connect(self.next)

    def item_click(self):
        sub_array = []
        count = 0
        if(self.checkBox_1.isChecked()):
            value = self.checkBox_1.text()
            sub_array.append(value)
            count += 1
        if (self.checkBox_2.isChecked()):
            value = self.checkBox_2.text()
            sub_array.append(value)
            count += 1
        if (self.checkBox_3.isChecked()):
            value = self.checkBox_3.text()
            sub_array.append(value)
            count += 1
        if (self.checkBox_4.isChecked()):
            value = self.checkBox_4.text()
            sub_array.append(value)
            count += 1
        answers[2] = sub_array
        if(count == 1):
            self.label_selected.setText('Выбрано: ' + sub_array[0])
        if (count == 2):
            self.label_selected.setText('Выбрано: ' + sub_array[0] + ', ' + sub_array[1])
        if (count == 3):
            self.label_selected.setText('Выбрано: ' + sub_array[0] + ', ' + sub_array[1] + ', ' + sub_array[2])
        if (count == 4):
            self.label_selected.setText('Выбрано: ' + sub_array[0] + ', ' + sub_array[1] + ', ' + sub_array[2] + ', ' + sub_array[3])
        if (answers[2] != ''):
            self.btn_next.setEnabled(True)

    def back(self):
        self.switch_window.emit('3<4')

    def next(self):
        self.switch_window.emit('4>5')

class Form5(QtWidgets.QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Form5, self).__init__()
        uic.loadUi('uis/form5.ui', self)

        self.setWindowTitle('Результат')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        # запрещаем редактирование таблицы
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # присваиваем значение ячейкам таблицы
        self.tableWidget.setItem(0, 0,
                                 QTableWidgetItem('Любимая игрушка'))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(answers[0]))

        self.tableWidget.setItem(1, 0,
                                 QTableWidgetItem('Любимый предмет'))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(answers[1]))

        self.tableWidget.setItem(2, 0,
                                 QTableWidgetItem('Какое(-ие) у вас хобби'))
        hobby = ''
        sub_array = answers[2]
        if (len(sub_array) == 1):
            hobby = sub_array[0]
        if (len(sub_array) == 2):
            hobby = sub_array[0] + ', ' + sub_array[1]
        if (len(sub_array) == 3):
            hobby = sub_array[0] + ', ' + sub_array[1] + ', ' + sub_array[2]
        if (len(sub_array) == 4):
            hobby = sub_array[0] + ', ' + sub_array[1] + ', ' + sub_array[2] + ', ' + sub_array[3]

        self.tableWidget.setItem(2, 1, QTableWidgetItem(hobby))

        self.btn_back.clicked.connect(self.back)
        self.btn_exit.clicked.connect(self.close)

    def back(self):
        self.switch_window.emit("4<5")

class Controller:
    def __init__(self):
        pass

    def select_forms(self, text):
        if text == '1':
            self.form1 = Form1()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()

        if text == '1>2':
            self.form2 = Form2()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form1.close()

        if text == '2>3':
            self.form3 = Form3()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form2.close()

        if text == '3>4':
            self.form4 = Form4()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form3.close()

        if text == '4>5':
            self.form5 = Form5()
            self.form5.switch_window.connect(self.select_forms)
            self.form5.show()
            self.form4.close()

        if text == '4<5':
            self.form4 = Form4()
            self.form4.switch_window.connect(self.select_forms)
            self.form4.show()
            self.form5.close()

        if text == '3<4':
            self.form3 = Form3()
            self.form3.switch_window.connect(self.select_forms)
            self.form3.show()
            self.form4.close()

        if text == '2<3':
            self.form2 = Form2()
            self.form2.switch_window.connect(self.select_forms)
            self.form2.show()
            self.form3.close()

        if text == '1<2':
            self.form1 = Form1()
            self.form1.switch_window.connect(self.select_forms)
            self.form1.show()
            self.form2.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.select_forms("1")
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
