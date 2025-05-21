def prime():
    n = int(input("Enter thy number: "))
    if n % 6 == 1 or n % 6 == 5:
        i = 2
        while i < int(n ** (1 / 2) + 1):
            div = n % i
            if div == 0:
                return("n is NOT prime.")
                break                      #imp lesson: don't use stufff after break. it wont run cause thel oop will terminate already.
            else: 
                i += 1
        return ("n is prime.")             # or can use 1 if prime, 0 if not.
    else:
        return('n is NOT prime.')
        
print(prime())
            



     
