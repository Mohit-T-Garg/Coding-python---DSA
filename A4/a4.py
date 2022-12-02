from mimetypes import init
import random
import math
from unittest import result

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)

# return appropriate N that satisfies the error bounds
def findN(eps,m):
	#we know eps=log2d*2*log2N/N which means N/Log2N=2log2d/eps Also d-->log2(26)*m
	v = 2*m*math.log(26)/(math.log(2)*eps)
	i = v #Iteratively put n in log to get new n till it converges to integer
	while i!=v*math.log(i)//math.log(2):
		i = v*math.log(i)//math.log(2)
	return i+1	#since we have taken mod , we can take next number even in case of equality it does not hurts to take 1 greater



# Return sorted list of starting indices where p matches x
def modPatternMatch(q,p,x):
	n = len(x)
	m = len(p)
	a = 26**(m-1) % q
	i = 0
	check = value(p,q) #O(mlogq)
	val = value(x[0:m],q) #O(mlogq)
	Result= []
	
	if check==val:
		Result = Result + [0]
	i=1	
	while i+m<=n:#O((n-m)logq)
		val = (((val - identify(x[i-1])*a)*26)%q + identify(x[i+m-1])) %q 
		if val == check:
			Result.append(i)
		i=i+1
	return Result	

# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q,p,x):#Similar just take out pth value each time while comparison
	w=-1	
	n = len(x)
	m = len(p)
	a = 26**(m-1) % q	
	for i in range(m):
		if p[i]=="?":
			w=i
			break
	check = 0
	for i in range(m):
		if i!=w:
			check = (check + (26**(m-i-1))*identify(p[i]) ) % q

	i = 0
	val = value(x[0:m],q)
	Result= []
	
	if check==(val-identify(x[i+w])*26**(m-w-1))%q:
		Result = Result + [0]
	i=1	
	while i+m<=n:
		val = ( ( ( val - identify(x[i-1])*a )*26 ) + identify(x[i+m-1]) ) %q
		if check==(val-identify(x[i+w])*26**(m-w-1))%q:
			Result.append(i)
		i=i+1
	return Result	


#Identify value of character
d = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
def identify(c):
	return d[c]-1

#Get value of a string
def value(s,q):
	val = 0
	n=len(s)
	for i in range(n):
		val = (val + (26**(n-i-1))*identify(s[i]) ) % q
	return val
