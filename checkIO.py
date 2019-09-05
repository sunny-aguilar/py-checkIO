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


# def main():
#     text = 'How are you? Eh, ok. Low or Lower? Ohhh.'
#     text2 = 'hello world!'
#     text3 = 'HELLO WORLD!!!'
#
#     find_message(text3)
#
#
# def find_message(string):
#     message = ''
#     for i in string:
#         if i.isupper():
#             message = message + i
#
#     print(message)
#
#
# main()


# def main():
#     number = 7
#     print(checkio(number))
#
#
# def checkio(number):
#     phrase = ''
#     if (number % 3) == 0 and (number % 5) == 0:
#         phrase = 'Fizz Buzz'
#     elif (number % 3) == 0:
#         phrase = 'Fizz'
#     elif (number % 5) == 0:
#         phrase = 'Buzz'
#     else:
#         phrase = str(number)
#
#     return phrase
#
#
# main()


def main():
    array = [0, 1, 2, 3, 4, 5]
    checkio(array)


def checkio(array):
    last = array[-1]
    total = 0
    
    for i in range(len(array)):
        if i % 2 == 0:
            total = total + array[i]
    total = total * last

    return total


main()



