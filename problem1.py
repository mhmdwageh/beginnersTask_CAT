def minRublesSpent(n, m, a, b):
   return (n // m) * b + min(b, (n % m) * a)


n, m, a, b = map(int, input().split())  
print(minRublesSpent(n, m, a, b)) 