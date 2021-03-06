import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

# CONSISTENT PROBLEM
    # I kept coding return BinarySearchTree(left.value).insert(value) instead of just left.value.insert(value)
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If there is no node at root, insert value as root
        if not self:
            self = BinarySearchTree(value)
        # Compare value to the root
        # If value is smaller, 
        if value < self.value:
            # Look left 
            # If node, repeat
            if self.left:
                return self.left.insert(value)
            # If no node, make new one with value
            else:
                self.left = BinarySearchTree(value)
                return self.left
        # If value is greater or equal,
        elif value >= self.value:
            # Look right
            # If node, repeat
            if self.right:
                return self.right.insert(value)
            # If no node, make new one with value
            else:
                self.right = BinarySearchTree(value)
                return self.right
        return self

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # If there is no node at root, return False
        if self.value is None:
            return False
        # Compare target to the root
        # If target is smaller,
        if target < self.value:
            # Go left
            # Look at node
            if self.left:
                return self.left.contains(target)
            else:
                return False
        # If target is bigger or equal,
        elif target > self.value:
            # Go right
            # Look at node
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        # If no right child, return value
        if self.right is None:
            return self.value
        # Otherwise, go right until you can’t anymore
        else:
            return self.right.get_max()
        # Return value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # # If no node, return None
        if not self.value:
            return None
        # # Call cb on node
        else:
            cb(self.value)
        # If right child, go right
        if self.right:
            return self.right.for_each(cb)
        # If left child, go left
        if self.left:
            return self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
