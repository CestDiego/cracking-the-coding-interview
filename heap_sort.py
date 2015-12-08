from heap import MaxHeap

def heap_sort(l):
    heap = MaxHeap()
    heap.populate_from_list(l)
    return [heap.pop() for _ in l]
