
def index_power(array: list, n: int) -> int:
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


