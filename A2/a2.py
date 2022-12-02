#Let us consider collision bw i and i+1 th mass as ith collision
class c:  #Collision Properties - i , time of collision if occuring otherwise -1
    def __init__(self,a,b) :
        self.ct  = a
        self.i = b
        
class MinHeap: #Min heap implementation of class c with c.ct(collision time) as comparision basis
    def __init__(self):
        self.Heap = [c(0,-1)]
        self.ms = 0 #MAXSIZE of array ; will append if size is same as ms
        self.size = 0 #Current size of Heap and location of last element
        self.top = 1 #Position for min collision time 
    def s(self): #Size of Heap
        s = 0 + self.size
        return s
    def swap(self, x, y): #Swapping two class positions in Heap Array
        self.Heap[x], self.Heap[y] = self.Heap[y], self.Heap[x]
    def minHeapify(self, pos):
        if pos*2 <= self.size: #Not a leaf
            if self.Heap[pos].ct > self.Heap[2*pos+1].ct or self.Heap[pos].ct > self.Heap[2*pos].ct : #either child is smaller than current
                if self.Heap[2*pos].ct < self.Heap[2*pos+1].ct:
                    self.swap(pos, 2*pos)
                    self.minHeapify(2*pos)
                else:
                    self.swap(pos, 2*pos+1)
                    self.minHeapify(2*pos+1)
    def insert(self, element,i):
        self.size+= 1
        if self.size > self.ms : #Size = MAXSIZE for HEAP array ; append
            self.Heap.append(c(element,i))
            self.ms+=1
        else: #Reference possible as size < ms
            self.Heap[self.size] = c(element,i)
        current = self.size
        while self.Heap[current].ct < self.Heap[current//2].ct: #if parent greater than swap till root
            self.swap(current, current//2)
            current = current//2
    def remove(self): #Remove Heap[1] and replace with last element and minheapify 
        answer = self.Heap[self.top]
        self.Heap[self.top] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.top)
        return answer



def listCollisions(M, x, v, m, To):
    Ans = [] #Final Answer containing tuples    
    n = len(M) #No. of objects
    collision = [-1]*(n-1) #Possible collision charaterized by ith and i+1th object - time if possible -1 otherwise
    T = [0]*n #Last time x[i] was updated 
    Heap = MinHeap()
    for k in range(n-1):
        if v[k]-v[k+1] > 0: #Collision possible check
            collision[k] = (x[k+1]-x[k])/(v[k]-v[k+1]) 
            Heap.insert(collision[k],k)
        else:
            collision[k] = -1;  
    t = 0 #current time
    while Heap.s()>0: #While there is possible valid collision
            mn = Heap.remove() 
            i = mn.i
            if(mn.ct==collision[i]): #Check if Expired collision due to interference in any object - no longer valid
                t = mn.ct 
                if(t>To): #time exceed break
                    break
                collision[i] = -1 #once collision occurs , no longer ith collision
                #Update x,v,T for i and i + 1
                x[i] = x[i] + v[i]*(t - T[i])
                x[i+1] = x[i+1] + v[i+1]*(t - T[i+1])
                v[i],v[i+1]= ( v[i]*( M[i] - M[i+1] )+ 2*M[i+1]*v[i+1] )/(M[i] + M[i+1]),( v[i+1]*( M[i+1] - M[i] )+ 2*M[i]*v[i] )/(M[i] + M[i+1])
                T[i] = t
                T[i+1] = t
                #Update new collision time for i-1 and i+1 th collisions in array and add to Heap
                if i > 0: #if previous colission is there
                    if v[i-1] - v[i] > 0: #if collision possible 
                        x[i-1] = x[i-1] + v[i-1]*(t - T[i-1])
                        T[i-1] = t #Update new time for edit in x[i-1]
                        collision[i-1] = t + (x[i] - x[i-1])/(v[i-1] - v[i])
                        Heap.insert(collision[i-1],i-1)
                if i < n-2: #if next colission is there
                    if v[i+1] - v[i+2] > 0: #if collision possible 
                        x[i+2] = x[i+2] + v[i+2]*(t - T[i+2])
                        T[i+2] = t #Update new time for edit in x[i+1]
                        collision[i+1] = t + (x[i+2] - x[i+1])/(v[i+1] - v[i+2])
                        Heap.insert(collision[i+1],i+1)
                cl = tuple((round(t,4),i,round(x[i],4))) 
                Ans.append(cl)
                m = m - 1 
                if(m==0): # m collsions recorded already
                    break 
    return Ans        

