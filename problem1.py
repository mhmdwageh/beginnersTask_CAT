def minRublesSpent(n, m, a, b):
   return min((n // m) * b + min(b, (n % m) * a), n * a)


n, m, a, b = map(int, input().split())  
print(minRublesSpent(n, m, a, b)) 
