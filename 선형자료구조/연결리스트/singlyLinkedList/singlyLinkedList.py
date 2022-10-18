from node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size=0
    def __len__(self):
        return self.size

    def pushFront(self,key):
        newNode = Node(key)
        newNode.link = self.head
        self.head = newNode
        self.size+=1
    
    def pushBack(self,key):
        newNode = Node(key)
        if(self.size ==0):
            self.head = newNode
        else:
            tail = self.head
            while tail.link!=None:
                tail = tail.link
            tail.link = newNode
        self.size+=1
    
    def popFront(self):
        if(self.size ==0):
            return None
        else:
            delNode = self.head
            self.head = delNode.link
            self.size-=1
            delNodeKey = delNode.key
            del delNode
            return delNodeKey

    def popBack(self):
        if(self.size == 0):
            return None
        elif(self.size ==1):
            self.head =None
            self.size-=1
            return None
        else:
            preTail= self.head
            tail = preTail.link
            
            while(tail.link):
                preTail =tail
                tail = tail.link
            
            else:
                delNode = tail
                preTail.link = None
                self.size-=1
                delNodeKey = delNode.key
                del delNode
                return delNodeKey

    def __str__(self):
        node = self.head
        answer = ""
        for node in self:
            answer+=(str(node)+"->")
        return answer

    def __iter__(self):
        node = self.head
        while(node):
            yield node
            node = node.link

    def search(self,key):
        for node in self:
            if(node.key == key):
                return node
        
        return None

l = SinglyLinkedList()

l.pushFront(1)
print(l)
l.pushFront(2)
print(l)
l.pushFront(3)
print(l)
l.pushFront(4)

print("l.search(3) = "+str(l.search(3)))

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

    

        


    
