# link da porcaria do video

numLinhaColuna = int(input("Digite o número de linhas/colunas da matriz quadrada que representa a área do mar: "))
Coluna = []

coluna = 0
linha = 0

print("(A) para água e (O) para óleo")
for numC in range(numLinhaColuna):
    coluna += 1
    linha = 0
    Linha = []
    for numL in range(numLinhaColuna):
        linha += 1
        while True:
            entrada = str(input(f"Digite a entrada da posição {coluna},{linha}: "))
            if entrada != 'A' and entrada != 'O':
                print("Entrada Incorreta!   Digite Apenas (A) para água e (O) para óleo")
            else:
                break
        Linha.append(entrada)
    Coluna.append(Linha)

isOleo = False

colAnalisada = 0
linhAnalisada = 0

for col in Coluna:
    colAnalisada += 1
    linhAnalisada = 0
    for l in col:
        linhAnalisada += 1
        if l == 'O':
            isOleo = True
            break
        if colAnalisada == len(Coluna) and linhAnalisada == len(Coluna):
            break
    if isOleo:
        break

#print(f"colAnalisada: {colAnalisada}")
#print(f"linhAnalisada: {linhAnalisada}")
#print(f"len(Coluna): {len(Coluna)}")

print("                                     ")
print("Matriz Analisada: ")

for iC in range(colAnalisada):
    endI = ""
    virgula = ","
    if iC == colAnalisada - 1:
        for iL in range(linhAnalisada):
            if iL == len(Coluna) - 1:
                endI = "\n"
                virgula = ""
            print(f"{Coluna[iC][iL]}{virgula} ", end=endI)
    else:
        for iL in range(len(Coluna)):
            if iL == len(Coluna)-1:
                endI = "\n"
                virgula =""

            print(f"{Coluna[iC][iL]}{virgula} ", end=endI)

print("             ")
print("             ")

if isOleo:
    print(f"Macha de Óleo Dectada!")
else:
    print(f"Mancha de Óleo Não Dectada!")