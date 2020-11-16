Task 2
Why does print_list() not correctly print out the elements a_list?

def print_list(a_list):
    for i in range(1, len(a_list)):
        print('Element {} = {}'.format(str(i),str(a_list[i])))


a_list = [1, 2, 3, 5, 7, 9]
print_list(a_list)

Added a comment to the part of the script that has an error in it, which causes the print funtion to not work properly