cadastro = {"55586798958": ["Tainara", 1967, "Diadema", "SP"],
            "55586798957": ["Fernando", 1987, "São João da Boa Vista", "SP"],
            "55527425839": ["Geovana", 2005, "São Paulo", "SP"],
            "36317871892": ["Ana Clara", 2004, "São Paulo", "SP"],
            "47415915810": ["Fernanda", 2003, "São Paulo", "SP"]
            }

for chave, valores in cadastro.items():
    print()
    print("Nome: ", valores[0])
    print("CPF: ", chave)
    print("Ano de Nascimento: ", valores[1])
    print(f"Cidade e Estado de nascimento: , {valores[2]}/{valores[3]}\n")

print()

while True:
    cpf = input("Digite o cpf da pessoa: ").lower()
    if cpf == "fim":
        break
    if cpf in cadastro:
        print(cadastro[cpf])
    else:
        print("Cpf não encontrado!")