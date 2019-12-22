#Если минимальный элемент стоит во втором столбце
#то заменить элементы второго столбца нулями

def read_file(filename):
    in_file = open(filename, 'r')
    array = []
    for line in in_file:
        sub_array = []
        str_nums = line.split(' ')
        for sn in str_nums:
            sub_array.append(int(sn))
        array.append(sub_array)
    return array


def write_file(filename, array):
    out_file = open(filename, 'w')
    for row in array:
        for num in row:
            out_file.write("%d " % num)
        out_file.write('\n')


def main():
    array = read_file('input.txt')
    min_value = array[0][0]
    min_value_col = 0
    for row in array:
        col_index = 0
        for col in row:
            if(col < min_value):
                min_value = col
                min_value_col = col_index
            col_index += 1

    if(min_value_col == 1):
        print("Условие выполненно!")
        for row in array:
            row[1] = 0
    else:
        print("Условие не выполненно!")

    write_file('output.txt', array)


if __name__ == '__main__':
    main()