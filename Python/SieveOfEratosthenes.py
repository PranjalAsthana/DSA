n = 1800
sieve = [1]*(n+1)
for i in range(2,n+1):
    if(sieve[i]==1):
        for j in range(i,(n+2)//i):
            sieve[i*j] = 0
for i in range(2,n+1):
    if sieve[i]==1:
        print(i, end=" ")
