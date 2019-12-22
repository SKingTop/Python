import math
from random import randint


def random_array(max_value=100):
    array = []
    for i in range(0, 10):
        array.append([randint(0, max_value), 0])
    return array


def print_array(array):
    print()

    for i in array:

        for j in i:
            print("%.15s\t" % j, end='')
        print()

def main():
    array = random_array()
    print_array(array)
    while True:
        print()
        print("1. Обновить массив")
        print("2. Выполнить задание")
        print("3. Выход")
        key = input('Введите команду: ')
        if key == '1':
            array = random_array()
            print_array(array)
        elif key == '2':
            print()

            for i in range(0, 10):
                if (i - 1) < 0:
                    answer = 'Ki-1 not found'
                    array[i][1] = answer
                else:
                    a = b = 0.0
                    Ki = array[i][0]
                    KI = array[i - 1][0]
                    try:
                        a = math.sqrt((math.sin(math.pow(Ki, 2)))/(math.factorial(i)))
                        b = (math.tan((3 * math.cos(KI) + math.cos(3 * KI)) / 4)) / (3.5 * math.sin(Ki))
                        answer = a + b
                        array[i][1] = answer
                    except:
                        array[i][1] = 'no answer'
                        continue
            print_array(array)
        elif key == '3':
            exit(0)

if __name__ == '__main__':
    main()