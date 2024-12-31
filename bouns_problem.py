def isCanDistribute(a,b,c,n):
    coinsPerOne = a+b+c+n
    if (coinsPerOne) %3 ==0 and  coinsPerOne >= max(a,b,c):
            return "YES"
    else:
        return "NO"
        

t = int(input())
while(t):
    a,b,c,n = map(int, input().split())
    print(isCanDistribute(a,b,c,n))
    t = t-1