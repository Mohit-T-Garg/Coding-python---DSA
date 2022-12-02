
class stack: #create stack class
    def __init__(self):
        self.s = []
    def clear(self):
        self.s=[]
    def print(self):
        print(self.s)
    def val(self):
        return self.s
    def empty(self): # boolean-->stack is empty or not
        return self.s==[]
    def push(self,x): #push-->add element to stack
        self.s.append(x)
    def get(self):#get-->view top element on stack
        if self.s==[]:
            return None
        return self.s[len(self.s)-1]
    def pop(self):#pop-->remove top element of stack
        if self.s==[]:
            return None
        ans = self.s.pop()
        return ans 

def ans(p,s,t,visit):
    n = len(visit)
    path = []
    for i in range(n):
        path.append([])
    for i in p:
        path[i[0]].append(i[1])
        path[i[1]].append(i[0])    
    st = stack()
    st.push(s)
    v=visit.copy()
    visit[s]=1
    n=s
    while n!=t and st.empty()==False:
        n = st.get()
        if n==t:
            break
        if v[n]==len(path[n]):
            st.pop()
        else:
            ne = path[n][v[n]]
            v[n]+=1
            if visit[ne]!=1:              
                visit[ne]=1
                st.push(ne) 
   
    a = st.val()       
    return  a          

def pk(parent,i):
    while parent[i]!=i:
        i = parent[i]
    return i  
def findMaxCapacity(n,links,s,t):
    D = {}
    for i in links:
        p = (i[0],i[1])
        if  p in D :
            if  D[p] < i[2]:
                D[p] = i[2]
        else:
            D[p] =i[2]

    D=list(sorted(D.items(), key=lambda x:x[1], reverse=True))

    path = []
    parent = []
    visit=[]
    C = -1
    for i in range(n):
        parent.append(i)
        visit.append(0)
    rank = [0]*n      
    for i in D:
        e = list(i[0])
        C= i[1]
        x = int(e[0])
        y = int(e[1])
        x=pk(parent,x)
        y=pk(parent,y)
        if x!=y:
            if rank[x]>rank[y]:
                parent[y] = x
            elif rank[x]<rank[y]:
                parent[x] = y
            else:
                if y>x:
                    parent[y]=x    
                    rank[x]+=1
                else:
                    parent[x]=y
                    rank[y]+=1    
            path.append([i[0][0],i[0][1]])  
            if pk(parent,s)==pk(parent,t):
                break
    route = ans(path,s,t,visit)

         
    return (C,route)             
#print(findMaxCapacity(8, [(0,1,5), (1,2,8), (2,3,6), (3,4,1), (4,5,15), (5,6,2), (6,7,3), (7,0,12), (1,5,7), (1,6,3), (2,5,9), (2,7,11), (3,7,14), (0,4,3), (0,5,4)], 0, 4))
#print(findMaxCapacity(8, [(0,1,5), (1,2,8), (2,3,6), (3,4,1), (4,5,15), (5,6,2), (6,7,3), (7,0,12), (1,5,7), (1,6,3), (2,5,9), (2,7,11), (3,7,14), (0,4,3), (0,5,4)], 0, 4))