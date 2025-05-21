def prime(n):
    primes = [2, 3]
    candidates = []
    for i in range(1, n // 6 + 1):
        candidates.append(i * 6 - 1)
        candidates.append(i * 6 + 1)
    for j in candidates:
        flag = True
        for l in range(2, int(j ** (1/2) + 1)):
            if j % l == 0:
                flag = False 
        if flag == True:
            primes.append(j)
    return primes


