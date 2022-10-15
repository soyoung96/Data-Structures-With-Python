class Stack:
    def __init__(self):
        self.items=[]
    def pop(self):
        try:
            return self.items.pop()
        except:
            print("stack is empty")

    def push(self,elt):
        self.items.append(elt)
    
    def top(self):
        try:
            return self.items[-1]
        except:
            print("stack is empty")
    
    def __len__(self):
        return len(self.items)

stack =Stack()
stack.push(1)
stack.top()
print(stack.pop())
stack.pop()
