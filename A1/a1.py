
class stack: #create stack class
    s = []
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
        
def step(c,temp):#defines command given and apply to x,y,z,d
    if c=="+X":
        temp[0] = temp[0] + 1
        temp[3] = temp[3] + 1
    elif c=="-X":
        temp[0] = temp[0] - 1
        temp[3] = temp[3] + 1
    if c=="+Y":
        temp[1] = temp[1] + 1
        temp[3] = temp[3] + 1
    elif c=="-Y":
        temp[1] = temp[1] - 1
        temp[3] = temp[3] + 1
    if c=="+Z":
        temp[2] = temp[2] + 1
        temp[3] = temp[3] + 1
    elif c=="-Z":
        temp[2] = temp[2] - 1
        temp[3] = temp[3] + 1  
    return temp  
    
    
def findPositionandDistance(p):
    s2 = stack()  #stack containg current answer under current m
    s2.push([0,0,0,0])  #initialize answer of overall string
    st = stack()  #stack containing ( , ) , number
    l = ['0','1','2','3','4','5','6','7','8','9'] #check numerical charater
    i = 0 #iterating over string on parameter i
    while i < len(p):
        if p[i] in l: #getting and storing number in string
            j = 0
            while p[i+j] in l:
                j = j + 1
            st.push(p[i:i+j]) #add number str to stack
            i = i + j
        elif p[i]=='+' or p[i]=='-':#perform command on outermost answer stack
            temp = s2.pop()
            step(p[i:i+2],temp)
            s2.push(temp)
            i = i + 2
        elif p[i] == '(':#add new corresponding ans array to answer stack and '(' to operation stack
            st.push('(')
            s2.push([0,0,0,0])
            i = i+1
        elif p[i]==')':
            temp = s2.pop() #perform scaling on corresponding answer array
            st.pop()
            ct = int(st.pop())
            temp = [i * ct for i in temp]
            ans = s2.pop() #add it to new current answer array
            ans[0] = ans[0] + temp[0]
            ans[1] = ans[1] + temp[1]
            ans[2] = ans[2] + temp[2]
            ans[3] = ans[3] + temp[3]
            s2.push(ans)
            i = i + 1
    return s2.pop()              
            
                    
                    
    
print(findPositionandDistance('+X+X+X+X4(+Y)2(+Z-Z)'))
