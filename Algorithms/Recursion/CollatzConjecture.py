def col(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + col(n//2)
    else:
        return 1 + col(3*n + 1)
    
print(col(6))
    