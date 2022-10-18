class Node:
    def __init__(self,key=None):
        self.key =key
        self.next = self
        self.prev = self
    def __str__(self):
        return str(self.key)