T= int(input())

def makePrimeList(num):
    primeNum={i for i in range(2,num+1)}

    for i in range(2, int(num**0.5)+1):
        cnt=0

        while (i*(i+cnt))<=num:
            if (i*(i+cnt)) in primeNum: primeNum.remove(i*(i+cnt))
            cnt+=1
    
    return primeNum

primeNum=makePrimeList(10000)

def getGoldbachPartition(num):
    for i in range(num//2, 1, -1):
        if (i in primeNum) and (num-i in primeNum):
            return print(i, num-i)

for _ in range(0, T):
    getGoldbachPartition(int(input()))
