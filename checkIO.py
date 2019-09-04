

def main():
    alist = [1, 2, 3]
    n = 2
    index_power(alist, n)


def index_power(my_list, n):
    """
        Find Nth power of the element with index N.
    """
    list_length = len(my_list)
    if list_length > 0:
        calc = 0
        print(my_list[n])
        for i in my_list:
            #print('11')
            calc = calc * my_list[n]
        return calc
    else:
        return -1


main()