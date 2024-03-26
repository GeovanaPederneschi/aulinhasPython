# geovana carvalho pederneschi 559092
# julia ingrid peixoto farias 559091

print("1º Semestre")

print("\nA nota digitada deve ser de 0 a 100!!\n")

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

notaPrimeiroSemestre = (nota40*0.4) + (globalSolution*0.6)

print("\n2º Semestre")
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

notaSegundoSemestre = (nota40*0.4) + (globalSolution*0.6)

notaFinal = (notaPrimeiroSemestre*0.4) + (notaSegundoSemestre*0.6)


print("\nSua nota final é ", notaFinal)

if notaFinal >= 60:
    print("Aluno Aprovado")
elif notaFinal >= 40:
    print("Exame!!")
else:
    print("Aluno Reprovado")


