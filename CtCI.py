# Numbers are randomly generated and stored into an (expanding) array.
# How would you keep track of the median?
# Answer: use a max heap and min heap for the bottom/top half of the numbers.
# The roots of the heaps are the "two" medians, and their avg is the median
from math import floor
class Heap: # heap with 1-based index
    def __init__(self, type):
        self.vals = []
        if type == 'Max':
            self.comparator = lambda x, y: x > y
        elif type == 'Min':
            self.comparator = lambda x, y: x < y
        else:
            print('Invalid heap type')
    def len(self):
        return self.vals.__len__()
    def empty(self):
        return self.len() == 0
    def get(self, index):
        return self.vals[index-1]
    def get_root(self):
        if not self.empty():
            return self.get(1)
        else:
            return None
    def get_vals(self):
        return [self.get(index) for index in range(1, self.len()+1)]
    def set(self, index, val):
        self.vals[index-1] = val
    def add(self, val):
        self.vals.append(val)
        self.bubble_up(self.len())
    def swap(self, index1, index2):
        temp = self.get(index1)
        self.set(index1, self.get(index2))
        self.set(index2, temp)
    def delete(self, index):
        del self.vals[index-1]
    def delete_last(self):
        self.delete(self.len())
    def isleaf(self, index):
        len = self.len()
        left_child_index = index * 2
        right_child_index = left_child_index + 1
        return ((right_child_index > len) and (left_child_index > len))
    def bubble_up(self, index):
        cur_index = index
        done = False
        while (cur_index > 1) and (not done): # bubble element at index up through the heap
            par_index = floor(cur_index/2) # parent of current node
            if self.comparator(self.get(cur_index), self.get(par_index)):
                # swap cur & par, and continue up the heap
                self.swap(cur_index, par_index)
                cur_index = par_index
            else:
                # cur is at its proper place in heap, no need to go higher
                done = True
    def compare(self, a, b):
        return self.comparator(self.get(a), self.get(b))
    def pop_root(self):
        len = self.len() # by the end we will have one fewer node in the heap (if non-empty)
        if len == 0:
            return None
        elif len == 1:
            # delete and return root
            rootVal = self.get_root()
            self.delete(1)
            return rootVal
        else: # heap has at least one node below root, so bubble down hole left at to-be-popped root
            rootVal = self.get_root() # save root val to return at the very end
            hole_index = 1 # this is the hole (1-based index) that needs to be bubbled all the way down
            self.set(hole_index, None)
            while (not self.isleaf(hole_index)):
                hole_left_child_index = hole_index * 2
                hole_right_child_index = hole_left_child_index + 1
                if ((hole_right_child_index <= len) and
                    self.compare(hole_right_child_index, hole_left_child_index)):
                    # hole has right child and it is the max/min, so bubble it up into the hole and continue down
                    next_hole_index = hole_right_child_index
                else:
                    # else bubble up the left child into the hole and continue down
                    next_hole_index = hole_left_child_index
                # swap hole and climber
                self.swap(hole_index, next_hole_index)
                hole_index = next_hole_index

            # hole is leaf now. if hole is not last heap element, move last heap element into hole and bubble up
            if not(hole_index == len):
                self.swap(hole_index, len)
                self.bubble_up(hole_index)
            # delete last heap element
            self.delete_last()
            # return popped root val
            return rootVal

# Design an algorithm to print all permutations of a string.
# For simplicity, assume all characters are unique.
from functools import reduce
def all_permutations(s): # s is a string
    len = s.__len__()
    if len == 0:
        return []
    elif len == 1:
        return [s[0]]
    else:
        first = s[0]
        rest_permutations = all_permutations(s[1:])
        return reduce(lambda l1, l2: l1+l2, [insert_throughout(first, perm) for perm in rest_permutations])

def insert_throughout(l, s): # l is a letter, s is a string
    len = s.__len__()
    if len == 0:
        return [l]
    else:
        return [s[0:i]+l+s[i:len] for i in range(len+1)]

# A sorted array has been rotated so that the elements might appear in the order 3 4 5 6 7 1 2.
# How would you find the minimum element? You may assume that the array has all unique elements.
from math import ceil
def min_in_sorted_rotated(a): # a is a sorted rotated array of unique numbers
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
