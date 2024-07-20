n = 23
sieve = [1]*(n+1)
for i in range(2,n+1):
    if(sieve[i]):
        for j in range(2,(n+1)//i):
            sieve[i*j] = 0
for i in range(2,n+1):
    if sieve[i]==1:
        print(i)
