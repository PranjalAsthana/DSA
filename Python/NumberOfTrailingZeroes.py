import math
num = 200 # number to find factorial of
c = 0
n = math.floor(math.log(num,5))
#print(n)
for i in range(1,n+1):
    #print(i)
    #print(num//(5**i))
    c += num//(5**i)
print(c)
