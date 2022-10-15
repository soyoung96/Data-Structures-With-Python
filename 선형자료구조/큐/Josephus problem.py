from collections import deque
class Queue:
    def __init__(self):
        self.items=deque([])
    def enqueue(self,val):
        self.items.append(val)
    def dequeue(self):
        return self.items.popleft()
    def __len__(self):
        return len(self.items)

def josephusProblem(n,k): #최종 생존자 번호 return
    step =1
    queue = Queue()
    for i in range(1,n+1): #병사 집어넣기
        queue.enqueue(i)
    while(len(queue)!=1):
        tmp = queue.dequeue()
        if(step % k !=0):#살려야함
            queue.enqueue(tmp)
        step+=1
    
    return queue.dequeue() #마지막 남은 생존자 리턴

print(josephusProblem(6,2))







