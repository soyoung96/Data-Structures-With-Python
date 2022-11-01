class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.key)
        
    def preorder(self):
        if(self!=None):
            print(self.key)
            if(self.left):
                self.left.preorder()
            if(self.right):
                self.right.preorder()

    def inorder(self):
        if(self!=None):
            if(self.left):
                self.left.inorder()
            print(self.key)
            if(self.right):
                self.right.inorder()

    def postorder(self):
        if(self!=None):
            if(self.left):
                self.left.postorder()
            if(self.right):
                self.right.postorder()
            print(self.key)

    

# a = Node("A")
# b = Node("B")
# c = Node("C")
# d = Node("D")
# g = Node("G")
# i = Node("I")
# h = Node("H")
# f = Node("f")

# a.parent = b
# d.parent = b
# b.left = a
# b.right = d

# g.right = i
# i.parent=g
# h.parent = i
# i.left = h

# b.parent = f
# g.parent = f
# f.left = b
# f.right = g

# #이진트리 탐색

# print("f.preorder()")
# f.preorder()
# print("f.inorder()")
# f.inorder()
# print("f.postorder()")
# f.postorder()
