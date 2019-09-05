# practice problems
# from checkIO


# def main():
#     alist = [1, 2, 3, 4]
#     n = 2
#     index_power(alist, n)
#
#
# def index_power(array, n):
#     """
#         Find Nth power of the element with index N.
#     """
#     if n < len(array):
#         calc = 1
#
#         for i in range(n):
#             calc = calc * array[n]
#         print(calc)
#         return calc
#     else:
#         return -1
#
#
# main()


# def main():
#     getCalc(123405)
#
#
# def getCalc(val):
#     total = 1
#     valStr = str(val)
#
#     for i in valStr:
#         if i is not '0':
#             total = total * int(i)
#         print(total)
#
#
# main()


def main():
    text = 'How are you? Eh, ok. Low or Lower? Ohhh.'
    find_message(text)


def find_message(string):
    print(string)


main()
