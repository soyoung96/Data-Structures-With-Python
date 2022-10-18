from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size=0
    def __len__(self):
        return self.size

    def splice(self,a,b,x): # 연결리스트 a에서 b 구간 짤라서 노드 x 이후에 넣기
        #조건 1: a->...->b
        #조건 2: a,b 사이에 head 없음
        aPrev,bNext,xNext= a.prev,b.next,x.next
        
        aPrev.next = bNext
        bNext.prev = aPrev #cut

        x.next = a
        a.prev = x
        b.next = xNext
        xNext.prev = b

    def moveAfter(self,a,x): #하나의 노드 a를 x 이후로 이동
        self.splice(a,a,x)
    
    def moveBefore(self,a,x): #하나의 노드 a를 x 이전으로 이동
        self.splice(a,a,x.prev)

    def insertAfter(self,x,key):#하나의 숫자를 노트 a로 만들어 x 이후로 이동
        node =  Node(key)
        self.moveAfter(node,x)

    def insertBefore(self,x,key):#하나의 숫자를 노트 a로 만들어 x 이전으로 이동
        node =  Node(key)
        self.moveBefore(node,x)

    def pushFront(self,key):#삽입 연산1
        self.insertAfter(self.head,key)
        self.size +=1

    def pushBack(self,key):#삽입 연산2
        self.insertBefore(self.head,key)
        self.size +=1

    def search(self,key):
        v = self.head
        for v in self:
            if(v.key == key):
                return v
        
        return None

    def remove(self,x):
        if(x==None or x ==self.head):
            return
        else:
            x.prev.next = x.next
            x.next.prev = x.prev
            del x

    def popFront(self):
        if(len(self) ==0):
            return None
        else:
            popVal = self.head.next.key
            self.remove(self.head.next)
            return popVal

    def popBack(self):
        if(len(self) ==0):
            return None
        else:
            popVal = self.head.prev.key
            self.remove(self.head.prev)
            return popVal  

    def __str__(self):
        answer=""
        for v in self:
            answer+=(str(v.key)+"->")
            v = v.next
            
        return answer

    def __iter__(self):
        v = self.head
        while(v.next != self.head):
            yield v
            v = v.next
        yield v

l = DoublyLinkedList()

l.pushFront(1)
print(l)
l.pushFront(2)
print(l)
l.pushFront(3)
print(l)
l.pushFront(4)

print("l.search(4) = "+str(l.search(1)))

print(l)

l.popFront()
print(l)
l.popBack()
print(l)
l.popBack()
print(l)
l.popBack()
print(l)
l.popBack()
print(l)

    

        


    
