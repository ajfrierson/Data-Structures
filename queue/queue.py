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
    
