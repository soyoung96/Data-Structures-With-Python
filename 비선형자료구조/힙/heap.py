#최대 힙!

def leafNode(eltList,k): # 리프노드인지 체크
    if((k*2+1)>(len(eltList)-1)): #맨 끝 인덱스보다 왼쪽 자식 인덱스가 더 크면 자식 없음
        return True # 리프노드임
    else:
        return False #리프노드 아님

def heapifyDown(eltList,k): #자식노드의 값이 #O(logN)
    while(not leafNode(eltList,k)):#리프노드 아니라면 -> 무조건 왼쪽 자식은 있음
        if((2*k+2)<=(len(eltList)-1)):#오른쪽 자식도 있다면
            l,r = 2*k+1,2*k+2
            _,maxInd = max((eltList[k],k),(eltList[r],r),(eltList[l],l)) #최대 힙
            
        else: #왼쪽 자식뿐이라면
            l = 2*k+1
            _,maxInd = max((eltList[k],k),(eltList[l],l)) #최대 힙
        
        if(k!=maxInd):
                eltList[maxInd],eltList[k] = eltList[k],eltList[maxInd]
                k = maxInd #DOWN!
        else:
            break

def heapifyUp(eltList,k):#O(logn)
    while(k>0 and eltList[k]>eltList[(k-1)//2]): #아직 루트노드 도착전인데 바꿔야할 상황이다?
        eltList[(k-1)//2],eltList[k] = eltList[k],eltList[(k-1)//2] #바꿔줌
        k = (k-1)//2


def makeHeap(eltList):#O(nlogn)
    n = len(eltList)
    for k in range(n-1,-1,-1): #n-1부터 0까지 #O(n)
        heapifyDown(eltList,k) #O(logn)


def insert(eltList,val): #O(logn)
    eltList.append(val)
    heapifyUp(eltList,len(eltList)-1) #마지막 인데스(방금 추가된 인덱스)

def deleteMax(eltList):
    if(len(eltList)==0):
        return None
    else:
        key = eltList[0]
        eltList[0],eltList[len(eltList)-1] = eltList[len(eltList)-1],eltList[0] #루트노드 마지막 노트 위치 바꿈
        eltList.pop() #기존 루트 노드 삭제
        heapifyDown(eltList,0)
        return key

testList = [1,2,3,4,5,6]
print(testList)

print("makeHeap(testList)실행")
makeHeap(testList)
print(testList)

print("insert(testList,4)실행")
insert(testList,4)
print(testList)

print("insert(testList,7)실행")
insert(testList,7)
print(testList)

print("deleteMax(eltList)실행1")
deleteMax(testList)
print(testList)

print("deleteMax(eltList)실행2")
deleteMax(testList)
print(testList)