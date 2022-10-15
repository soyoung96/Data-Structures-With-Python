class Node:
    def __init__(self,key=None):
        self.key =key
        self.link = None
    def __str__(self):
        return self.key