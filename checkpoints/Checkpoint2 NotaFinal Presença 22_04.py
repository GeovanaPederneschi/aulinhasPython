# geovana carvalho pederneschi 559092
# julia ingrid peixoto farias 559091

semestre = 1
print("\nA porcetagem deve ser de 0 a 100\nAceita números decimais\n")
presenca = float(input(f"\nDigite a presença em porcentagem do aluno na disciplina: "))

while semestre <= 2:
    print(f"\n{semestre}º Semestre")

    print("\nCalcular nota da disciplina no semestre")
    print("\nA nota digitada deve ser de 0 a 100!!\nAceita apenas números inteiros\n")

    checkpoint1 = int(input("Digite a nota do primeiro checkpoint: "))
    checkpoint2 = int(input("Digite a nota do segundo checkpoint: "))
    checkpoint3 = int(input("Digite a nota do terceiro checkpoint: "))

    menorNota = min(checkpoint1, checkpoint2, checkpoint3)

    sprint1 = int(input("Digite a nota da primeira sprint: "))
    sprint2 = int(input("Digite a nota da segunda sprint: "))

    globalSolution = int(input("Digite a nota da global solution: "))

    checkpoint = int(0)

    if checkpoint1 == menorNota:
        checkpoint = checkpoint2 + checkpoint3
    elif checkpoint2 == menorNota:
        checkpoint = checkpoint1 + checkpoint3
    else:
        checkpoint = checkpoint1 + checkpoint2

    nota40 = (checkpoint + sprint1 + sprint2)/4

    if semestre == 1:
        notaPrimeiroSemestre = (nota40*0.4) + (globalSolution*0.6)
    elif semestre == 2:
        notaSegundoSemestre = (nota40*0.4) + (globalSolution*0.6)
        notaFinal = (notaPrimeiroSemestre*0.4) + (notaSegundoSemestre*0.6)

    semestre += 1

print(f"\nSua nota final é {notaFinal:.0f}")
print(f"A presença final foi de {presenca}%")

if notaFinal >= 60 and presenca >= 75.0:
    print("Aluno Aprovado")
elif notaFinal >= 40 and presenca >= 75.0:
    print("Exame!!")
else:
    print("Aluno Reprovado")

    if notaFinal<40:
        print("Reprovado por nota")
    if presenca < 75.0:
        print("Reprovado por falta")


