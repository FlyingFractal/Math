def euler(n):
    a = n//3
    b = n //5
    summa_a = 3 * (a**2 + a)//2
    summa_b = 5 * (b**2 + b)//2
    res = summa_a + summa_b
    return(res)

print(euler(999))