distancia = int(input("Digite a distância que você deseja percorrer em km: "))

if distancia <= 200:
    valor = distancia*0.50
    print("Valor da viagem ", valor)
else:
    valor = distancia*0.45
    print("Valor da viagem ", valor)
