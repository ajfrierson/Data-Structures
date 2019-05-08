class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
        #check if new node's value is less that our current node's value
        if value < self.value:
            #check if there is no left child
            if not self.left:
                #park the new_node here
                self.left = BinarySearchTree(value)
            else:    
                #otherwise we have to traverse further down since there exists a left child
                self.left.insert(value)
        #do the same on the right side
        else:
            #check if there is no right child
            if not self.right:
            #park the value here  
                self.right = BinarySearchTree(value)
            else:
            #keep recursing down the right since there is a right child
                self.right.insert(value)  

  def contains(self, target):
    #set a reference to self
    current = self
    while True:
        #will return False if doesn't contain the item
        if not current:
              return False
        #if there is a match return true
        if current.value == target:
              return True      
        #If it's bigger check a node to the left which is lower than current otherwise check right
        elif current.value > target:
          current = current.left
        else:
          current = current.right        


  def get_max(self):
    #set a reference to self
    current = self
    max = 0
    while current:
          # if the current value is greater than the max set it to the current value and move right to check again 
          if current.value > max:
            max = current.value
            current = current.right

    return max        

