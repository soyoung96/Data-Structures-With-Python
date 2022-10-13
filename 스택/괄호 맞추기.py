import sys

class Stack:
    def __init__(self):
        self.items=[]
    def pop(self):
        try:
            return self.items.pop()
        except:
            raise Exception("stack is empty")

    def push(self,elt):
        self.items.append(elt)
    
    def top(self):
        try:
            return self.items[-1]
        except:
            raise Exception("stack is empty")
    
    def __len__(self):
        return len(self.items)

inputReq = sys.stdin.readline().rstrip()

stack = Stack()
for p in inputReq:
    if(p =="("):
        stack.push(p)
    elif(p==")"):
        try:
            stack.pop()
        except:
            print("False")
            exit() #프로그램 종료 # )가 더 많다
    else:
        print("Not allowed Symbol")

if(len(stack)!=0): # (가 더 많다
    print("False")
else: #올바른 괄호
    print("True")
    

