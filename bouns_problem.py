def isCanDistribute(a,b,c,n):
    totalcoins = a+b+c+n
    coinsPerOne = totalcoins / 3
    if (totalcoins) %3 == 0 and  coinsPerOne >= max(a,b,c):
            return "YES"
    else:
        return "NO"
        

t = int(input())
while(t):
    a,b,c,n = map(int, input().split())
    print(isCanDistribute(a,b,c,n))
    t -=1
