# Numbers are randomly generated and stored into an (expanding) array.
# How would you keep track of the median?
# Answer: use a max heap and min heap for the bottom/top half of the numbers.
# The roots of the heaps are the "two" medians
from math import floor
class Heap:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    def __init__(self, type):
        self.nodes = []
        if type == 'Max':
            self.comparator = lambda x, y: x > y
        elif type == 'Min':
            self.comparator = lambda x, y: x < y
        else:
            print('Invalid heap type')
    def add(self, val):
        self.nodes.append(Heap.Node(val))
        self.rebalance()
    def rebalance(self):
        cur_index = self.nodes.__len__()
        done = False
        while (cur_index > 1) and (not done):
            par_index = floor(cur_index/2)
            if self.comparator(self.nodes[cur_index-1].val, self.nodes[par_index-1].val):
                # swap the two values and continue up the chain
                self.nodes[cur_index-1].val, self.nodes[par_index-1].val = self.nodes[par_index-1].val, self.nodes[cur_index-1].val
                cur_index = par_index
            else:
                done = True
    def vals(self):
        return [self.nodes[i].val for i in range(self.nodes.__len__())]
    def root(self):
        if self.nodes.__len__() != 0:
            return self.nodes[0].val
        else:
            return None
    def pop(self):
        len self.nodes.__len__()
        if len == 0:
            return None
        elif len == 1:
            rootVal = self.nodes[0].val
            del self.nodes[0]
            return rootVal
        else:
            rootVal = self.nodes[0].val # return this at the end
            len = self.nodes.__len__() # by the end we will have one fewer node
            hole_index = 0 # this is the hole that needs to be filled
            while (hole_index < len) and (not done):
                leftChild = 2 * hole_index
                rightChild = leftChild + 1
                if rightChild > len: # hole has no right child
                    if leftChild > len: # hole has no left child either
                        done = True # done with while loop, now fill this hole at the end
                    else: # hole has no right child, but has left child
                        self.nodes[hole_index-1].val = self.nodes[leftChild-1].val
                        hole_index = leftChild
                else: # hole has right child (and therefore also has left child)
                    if (self.comparator(self.nodes[leftChild-1], self.nodes[rightChild-1])):
                        self.nodes[hole_index-1].val = self.nodes[leftChild-1].val
                        hole_index = leftChild
                    else:
                        self.nodes[hole_index-1].val = self.nodes[rightChild-1].val
                        hole_index = rightChild
            # fill hole_index with last element and then rebalance
            self.nodes[hole_index-1].val = self.nodes[len-1].val
            del self.nodes[-1]
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
