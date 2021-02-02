class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Python List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0 

    #Self -> boolean
    #Returns true if the stack is empty, false otherwise
    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''
        return self.size() == 0

    #Self -> boolean
    #Returns true if the stack is full, false otherwise
    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == self.capacity

    #Stack and item -> Returns nothing
    #Pushes item on stack
    def push(self, item):
        '''If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError
        self.items[self.num_items] = item
        self.num_items += 1

    #Self -> item
    #Removes last item pushed to the stack and returns the item 
    def pop(self): 
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if (self.is_empty()):
            raise IndexError
        item = self.items[self.num_items-1]
        self.items[self.num_items - 1] = None
        self.num_items -= 1
        return item

    #Self -> item
    #Returns last item pushed to the stack
    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if (self.is_empty()):
            raise IndexError
        return self.items[self.num_items-1]
            
    #Self -> int
    #Returns number of items currently in the stack
    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.num_items
