# A sorted array has been rotated so that the elements might appear in the order 3 4 5 6 7 1 2.
# How would you find the minimum element? You may assume that the array has all unique elements.

from math import ceil

def min_in_sorted_rotated(a):
    len = a.__len__()
    if len == 1:
        return a[0]
    elif len == 2:
        return min(a[0],a[1])
    else:
        mid = ceil(len/2)
        if a[0] > a[mid-1]:
            return min_in_sorted_rotated(a[:mid])
        else:
            return min_in_sorted_rotated(a[mid:])
