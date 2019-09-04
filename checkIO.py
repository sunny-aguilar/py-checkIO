

def main():
    alist = [1, 2, 3]
    n = 3
    index_power(alist, n)


main()


def index_power(list, n):
    """
        Find Nth power of the element with index N.
    """
    listLength = len(list)
    if listLength > 0:
        calc = 0
        for i in list:
            calc *= list[n]

    else:
        return -1


