s=0
for i in range(3,1000,3):
	s=s+i
for j in range(5,1000,5):
	if j%3!=0:
		s=s+j
print(s)
