#!/usr/bin/env python3
# coding=utf-8

import math

try:
    a = float(input("Введите A="))
    b = float(input("Введите B="))
    x = float(input("Введите X="))
    try:
        if (x < 7):
            y = (math.pow(x, 2) + math.pow(a, 2) + math.pow(b, 2))/(a + b)
        else:
            y = math.pow(x, 3) * math.pow((a + b), 2)
        print('Ответ: ', y)
    except:
        print("Ошибка!")
except:
    print("Неверные входные данные!")
input("Нажмите Enter для выхода")