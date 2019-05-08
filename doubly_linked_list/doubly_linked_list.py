"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
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

  def add_to_head(self, value):
      self.length += 1  
      current_head = self.head
      # If there is no head create a new ListNode and set the head and the tail to this new node.
      if not current_head:
          node = ListNode(value)
          self.head = node
          self.tail = node
      # If there is a head then we can add this head value before our current value and point back to it using head.prev
      else:
          current_head.insert_before(value)
          self.head = current_head.prev
      return self.head

  def remove_from_head(self):
        if self.head:
            self.length -= 1
            # handle list of length 1
            if self.head == self.tail:
                head = self.head
                self.head = None
                self.tail = None
                # self.length -= 1
                return head.value
            # else handle length > 1 list
            else:
                old_head = self.head
                self.head = old_head.next
                old_head.delete()
                # self.length -= 1
                return old_head.value
        else:
            return None

  def add_to_tail(self, value):
      self.length += 1
      current_tail = self.tail
      # If there is no element make it the current tail
      if not current_tail:
          node = ListNode(value)
          self.head = node
          self.tail = node
      # If there is one or more element insert after the current tail and set the new tail to be this value's `next`
      else:
          current_tail.insert_after(value)
          self.tail = current_tail.next
      pass

  def remove_from_tail(self):
      self.length -= 1  
      if not self.tail:
          return None
      if self.head == self.tail:
          tail = self.tail
          self.head = None
          self.tail = None
          return tail.value
      else:
          tail = self.tail
          self.tail.delete()
          self.tail = self.tail.prev
          return tail.value

  def move_to_front(self, node):
        # self.length +=1
        # check if empty
        if self.head is not node:
          # if in a middle spot remove the node
            if node.next and node.prev:
                node.delete()
            # refer to self.head
            current_head = self.head
            # set current head to node since now it's in front
            self.head = node
            # the new head's next should be the old node that's in front of it and likewise that item's `prev` should now point to the new head which is node
            node.next = current_head
            current_head.prev = node

  def move_to_end(self, node):
      # check if empty
      if self.tail is not node:
          # if in a middle spot
          if node.next and node.prev:
              node.delete()
          current_tail = self.tail
          # the new tail's prev should be the old node that's in behind it and likewise that item's `next` should now point to the new tail which is node
          self.tail = node
          node.prev = current_tail
          current_tail.prev = node

  def delete(self, node):
      self.length -= 1  
      # check if empty and return None if it is
      if not self.head and not self.tail:
          return None
      # if the list only has a single node, delete it
      # both self.head and self.tail should be None
      if self.head == self.tail:
          node.delete()
          self.head = None
          self.tail = None
      # if given node is the head
      if self.head == node:
          # set the self.head pointer to the next node
          self.head = node.next
          # delete the node
          node.delete()

      # if the given node is the tail
      if self.tail == node:
          # set the self.tail pointer to the previous node
          self.tail = node.prev
      # delete the node
          node.delete()
      # otherwise, tnode is somewhere in the middle and we can delete normally
      else:
          # just call node.delete
          node.delete()

  def get_max(self):
      max = 0
      # Start at the beginning looking for the max value and return that value
      current = self.head
      while current:
          if current.value > max:
              max = current.value
          current = current.next
      return max

# dll = DoublyLinkedList(ListNode(1))

# dll.move_to_end(ListNode(40))

# print(len(dll))