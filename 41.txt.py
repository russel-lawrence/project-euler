# coding: utf-8
def prime(x):
	if x==2 or x==3:
		return True
	if x==1 or x%2==0 or x%3==0:
		return False
	gex=True
	i,w=5,2
	while i*i<=x:
		if x%i==0:
			return False
		i+=w
		w=6-w
	return True
def pand(l):
    pqr=[]
    abc=[]
    for v in range(1,len(str(l))+1):
        abc.append(v)
    for t in str(l):
        if t not in pqr and int(t)!=0:
            pqr.append(int(t))
        else:
            break
    pqr.sort()
    if pqr==abc:
        pqr=[]
        return True
    else:
        pqr=[]
        return False
    
a=[]
p,q=5,2
while(p<9876543):
    if pand(p):
        if prime(p):
            a.append(p)
    p+=q
    q=6-q
print(a[-1])
    
