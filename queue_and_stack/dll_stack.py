import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        '''
        adds an item to the top of the stack
        '''
        self.storage.add_to_head(value)
        self.size += 1
        return self.size

    def pop(self):
        '''
        removes and returns an item from the top of the stack
        '''
        if self.storage.tail is None:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        '''
        returns the number of items in the stack
        '''
        return self.size
