"""
A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the
power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
For example, take 153 (3 digits), which is narcissistic:
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:
    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
The Challenge:
Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic
number in base 10. This may be True and False in your language, e.g. PHP.
Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be
passed into the function.
"""
import math

import codewars_test as test
import numpy as numpy


def narcissistic(value):
    result = 0
    for i in str(value):
        result += int(i) ** len(str(value))
    if result == value:
        return True
    else:
        return False


test.assert_equals(narcissistic(7), True, '7 is narcissistic')
test.assert_equals(narcissistic(371), True, '371 is narcissistic')
test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')

"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special 
characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet 
should be shifted, like in the original Rot13 "implementation".
Please note that using encode is considered cheating.
"""


# Можно решить через ord() и char()
def rot13(message):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for word in message:
        for letter in word:
            if letter in abc:
                result += abc[(abc.find(letter) + 13) % 26]
            elif letter in ABC:
                result += ABC[(ABC.find(letter) + 13) % 26]
            else:
                result += letter
    return result


test.assert_equals(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
test.assert_equals(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
test.assert_equals(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%',
                   'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')

"""
You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the 
integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make 
this happen, return -1.
For example:
Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index
 ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.
"""


def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[0:i]) == sum(arr[i + 1:]):
            return i
    return -1


test.assert_equals(find_even_index([1, 2, 3, 4, 3, 2, 1]), 3)
test.assert_equals(find_even_index([1, 100, 50, -51, 1, 1]), 1, )
test.assert_equals(find_even_index([1, 2, 3, 4, 5, 6]), -1)
test.assert_equals(find_even_index([20, 10, 30, 10, 10, 15, 35]), 3)
test.assert_equals(find_even_index([20, 10, -80, 10, 10, 15, 35]), 0)
test.assert_equals(find_even_index([10, -80, 10, 10, 15, 35, 20]), 6)
test.assert_equals(find_even_index(list(range(1, 100))), -1)
test.assert_equals(find_even_index([0, 0, 0, 0, 0]), 0, "Should pick the first index if more cases are valid")
test.assert_equals(find_even_index([-1, -2, -3, -4, -3, -2, -1]), 3)
test.assert_equals(find_even_index(list(range(-100, -1))), -1)

"""
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total 
time required for all the customers to check out!
input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is 
the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.
"""


# Плохое решение

def queue_time(customers, n):
    if len(customers) == 0:
        return 0
    elif n < len(customers):
        while len(customers) != n:
            min_queue = customers[:n].index(min(customers[:n]))
            customers[min_queue] += customers[n]
            del customers[n]
        return max(customers)
    else:
        return max(customers)


test.assert_equals(queue_time([], 1), 0, "wrong answer for case with an empty queue")
test.assert_equals(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
test.assert_equals(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
test.assert_equals(queue_time([1, 2, 3, 4, 5], 1), 15, "wrong answer for a single till")
test.assert_equals(queue_time([1, 2, 3, 4, 5], 100), 5, "wrong answer for a case with a large number of tills")
test.assert_equals(queue_time([2, 2, 3, 3, 4, 4], 2), 9, "wrong answer for a case with two tills")


"""
For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, 
which is a utility class helpful for querying paging information related to an array.
The class is designed to take in an array of values and an integer indicating how many items will be 
allowed per each page. The types of values contained within the collection/array are not relevant.
"""

class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return math.ceil(len(self.collection) / self.items_per_page)

    def page_item_count(self, page_index):

        if page_index > self.page_count() - 1:
            return -1
        elif page_index == self.page_count() - 1:
            return self.item_count() - page_index * self.items_per_page
        else:
            return self.items_per_page

    def page_index(self, item_index):
        page = 0
        if self.item_count() - 1 < item_index or item_index < 0:
            return -1
        else:
            while item_index > self.items_per_page:
                item_index -= self.items_per_page
                page += 1
        return page


collection = range(1, 25)
helper = PaginationHelper(collection, 10)

test.assert_equals(helper.page_count(), 3, 'page_count is returning incorrect value.')
test.assert_equals(helper.page_index(23), 2, 'page_index returned incorrect value')
test.assert_equals(helper.item_count(), 24, 'item_count returned incorrect value')
test.assert_equals(helper.page_item_count(2), 4, 'item_count returned incorrect value')
