
class Node(object):
    def __init__(self, point) -> None:
        self.point = point
        self.left = None
        self.right = None
        self.ytree = None
def yt(data):
    if not data:
        return None
    if len(data) == 1:
        node = Node(data[0])
    else:
        m = len(data)//2
        node = Node(data[m])  
        node.left = yt(data[:m])
        node.right = yt(data[m+1:])
    return node
           
def R2d(data,yd):
    if not data:
        return None
    if len(data) == 1:
        node = Node(data[0])
    else: 
            m = len(data)//2
            l = len(data)
            node = Node(data[m])   
            yd1=[]
            yd2=[]
            yd3=[]
            for i in yd:
                if i[0]<data[m][0]:
                    yd1.append(i)
                elif i[0]>data[m][0]:
                    yd2.append(i)
                else:
                    yd3.append(i)    
            while len(yd2)<l-m-1:
                yd2.append(yd3.pop())
            while len(yd1)<m:
                yd1.append(yd3.pop())              
            node.left = R2d(data[:m],yd1)
            node.right = R2d(data[m+1:],yd2)
    node.ytree = yt(yd)
    return node

def wR2(point, x1,x2,y1,y2):
    return x1<=point[0]<=x2 and y1<=point[1]<=y2

def wR(x,x1,x2):
    return x>=x1 and x<=x2

def SR1d (tree, y1, y2):
    nodes = []
    spl = tree
    while spl != None:
        n = spl.point[1]
        if y2 < n:
            spl = spl.left
        elif y1 > n:
            spl = spl.right
        elif y1 <= n <= y2:
            break
    if spl == None:
        return nodes
    elif wR( spl.point[1] , y1,y2 ):
        nodes.append(spl.point)
    nodes += SR1d(spl.left, y1,y2)
    nodes += SR1d(spl.right,y1,y2)
    return nodes

def SR2d (tree, x1, x2, y1, y2 ):
    results = []
    ancestor = tree


    while ancestor != None:
        node = ancestor.point[0]
        if x2 < node:
            ancestor = ancestor.left
        elif x1 > node:
            ancestor = ancestor.right
        elif x1 <= node <= x2:
            break
    if ancestor == None:
        return results
    else:
        if wR(ancestor.point[1], y1, y2) :
            results.append(ancestor.point)


        lft = ancestor.left 
        while lft != None :
            if wR2(lft.point, x1, x2, y1, y2):
                results.append(lft.point)
            if x1 <= lft.point[0]:
                if lft.right != None:
                    results += SR1d(lft.right.ytree, y1, y2)
                lft = lft.left
            else:
                lft = lft.right


        rght = ancestor.right
        while rght != None :
            if wR2(rght.point, x1,x2,y1,y2):
                    results.append(rght.point)
            if x2 >= rght.point[0]:
                if rght.left != None:
                    results += SR1d(rght.left.ytree, y1, y2)
                rght = rght.right
            else:
                    rght = rght.left
        
        return results

class PointDatabase:
    def __init__(self,pointlist):
        self.tree=R2d(sorted(pointlist, key=lambda x: x[0]),sorted(pointlist, key=lambda x: x[1]))
    def searchNearby(self,q,d):
        return SR2d(self.tree,q[0]-d,q[0]+d,q[1]-d,q[1]+d)
