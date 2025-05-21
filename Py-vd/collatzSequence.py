#Collatz
import evenTester
def col(n):
    yes = [n]
    while n > 1:
        if evenTester.check(n) == 1:
            n = 3 * n + 1
            yes.append(n)
        else:
            n = n // 2
            yes.append(n)
    return(yes, len(yes))

print(col(100))