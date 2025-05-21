import primeHunter
def prt(n):
    a = int(n ** (1/2) + 1)
    b = primeHunter.prime(a)
    return b
    
def get(a, b):
    fact = []
    for i in b:
        while a % i == 0 and a // i > 0:
            fact.append(i)
            a = a // i
        else:
            if i == len(b):
                fact.append(a)
    return fact


print(get(999999, prt(999999)))

   


