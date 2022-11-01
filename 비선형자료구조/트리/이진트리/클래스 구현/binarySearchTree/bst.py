from re import A
from node import Node
class BST:
    def __init__(self):
        self.root = None
        self.size =0

    def __len__(self):
        return self.size
    

    def find_loc(self,key): # key 노드가 있다면 해당 노드 반환 
                            #없으면 노드가 삽입될 부모노드 리턴
        if(self.size == 0):
            return None,None
        else:
            p = None
            v = self.root
            while v != None: #v가 None이 아닐때까지
                if(v.key == key):
                    return p,v
                elif v.key <key:
                    p,v = v,v.right
                else:
                    p,v = v,v.left
            
            return p,v #c찾는 key값이 bst 에 없음
    
    def search(self,key):
        p,v = self.find_loc(key)

        if(v != None and v.key == key):
            return v
        else: #못찾음
            print("Not Found")
            return None
    
    def insert(self,key):
        newNode = Node(key)
        p,v = self.find_loc(key)
        if(self.size == 0): #처음 삽입되는 노드!
            self.root = newNode
            self.size +=1
            return newNode

        elif(v!=None and v.key == key):#이미 이진트리에 키가 있어 중복되는 경우
            print("key is already in tree")
            return v

        else: # 이진 트리에 없고 삽입되는 노드!
            newNode.parent =p
            if(p.key>key):
                p.left = newNode
            else:
                p.right = newNode
            self.size +=1
            return newNode
        
    def rotateRight(self,node): # O(1)
        if node == None:
            return None
        x = node.left
        if(x == None):
            return None
        b = node.right
        x.parent = node.parent
        if node.parent != None: #node가 root가 아니면
            if node.parent.left == node:#자식으로 x연결
                node.parent.left = x
            else:
                node.parent.right = x
        else:
            self.root = x #기존 node가 root이면 이제 x가 루트가 됌
        
        x.right = node #기존 노드 x의 자식으로
        node.parent = x

        node.left = b # node의 왼쪽 자식으로 b 설정
        if b!=None:
            b.parent = node
        
        




    def deleteByMerging(self,node):
        l = node.left
        r = node.right
        p = node.parent

        if(self.size == 0):
            return None
    
        if(l != None):
            c = l
            cMax = l
            while cMax.right:
                cMax = cMax.right
            cMax.right = r
        else:
            c = r

        if p==None: #삭제하려는 값이 루트 -> 루트 값 갱신해주어야 함
            self.root = c
            if c: #삭제 하고 값이 있다면
                c.parent = None
        
        if p != None:
            if c: #삭제하고 값이 있다면
                c.parent = p
                if p.key>c.key:
                    p.left = c
                else:
                    p.right = c
            else: #삭제하고 값이 없다면
                if p.key>node.key: #삭제된 쪽이 왼쪽 노드
                    p.left = None
                else:#삭제된 쪽이 오른쪽 노드
                    p.right = None
        
        self.size -=1
        return None
        







testBST = BST()

print("testBST.insert(1)")
testBST.insert(1)
print("testBST.insert(2)")
testBST.insert(2)
print("testBST.insert(3)")
testBST.insert(3)
print("testBST.insert(4)")
testBST.insert(4)
print("testBST.insert(5)")
testBST.insert(5)
print("testBST.insert(1)")
testBST.insert(1)
print("testBST.search(1)")
testBST.search(1)
print("testBST.deleteByMerging(testBST.search(5))")
testBST.deleteByMerging(testBST.search(5))

print("testBST.deleteByMerging(testBST.search(2))")
testBST.deleteByMerging(testBST.search(2))

print("testBST.deleteByMerging(testBST.search(1))")
testBST.deleteByMerging(testBST.search(1))

print("testBST.deleteByMerging(testBST.search(3))")
testBST.deleteByMerging(testBST.search(3))

print("testBST.deleteByMerging(testBST.search(4))")
testBST.deleteByMerging(testBST.search(4))



testBST.root.inorder()

