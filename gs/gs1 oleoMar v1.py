# link da porcaria do video

numLinhaColuna = int(input("Digite o número de linhas/colunas da matriz quadrada que representa a área do mar: "))
Linha = []

print(f"\n(A) para água e (O) para óleo\n")
for numL in range(numLinhaColuna):
    Coluna = []
    for numC in range(numLinhaColuna):
        while True:
            entrada = str(input(f"Digite a entrada da posição {numC+1},{numL+1}: "))
            if entrada != 'A' and entrada != 'O':
                print("Entrada Incorreta!   Digite Apenas (A) para água e (O) para óleo")
            else:
                break
        Coluna.append(entrada)
    Linha.append(Coluna)

isOleo = False

colAnalisada = 0
linhAnalisada = 0

for lin in Linha:
    linhAnalisada += 1
    colAnalisada = 0
    for c in lin:
        colAnalisada += 1
        if c == 'O':
            isOleo = True
            break
    if isOleo:
        break

print(linhAnalisada)
print(colAnalisada)

print(f"\nMatriz Analisada: ")

for iL in range(linhAnalisada):
    endI = ""
    virgula = ","
    if iL == linhAnalisada - 1:
        for iC in range(colAnalisada):
            if iC == len(Linha) - 1:
                endI = "\n"
                virgula = ""
            print(f"{Linha[iL][iC]}{virgula} ", end=endI)
    else:
        for iC in range(len(Linha)):
            if iC == len(Linha)-1:
                endI = "\n"
                virgula =""

            print(f"{Linha[iL][iC]}{virgula} ", end=endI)


totalElementos = len(Linha) * len(Linha)
elementosAnalisados = (linhAnalisada-1)*numLinhaColuna+colAnalisada
porcentagemAnalisada = (elementosAnalisados / totalElementos) * 100

print(f"\nMatriz Analisada: {porcentagemAnalisada:.2f}%\n\n")

if isOleo:
    print(f"Macha de Óleo Dectada!")
else:
    print(f"Mancha de Óleo Não Dectada!")