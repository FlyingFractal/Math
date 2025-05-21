#TO generate the first n rows of the pascal triangle.
import factorial
def pas(n):
    row = []
    for i in range(0, n+1):
        iterite = []
        for j in range(0, i+1):
            iterite.append(j)
        row = list(map(lambda x: factorial.fact(i) // (factorial.fact(i - x) * factorial.fact(x)), iterite))   
        print(row)
pas(int(input("Enter the number: "))) 