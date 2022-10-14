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


inputExp = list(sys.stdin.readline().rstrip())

def makeBackExp(inputExp):
    backExp = ""
    backStack = Stack()
    for token in inputExp: #먼저 후위표기식으로 만들기
        if token == "(":
            backStack.push(token)
        elif (token == ")"):
            while True:
                tmp = backStack.pop()
                if(tmp == "("):
                    break
                else:
                    backExp+=tmp # 후위표기식에 표기해줌
        elif (token in "+-*/"): #연산자라면
            if(token in "+-"):
                while True:
                    if(len(backStack)!=0):
                        if(backStack.top() in "+=*/"):
                            backExp+=backStack.pop() # 후위표기식에 표기해줌
                        else:
                            backStack.push(token)
                            break
                    else:
                        backStack.push(token)
                        break
                    
            elif(token in "*/"):
                while True:
                    if(len(backStack)!=0):
                        if(backStack.top() in "*/"):
                            backExp+=backStack.pop() # 후위표기식에 표기해줌
                        else:
                            backStack.push(token)
                            break
                    else:
                        backStack.push(token)
                        break
        else: # 피연산자라면
            backExp+=token # 후위표기식에 표기해줌
    
    while(backStack): # backStack에 원소 남아있으면 전부 pop
        backExp+=backStack.pop()
    return backExp

def operator(oper,num1,num2):
    if(oper == "+"):
        return num1 + num2
    elif(oper == "-"):
        return num1 - num2
    elif(oper == "*"):
        return num1 * num2
    else: # 나누기
        return num1 / num2


def calculator(backExp):
    calStack = Stack()
    for token in backExp:
        if(token in "+-*/"):#연산자라면
            num1 = int(calStack.pop())
            num2 = int(calStack.pop())
            calStack.push(operator(token,num2,num1))
        else: #피연산자라면
            calStack.push(token)
    
    return calStack.pop()

backExp = makeBackExp(inputExp)
print(calculator(backExp))






            
