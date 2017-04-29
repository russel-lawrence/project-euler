import math
s, num = 2, 3
while num <= 2000000:
    t = True
    for i in range(3,int(math.sqrt(num))+1,2):
        t = t and num%i != 0
    if t == True:
        s = s+num
    num = num + 2
print(s)


