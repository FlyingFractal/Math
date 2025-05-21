def gcd():
    n = int(input('Enter the first number: '))
    m = int(input('Enter the second number: '))
    num = []
    if n > m:            #my method to keep it working even if user inputs them wrongly.
        num.insert(0, n)
        num.insert(1, m)
    else: 
        num.insert(0, m)             
        num.insert(1, n)  
   
    if num[0] % num[1] == 0:
        return (num[1])
    else: 
        j = 0
        num.insert(2, num[j] % num[j+1])
        while num[j+1] % num[j+2] > 0:
            num[j+1] % num[j+2]
            j += 1
        else: 
            return (num[j+2])

print(gcd())
