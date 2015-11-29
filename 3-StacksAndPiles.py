class StackCapacityExceded(Exception):
    pass

# 3.1
class Stack:

    def __init__(self, capacity=4):
        self._data = []
        self.capacity = capacity

    def pop(self):
        if self.is_empty():
            raise Error("nope")
        poped = self._data[-1]
        self._data.remove(poped)
        return poped

    def peek(self):
        if self.is_empty():
            raise Error("nope")
        return self._data[-1]

    def push(self, elem):
        if len(self._data) == self.capacity:
            raise StackCapacityExceded()
        self._data.append(elem)
        return elem

    def is_empty(self):
        return self._data == []

#3.3
class SetOfStacks:

    def __init__(self):
        self.stackArray = []
        self.current_stack = Stack()
        self.stackArray.append(self.current_stack)

    def push(self, elem):
        try:
            self.current_stack.push(elem)
        except StackCapacityExceded:
            self.current_stack = Stack()
            self.current_stack.push(elem)
            self.stackArray.append(self.current_stack)
        return elem

    def peek(self):
        if self.is_empty():
            raise Error("you crazy! Stacks are empty")
        if self.current_stack.is_empty():
            self.current_stack = self.stackArray[-1]
        return self.current_stack.peek()

    def pop(self):
        if self.is_empty():
            raise Error("you crazy! Stacks are empty")
        if self.current_stack.is_empty():
            self.stackArray.remove(self.current_stack)
            self.current_stack = self.stackArray[-1]
        return self.current_stack.pop()

    def is_empty(self):
        if len(self.stackArray) > 1:
            return False
        if self.current_stack.is_empty():
            return True

    # Follow Up Question (dummy one)
    def popAt(self, index):
        try:
            atStack = self.stackArray[index]
        except IndexError:
            return "Such Stack doesn't exist"
        return atStack.pop()

#3.4
class MyQueue:

    def __init__(self):
        self.stash = Stack()
        self.data  = Stack()

    def add(self, item):
        assert self.stash.is_empty
        while not self.data.is_empty():
            head = self.data.pop()
            self.stash.push(head)
        self.data.push(item)
        while not self.stash.is_empty():
            back = self.stash.pop()
            self.data.push(back)
        return self.data._data

    def remove(self):
        return self.data.pop()

    def peek(self):
        return self.data.peek()

    def is_empty(self):
        return self.data.is_empty()
