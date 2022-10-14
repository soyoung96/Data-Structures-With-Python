class Queue:
    def __init__(self):
        self.items=[]
        self.front_index=0
    def enqueue(self,val):
        self.items.append(val)
    def dequeue(self):
        if(self.front_index == len(self.items)):
            print("Q is empty")
            return None
        else:
            item = self.items[self.front_index]
            self.front_index +=1
            return item

testQ = Queue()

testQ.enqueue(1)
testQ.enqueue(2)
testQ.enqueue(3)

testQ.dequeue()
testQ.dequeue()
testQ.dequeue()
testQ.dequeue()
testQ.dequeue()
