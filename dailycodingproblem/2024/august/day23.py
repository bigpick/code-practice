#!/usr/bin/env python

# Given an array of intergers, return a new array such thath each element at index i
# of the new array is the product of all the numbers in the original array exccept
# the one at i
from math import prod

TEST_CASES =[
    ([1,2,3,4,5], [120,60,40,30,24]),
    ([3,2,1], [2,3,6]),
]

def array_products(input_list: list[int]):
    tot = prod(input_list)
    return [int(tot/x) for x in input_list]

def array_products_no_div(input_list: list[int]):
    new_list = []
    for idx in range(len(input_list)):
        left = input_list[:idx]
        right = input_list[idx+1:]
        new_list.append(prod([*left, *right]))
    return new_list


for test_case in TEST_CASES:
    assert array_products(test_case[0]) == array_products_no_div(test_case[0]) == test_case[1]
