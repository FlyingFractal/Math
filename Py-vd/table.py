def table():
    n = int(input("Enter the nuumber whose table is to be calculated: "))
    d = []
    for i in range(1,11):
        d.append (n * i)
    return (d)
print(table())