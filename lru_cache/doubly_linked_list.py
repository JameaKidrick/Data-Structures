"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

# ONLY THINGS CHANGED: ADDING KEYS
class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, key, value):
        current_next = self.next
        self.next = ListNode(key, value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, key, value):
        current_prev = self.prev
        self.prev = ListNode(key, value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, key, value):
        self.length += 1
        if not self.head and not self.tail:
            self.head = self.tail = ListNode(key, value)
        else:
            self.head.insert_before(key, value)
            self.head = self.head.prev

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, key, value):
        self.length += 1 
        if not self.head and not self.tail:
            self.head = self.tail = ListNode(key, value)
        else:
            self.tail.insert_after(key, value)
            self.tail = self.tail.next

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.key, node.value)

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.key, node.value)

    def delete(self, node):
        if not self.head and not self.tail:
            print('ERROR: Attempted to delete node not in list')
            return
        elif self.head == self.tail and self.head == node:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()
        self.length -= 1

    def get_max(self):
        maximum = 0
        cur_node = self.head
        cur_value = self.head.value
        while cur_value is not None:
            if cur_value > maximum:
                maximum = cur_value
            if cur_node.next is not None:
                    cur_value = cur_node.next.value
                    cur_node = cur_node.next
            else:
                return maximum
        return maximum
