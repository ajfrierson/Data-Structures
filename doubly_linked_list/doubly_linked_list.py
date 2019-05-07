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
            # handle list of length 1
            if self.head == self.tail:
                head = self.head
                self.head = None
                self.tail = None
                return head.value
            # else handle length > 1 list
            else:
                old_head = self.head
                self.head = old_head.next
                old_head.delete()
                return old_head.value
        else:
            return None

  def add_to_tail(self, value):
    pass

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass
