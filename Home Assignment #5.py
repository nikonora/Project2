# MAP #

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))

# 1. Сконвертуйте лист градусів у Цельсіях до Фаренгейтів. (Лист [0, 10, 20, 30, 40]).
# Формула для обчислення: (c * 9/5) + 32

def fahren(c):
    return (c * 9 / 5) + 32

gradus = [0, 10, 20, 30, 40]
fahr = map(fahren, gradus)
print(list(fahr))


# 2. Порахуйте довжину кожної строки (Лист ['apple', 'banana', 'orange', 'kiwi'])

def length(s):
    return len(s)

list1 = ['apple', 'banana', 'orange', 'kiwi']
list2 = map(length, list1)
print(list(list2))


# 3. Сконвертуйте лист строк у верхній регістр (Лист ['hello', 'world', 'python', 'programming'])

def up_reg(w):
    return str.upper(w)

a = ['hello', 'world', 'python', 'programming']
upper = map(up_reg, a)
print(list(upper))


# FILTER #

def is_ever(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_ever, numbers)
print(list(even_numbers))

# 1. Відфельтруйте слова, довжина яких менша за 5 (Лист ['apple', 'banana', 'orange', 'kiwi', 'grape'])

def word_len(x):
    return len(x) >= 5

words = ['apple', 'banana', 'orange', 'kiwi', 'grape']
filt_word = filter(word_len, words)
print(list(filt_word))


# 2. Відфельтруйте пусті строки (Лист ['hello', '', 'world', 'python', '', 'programming'])

def full_str(x):
    return len(x) > 0

list_str = ['hello', '', 'world', 'python', '', 'programming']
filt_str = filter(full_str, list_str)
print(list(filt_str))


# 3. Відфельтруйте слова, що НЕ починаються з літери ‘a’ (Лист ['apple', 'banana', 'orange', 'kiwi', 'grape', 'avocado'])

def dif_words(x):
    return x[0] != 'a'

list_words = ['apple', 'banana', 'orange', 'kiwi', 'grape', 'avocado']
filt_dif = filter(dif_words, list_words)
print(list(filt_dif))


# REDUCE #

from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
product = reduce(multiply, numbers)
print(product)

# 1. Порахуйте сумму елементів (Лист [1, 2, 3, 4, 5])

def summ(x, y):
    return x + y

numbers1 = [1, 2, 3, 4, 5]
product1 = reduce(summ, numbers1)
print(product1)


# 2. Знайдіть найбільший елемент (Лист [23, 12, 56, 34, 78, 9, 67])

def max_number(x, y):
    return max(x, y)

list_numbers = [23, 12, 56, 34, 78, 9, 67]
des_number = reduce(max_number, list_numbers)
print(des_number)


# 3. Зробіть одну строку (з пробілами) з листу строк (Лист ['hello', 'world', 'python', 'programming'])

def word_4(x, y):
    return x + " " + y

list_w = ['hello', 'world', 'python', 'programming']
des_str = reduce(word_4, list_w)
print(des_str)


# LAMBDA FUNCTIONS #

def is_positive(num):
    return num >= 0

numbers = [-1, 2, -3, 4, -5]
positive_numbers = filter(is_positive, numbers)
print(list(positive_numbers))


numbers = [-1, 2, -3, 4, -5]
positive_numbers = filter(lambda num: num >= 0, numbers)
print(list(positive_numbers))



def fah(c):
    return (c * 9 / 5) + 32

celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(fah, celsius))
result = map(lambda grad: grad / 5, fahrenheit)
print(list(result))
