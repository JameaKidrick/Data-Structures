import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.length = 0
        self.storage = DoublyLinkedList()
        self.hash = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # create a variable pointing to the current node
        current = self.storage.head
        # while the node is not equal to None...
        while current is not None:
            # check to see if the key is in the hash table
            if key in self.hash.keys():
                # if the current node's key is the same as the key we are searching for...
                if current.key == key:
                    # move the node to the front of the linked list and return its value
                    self.storage.move_to_front(current)
                    return current.value
                else:
                    # go to the next node if node's key is not the same
                    current = current.next
            else:
                # return None if the key does not exist in the hash table
                return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value): 
        # if the key is already in the hash table
        if key in self.hash.keys():
            # create a variable pointing to the current node
            current = self.storage.head
            # overwrite the hash table key's value
            self.hash[key] = value
            # find the node with the matching key
            while current is not None:
                if current.key == key:
                    # overwrite the node's value
                    current.value = value
                    return
                else:
                    current = current.next
        # if the cache limit is reached...
        elif self.length == self.limit:
            # delete the tail (LRU) from the hash table
            del self.hash[self.storage.tail.key]
            # delete the tail (LRU) from the linked list
            self.storage.remove_from_tail()
        else:
            # increase the length by 1
            self.length += 1
        # add the new pair to the hash table
        self.hash.update({key: value})
        # add the new pair to the cache as the head (MRU)
        self.storage.add_to_head(key, value)
