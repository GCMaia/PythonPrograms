dic = {}

arq_entrada = "baboon.pgm"
arq_saida = "baboon.pgm"('informe o novo nome do arquivo e a extensão: ')

proj = open(arq_entrada, "r")

formato = proj.readline()  # P2

tamanho = proj.readline()  # 512, 512
tamanho0 = tamanho
tamanho = tamanho.split(" ")
tamanho1 = tamanho[0]
tamanho2 = tamanho[1]

escala = proj.readline()  # 255

matriz = proj.readlines()  # valores da imagem
print matriz
proj2 = open(arq_saida, "w")
proj2.write(formato)
proj2.write(tamanho0)
proj2.write(escala)

for x in range(len(matriz)):
    lista = matriz[x].split(" ")
    lista[-1] = lista[-1][:-2]
    lista.remove('')

    for i in range(len(matriz)):
        dic[x, i] = lista[i]
        dic[x, i] = int(dic[x, i])

for i in range(int(tamanho1)):
    for j in range(int(tamanho2)):
        if i - 1 < 0:
            z1 = 0
            z2 = 0
            z3 = 0
            if j - 1 < 0:
                z1 = 0
                z4 = 0
                z7 = 0
                z5 = dic[i, j]
                z6 = dic[i, j + 1]
                z8 = dic[i + 1, j]
                z9 = dic[i + 1, j + 1]
            elif j + 1 > int(tamanho2) - 1:
                z3 = 0
                z4 = dic[i, j - 1]
                z5 = dic[i, j]
                z6 = 0
                z7 = dic[i + 1, j - 1]
                z8 = dic[i + 1, j]
                z9 = 0
            else:
                z4 = dic[i, j - 1]
                z5 = dic[i, j]
                z6 = dic[i, j + 1]
                z7 = dic[i + 1, j - 1]
                z8 = dic[i + 1, j]
                z9 = dic[i + 1, j + 1]
        elif i + 1 > int(tamanho1) - 1:
            z7 = 0
            z8 = 0
            z9 = 0
            if j - 1 < 0:
                z1 = 0
                z4 = 0
                z7 = 0
                z2 = dic[i - 1, j]
                z3 = dic[i - 1, j + 1]
                z5 = dic[i, j]
                z6 = dic[1, j + 1]
            elif j + 1 > (int(tamanho2)) - 1:
                z3 = 0
                z6 = 0
                z1 = dic[i - 1, j - 1]
                z2 = dic[i - 1, j]
                z4 = dic[i, j - 1]
                z5 = dic[i, j]
            else:
                z1 = dic[i - 1, j - 1]
                z2 = dic[i - 1, j]
                z3 = dic[i - 1, j + 1]
                z4 = dic[i, j - 1]
                z5 = dic[i, j]
                z6 = dic[i, j + 1]
        elif j - 1 < 0:
            z1 = 0
            z4 = 0
            z7 = 0
            if i - 1 < 0:
                z2 = 0
                z3 = 0
                z5 = dic[i, j]
                z6 = dic[i, j + 1]
                z8 = dic[i + 1, j]
                z9 = dic[i + 1, j + 1]
            elif i + 1 > (int(tamanho1)) - 1:
                z5 = dic[i, j]
                z2 = dic[i - 1, j]
                z3 = dic[i - 1, j + 1]
                z6 = dic[i, j + 1]
                z7 = 0
                z8 = 0
                z9 = 0
            else:
                z2 = dic[i - 1, j]
                z3 = dic[i - 1, j + 1]
                z5 = dic[i, j]
                z6 = dic[i, j + 1]
                z8 = dic[i + 1, j]
                z9 = dic[i + 1, j + 1]
        elif j + 1 > (int(tamanho2)) - 1:
            z3 = 0
            z6 = 0
            z9 = 0
            if i - 1 < 0:
                z4 = dic[i, j - 1]
                z5 = dic[i, j]
                z7 = dic[i + 1, j - 1]
                z8 = dic[i + 1, j]
            elif i + 1 > (int(tamanho1) + 1):
                z1 = dic[i - 1, j - 1]
                z2 = dic[i - 1, j]
                z4 = dic[i, j - 1]
                z5 = dic[i, j]
            else:
                z1 = dic[i - 1, j - 1]
                z2 = dic[i - 1, j]
                z4 = dic[i, j - 1]
                z5 = dic[i, j]
                z6 = dic[i + 1, j - 1]
                z7 = dic[i + 1, j]
        else:
            z1 = dic[i - 1, j - 1]
            z2 = dic[i - 1, j]
            z3 = dic[i - 1, j + 1]
            z4 = dic[i, j - 1]
            z5 = dic[i, j]
            z6 = dic[i, j + 1]
            z7 = dic[i + 1, j - 1]
            z8 = dic[i + 1, j]
            z9 = dic[i + 1, j + 1]

        novo_z5 = int(((z7 + 2 * z8 + z9 - (z1 + 2 * z2 + z3)) * (z7 + 2 * z8 + z9 - (z1 + 2 * z2 + z3)) + (
                    z3 + 2 * z6 + z9 - (z1 + 2 * z4 + z7)) * (z3 + 2 * z6 + z9 - (z1 + 2 * z4 + z7))) ** 0.5)

        if novo_z5 > int(escala):
            novo_z5 = int(escala)
        arqN = ""
        arqN = str(novo_z5)

        proj2.write(arqN)
        proj2.write(" ")

    proj2.write("\n")

proj.close()
proj2.close()




