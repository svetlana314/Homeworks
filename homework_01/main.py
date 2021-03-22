"""
Домашнее задание №1
Функции и структуры данных
"""
import math

def power_numbers(*num):
    num_list = []
    for n in num:
        num_list.append(n**2)
    return (num_list)
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(num_list, cond):
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
        return True
    if cond == ODD:
        return list(filter(lambda x: x % 2 == 1, num_list))
    elif cond == EVEN:
        return list(filter(lambda x: x % 2 == 0, num_list))
    elif cond == PRIME:
        return list(filter(is_prime, num_list))

    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """