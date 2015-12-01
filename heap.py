from __future__ import division

class MaxHeap(object):
    def __init__(self, size):
        self.array = [None] * size
        self.n     = 0

    def parent_index(self, index):
        return int((index-1)/2)

    def children_index_tuple(self, index):
        return (2 * index + 1, 2 * index + 2)

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

    def push(self, elem):
        self.array[self.n] = elem
        self.percolate_up(self.n)

        self.n += 1