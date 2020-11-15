def print_list(a_list):
    for i in range(1, len(a_list)): # The function does not work properly because the range should be from 0 to len of a_list, because lists start at 0, not 1
        print('Element {} = {}'.format(str(i), str(a_list[i])))

if __name__ == '__main__':
    a_list = [1, 2, 3, 5, 7, 9]
    print_list(a_list)