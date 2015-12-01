from __future__ import division
import random
import numpy as np

class MaxHeap(object):
    def __init__(self):
        self.array = []

    def parent_index(self, index):
        return int((index-1)/2)

    def children_indices(self, index):
        return filter(lambda x: len(self.array) > x,
                      [2 * index + 1, 2 * index + 2])

    def swap(self, index1, index2):
        self.array[index1], self.array[index2] =  self.array[index2], self.array[index1]

    def percolate_up(self, index):

        if index == 0:
            return

        parent_index = self.parent_index(index)
        parent = self.array[parent_index]
        current = self.array[index]

        if current <= parent:
            return
        self.swap(index, parent_index)

        self.percolate_up(parent_index)

    def percolate_down(self, index):
        children_indices =  self.children_indices(index)
        children = [self.array[child] for child in children_indices]
        if len(children) == 0 or self.array[index] >= max(children):
            return
        max_index = children_indices[np.argmax(children)]
        self.swap(index, max_index)
        self.percolate_down(max_index)

    def push(self, elem):
        index = len(self.array)
        self.array.append(elem)
        self.percolate_up(index)

    def peek(self):
        if len(self.array) == 0:
            return None
        return self.array[0]

    def pop(self):
        value = self.peek()
        if len(self.array) == 1:
            return self.pop()
        if value is not None:
            self.array[0] = self.array.pop()
            self.percolate_down(0)
        return value

    def populate(self, n):
        for _ in range(n):
            self.push(random.randint(-10*n,10*n))
        return self

    def populate_from_list(self, l):
        for _ in range(n):
            self.push(random.randint(-10*n,10*n))
