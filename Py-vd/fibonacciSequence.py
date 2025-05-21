def fib():
    n = int(input('Enter the number: '))
    fibonacci = [0, 1]
    for i in range(0, n-2):
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
    return fibonacci

print(fib())