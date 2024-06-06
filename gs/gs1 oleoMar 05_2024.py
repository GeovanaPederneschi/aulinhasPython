# link da porcaria do video

numLinhaColuna = int(input("Digite o número de linhas/colunas da matriz quadrada que representa a área do mar: "))
Coluna = []

print(f"\n(A) para água e (O) para óleo\n")
for numC in range(numLinhaColuna):
    Linha = []
    for numL in range(numLinhaColuna):
        while True:
            entrada = str(input(f"Digite a entrada da posição {numC+1},{numL+1}: "))
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
    if isOleo:
        break

print(f"\nMatriz Analisada: ")

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


totalElementos = len(Coluna)*len(Coluna)
elementosAnalisados = (colAnalisada-1)*numLinhaColuna+linhAnalisada
porcentagemAnalisada = (elementosAnalisados / totalElementos) * 100

print(f"\nMatriz Analisada: {porcentagemAnalisada:.2f}%\n\n")

if isOleo:
    print(f"Macha de Óleo Dectada!")
else:
    print(f"Mancha de Óleo Não Dectada!")