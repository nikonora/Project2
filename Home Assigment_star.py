#Напишіть функцію Python filter_and_sum_squares, яка приймає список чисел і повертає суму квадратів парних чисел у списку.
#Функція має використовувати filter для вибору парних чисел, map для їх зведення в квадрат і reduce для підсумовування квадратів.
#Ось приклад того, як має працювати функція:

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#result = filter_and_sum_squares(numbers)
#print(result) # 220  (4**2 + 6**2 + 8**2 + 10**2)

from functools import reduce

def filter_and_sum_squares(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers1 = list(filter(lambda is_ever: is_ever % 2 == 0, numbers))
numbers2 = list(map(lambda square: square ** 2 , numbers1))
result = reduce(filter_and_sum_squares, numbers2)
print(result)