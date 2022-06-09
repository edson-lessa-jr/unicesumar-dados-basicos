def main():
    matriz = []
    contador=0
    for i in range(3):
        matriz.append([])
        for j in range(3):
            contador += 1
            matriz[i].append(contador)

    print("Matriz")
    for i in range(len(matriz)):
        linha = ""
        for j in range(len(matriz[i])):
            linha += str(matriz[i][j]) + " "
        print(linha)

    print("-------")
    print("Matriz transposta")

    for i in range(len(matriz)):
        linha = ""
        for j in range(len(matriz[i])):
            linha+= str(matriz[j][i]) + " "
        print(linha)

main()