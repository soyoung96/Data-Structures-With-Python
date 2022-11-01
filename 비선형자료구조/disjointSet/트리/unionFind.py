from node import Node

def makeSet(x):
    return Node(x)

def find(x): #x의 root 리턴
    while x.parent != x: #root가 아니면
        x = x.parent
    
    return x

def union(x,y):
    rootX,rootY = find(x),find(y)
    if(rootX==rootY): #루트 같으면
        print("union 불가")
        return
    if(rootX.rank > rootY.rank): #rootX의 랭크가 더 크면
        rootY.parent = rootX # rootX 자식으로 rootY추가
    elif(rootX.rank < rootY.rank):
        rootX.parent = rootY # rootY 자식으로 rootX추가
    else: #같을 경우
        rootY.parent = rootX # rootX 자식으로 rootY추가
        rootX.rank +=1 #랭크하나 증가
    

a = makeSet(1)
b = makeSet(2)
c = makeSet(3)
d = makeSet(4)
e = makeSet(5)

union(a,b)

union(a,c)

union(d,e)

union(c,d)

rootD = find(d)

print("rootD: "+str(rootD.rank))
