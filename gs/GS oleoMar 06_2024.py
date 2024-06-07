# https://youtu.be/Xq-cIxkMCc0?feature=shared

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

for lin in Linha:
    for c in lin:
        if c == 'O':
            isOleo = True
            break
    if isOleo:
        break

print(f"\nMatriz: ")

for iL in range(numLinhaColuna):
    endI = ""
    virgula = ","
    for iC in range(numLinhaColuna):
        if iC == numLinhaColuna-1:
            endI = "\n"
            virgula = ""
        print(f"{Linha[iL][iC]}{virgula} ", end=endI)

if isOleo:
    print(f"\nMacha de Óleo Dectada!")
else:
    print(f"\nMancha de Óleo Não Dectada!")