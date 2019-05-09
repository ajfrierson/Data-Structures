class Heap:
    def __init__(self, comporator):
        self.storage = []
        

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        deleted = self.storage[0]
        # changing the last element to the first element
        self.storage[0] = self.storage[len(self.storage) - 1]
        # getting rid of the last element in self.storage
        self.storage.pop()
        self._sift_down(0)
        return deleted

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # keeps looping until the top of the heap is reached
        while (index - 1) // 2 >= 0:
            # if the value of the parent is less than the child, swap
            if self.storage[(index - 1) // 2] < self.storage[index]:
                self.storage[(index - 1) // 2], self.storage[index] = self.storage[index], self.storage[(index - 1) // 2]
            # decrementing index so loop will start at parent's parent
            index = (index - 1) // 2

    def _sift_down(self, index):
        # checks to see if a child element exists in self.storage
        while index * 2 + 1 < len(self.storage):
            # if the second child doesn't exist, by default the first child is biggest
            if index * 2 + 2 > len(self.storage) - 1:
                biggest_child = index * 2 + 1
            # compares the children to see which is biggest
            else:
                if self.storage[index * 2 + 1] > self.storage[index * 2 + 2]:
                    biggest_child = index * 2 + 1
                else:
                    biggest_child = index * 2 + 2
            # compares the parent to the biggest child, swapping if the parent is less
            if self.storage[index] < self.storage[biggest_child]:
                self.storage[index], self.storage[biggest_child] = self.storage[biggest_child], self.storage[index]
            # changes index to be child for next iteration
            index = biggest_child
