class HashTable:
    def __init__(self,m):
        self.list = [[None,None] for _ in range(m)]
        self.slotNum = m
    
    def findSlot(self,key):
        #key 값이 없으면 slot 번호 리턴
        #key 값이 있으면 slot 번호 리턴
        ind = self.hashFtn(key)
        start = ind
        while( (self.list[ind][0] != None) and (self.list[ind][0] != key)):
            ind = (ind+1) %self.slotNum
            if(ind == start):
                return False
        return ind

    def hashFtn(self,key):
        return key%self.slotNum

    def set(self,key,value=None):
        ind = self.findSlot(key)
        if(not ind): # 키값 없이 꽉차있음
            return None
        else:
            if(self.list[ind][0] !=None): #키값 있다 -> value 갱신
                self.list[ind][1] = value
            else: # key 값 없다->key value 둘다 갱신
                self.list[ind][0],self.list[ind][1] = key,value

    def search(self,key):
        ind = self.findSlot(key)
        if(not ind): # 꽉차있음
            return None
        else:
            if(self.list[ind][0] !=None): #키값 있다 ->value 반환
                return self.list[ind][1]
            else: # key 값 없다->key value 둘다 갱신
                return None

    def remove(self,key):
        ind = self.findSlot(key)
        if(not ind): #키값 없이 꽉차있음
            return None

        if(self.list[ind][0] != None):#키값있다
            
            while True:
                self.list[ind] = [None,None]# 삭제
                start = ind
                while True:
                    start = (start+1)%self.slotNum
                    if (self.list[start][0] ==None): #빈칸 나오면
                        return key
                    else:
                        k = self.hashFtn(self.list[start][0])
                        if(k<=ind<=start):
                            break
                self.list[ind] = [self.list[start][0],self.list[start][1]]
                ind = start

        else:#키값 없다
            return None



    def __iter__(self):
        for i in self.list:
            yield i
    
    def __str__(self):
        answer =""
        for key,val in self:
            answer+=(str(key)+","+str(val)+"\n")
        return answer

ht = HashTable(5)

ht.set(3,"고고")
ht.set(3,"갱신")
ht.remove(2)

print(ht)