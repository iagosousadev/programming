with open("./alfabeto", "r") as f:
    alfabeto = f.read()
    n = int(input("Informe o valor de n:"))
    P = [x for x in alfabeto]
    for i in range(n-1):
        P = [x + y for x in P for y in alfabeto]

    with open("./permutacoes", "w") as out:
        i = 0
        for x in P:
            out.write(x + " ")
            if i == 9:
                out.write("\n")
            i = (i + 1 ) % 10

