def pyt(n):
    sq = []
    for i in range(1, n+1):
        sq.append((i + 2 * i ** 2 - i) // 2)
    for j in range(1, n):
        sum = 0
        for l in range(j, n):
            sum = sq[j] + sq[l]
            for m in range(0, n):
                pythogori = []
                if sum == sq[m]:
                    pythogori.append(sq[j])
                    pythogori.append(sq[l])
                    pythogori.append(sq[m])
                    res = list(map(lambda x: int(x**(1/2)), pythogori))
                    print(res)
pyt(100)