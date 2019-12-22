import random

def random_array(n, m, max_value=100):
    array = []
    for i in range(0, n):
        sub_array = []
        for j in range(m):
            number = random.randint(0, max_value)
            sub_array.append(number)
        array.append(sub_array)
    return array


def print_array(array):
    print()
    for i in array:
        for j in i:
            print("%5d\t" % j, end='')
        print()


def main():
    array = random_array(4, 5)
    print_array(array)
    while True:
        print()
        print("Имеется двумерный массив 4x5.\nПоменять местами максимальный и минимальный элемент массива,\nесли сумма значений массива больше ста\n\n")
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')
        print()
        if key == '1':
            array = random_array(4, 5)
            print_array(array)
        elif key == '2':
            print("\n--------Выполнение задания--------\n")
            count = 0
            b_max = b_min = array[0][0]
            b_max_row = b_min_row = b_max_col = b_min_col = 0

            for row, r in enumerate(array):
                for col, cell in enumerate(r):
                    count = count + cell;
                    if (cell > b_max):
                        b_max = cell
                        b_max_col = col
                        b_max_row = row
                    if (cell < b_min):
                        b_min = cell
                        b_min_col = col
                        b_min_row = row

            if(count >= 100):
                print("Исходный массив\n")
                print_array(array)
                print()
                print("Максимум исходного массива: ", b_max, "[", b_max_row + 1, "] [", b_max_col + 1, "]")
                print("Минимум исходного массива: ", b_min, "[", b_min_row + 1, "] [", b_min_col + 1, "]")
                array[b_max_row][b_max_col] = b_min
                array[b_min_row][b_min_col] = b_max
                print("\nУсловие выполенно!\n")
                print("Сумма значений массива равна: ", count, "\n")
                print("Новый массив")
                print_array(array)
                print()
                print("Максимум нового массива: ", b_max, "[", b_min_row + 1, "] [", b_min_col+ 1, "]")
                print("Минимум нового массива: ", b_min, "[", b_max_row + 1, "] [", b_max_col + 1, "]")
            else:
                print("Условие не выполненно!")
                print()
                print("Значение " , count , "меньше чем 100")

            print("\n----------Конец задания----------\n")
            print("Press Enter to exit...")
            input()

            break  # выход из цикла
        elif key == '3':
            exit(0)


if __name__ == '__main__':
    main()