#armstrong
def strong(n):
    def calc(n):
        string = str(n)
        a = len(string)
        digits = []
        sum = 0
        for i in range (0, a):
            d = (n % (10 ** (i+1))) // 10**i
            digits.insert(i, d)
        for j in  range(0, a):
            sum += digits[j] ** a
        return(sum)
    calc(n)
    if calc(n) == (n):
        return(f"Yes, {n} is an Armstrong number.")
    else:
        return(f"No, {n} is not an  Armstrong number, you ***** .")
print(strong(1000))
    

    



    
    
