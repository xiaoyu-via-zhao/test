#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:04:26 2019

@author: xiaoyuzhao
"""


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print (quicksort([3,6,8,10,1,2,1]))


arr = [3,6,8,10,1,2,1]
print (arr)
pivot  = arr [len(arr)//2]
print


