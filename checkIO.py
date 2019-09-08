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


# def main():
#     array = []
#     checkio(array)
#
#
# def checkio(array):
#     if len(array) > 0:
#         last = array[-1]
#         total = 0
#         for i in range(len(array)):
#             if i % 2 == 0:
#                 total = total + array[i]
#         total = total * last
#         return total
#     else:
#         return 0
#
#
# main()


# def main():
#     data = {'CAC': 10.0, 'ATX': 390.2, 'WIG': 1.2}
#     best_stock(data)
#
# def best_stock(data):
#     price = 0
#     stock = ''
#
#     for i in data:
#         if data[i] > price:
#             price = data[i]
#             stock = i
#     return stock
#
#
# main()


# def main():
#     text = "hello, Sandro"
#     correct_sentence(text)


# def correct_sentence(text):
#     new_str = ''
#
#     for i in range(len(text)):
#         new_str += text[i]
#
#         if i == 0:
#             if text[0] is not text[0].isupper():
#                 r = text[0]
#                 new_str = r.upper()
#
#         if i == len(text) - 1:
#             if text[-1] is not '.':
#                 new_str += '.'
#
#     return new_str
#
#
# main()


def main():
    phrases = 'left, right, left, stop'
    left_join(phrases)


def left_join(phrases):
    print(phrases.replace("right", "left"))


main()


