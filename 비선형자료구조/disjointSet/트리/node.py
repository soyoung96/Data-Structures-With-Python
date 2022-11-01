class Node:
    def __init__(self,key):
        self.key = key
        self.parent = self
        self.rank = 0
