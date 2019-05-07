class Node:
      def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

      def get_value(self):
            return self.value

      def get_next(self):
            return self.get_next

      def set_next(self, new_next):
            self.next_node = self.new_next

class LinkedList:
      def __init__(self):            

class Queue:
      def __init__(self):
      self.size = 0
      # what data structure should we
      # use to store queue elements?
      self.storage = []

      def enqueue(self, item):
            self.storage = [item] + self.storage
            self.size += 1

      def dequeue(self):
            if self.size == 0:
            return 
            self.size -= 1
            return self.storage.pop()

      def len(self):
            return self.size
