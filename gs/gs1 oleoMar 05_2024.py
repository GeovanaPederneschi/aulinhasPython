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
        entrada = str(input(f"Digite a entrada da posição {coluna},{linha}: "))
        linha += 1
        Linha.append(entrada)
    Coluna.append(Linha)

isOleo = False

colAnalisada = 0
linhAnalisada = 0

for col in Coluna:
    colAnalisada += 1
    for l in col:
        linhAnalisada += 1
        if l == '0':
            isOleo = True
            break
        if colAnalisada == len(Coluna) and linhAnalisada == len(Coluna):
            print("foi")
            break

for iC in range(len(Coluna)):
    endI = ""
    for iL in range(len(Coluna)):
        if iL == len(Coluna):
            endI = "\n"
        print(f"{Coluna[iC][iL]}, ", end=endI)

# print(Coluna[0:2])
# print(Coluna[0:1])
# print(Coluna[1:2])
# print(Coluna)
