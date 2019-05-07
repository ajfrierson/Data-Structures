
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap the input value in a new node
        new_node = Node(value)
        # check if we have anything in our linked list
        # check if the head and tail are both None
        if not self.head:
            # hey, we're in an empty linked list situation
            # set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # hey, we have some elements in the linked list already
            # add the new node as the tail's `next` node
            self.tail.set_next(new_node)
            # update the `self.tail` reference accordingly
            self.tail = new_node

    # remove the head element and return its value
    def remove_head(self):
        # what if we have an empty linked list?
        # check to see if head == None
        if not self.head:
            return None
        # otherwise, we have elements to remove!
        # what if we only have a single linked list element?
        # check if self.head.next == None
        # check if self.head == self.tail
        if not self.head.get_next():
            # grab a second reference to our current head element
            head = self.head
            # set self.head = None
            self.head = None
            # set self.tail = None
            self.tail = None
            # return the value of the old head element
            return head.value
        # what if we have multiple linked list elements?
        else:
            # grab a second reference to our current head element
            head = self.head
            # reassign the self.head reference to the current head's next node
            self.head = self.head.get_next()
            # return the old head's value
            return head.value

    def contains(self, value):
        # check to see if list is empty
        if not self.head:
            # return None
            return None
        # init a `current_node` variable to keep track of where we are in the linked list as we're iterating
        current_node = self.head
        # check while current_node is a valid (non-None) node
        while current_node:
            # check if current_node.value == input value
            if current_node.get_value() == value:
                # return True
                return True
            # otherwise, the current node doesn't contain the value we're looking for; move on
            # update current_node to current_node.next
            current_node = current_node.get_next()
        # we've checked the whole list at this point, and we didn't find what we were looking for
        # return False
        return False

    # This function counts number of nodes in Linked List
    # recursively, given 'node' as starting node.
    def getCountRec(self, node):
        if (not node):  # Base case
            return 0
        else:
            return 1 + self.getCountRec(node.next_node)

    # A wrapper over getCountRec()
    def getCount(self):
        return self.getCountRec(self.head)


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?

        # Using a linked list as the data structure since removing from the end of the list is not efficient.
        self.storage = LinkedList()

    def enqueue(self, item):
        # Calls our add_to_tail method which adds an item to the end of a linked list
        self.storage.add_to_tail(item)
        pass

    def dequeue(self):
        # Removes the head element and returns its values. Uses the remove_head method from our linked list.
        dequeuedList = self.storage.remove_head()
        return dequeuedList

    def len(self):
        length = self.storage.getCount()
        return length


