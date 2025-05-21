def quad(a, b, c):
    m = -b / (2 * a)
    e = m + (m ** 2 - c/a) ** (1/2)
    d = m - (m ** 2 - c/a) ** (1/2)
    return(f"x1 = {e} \nx2 = {d}")


a = float(input("Enter the co-ordinate of x^2, or a: "))
b = float(input("Enter the co-ordinate of x, or b: "))      
c = float(input("Enter the constant term, or c: "))
print(quad(a, b, c))