cadastro = {"55586798958":["Tainara",1967,"Diadema"],
            "55586798957":["Fernando",1987,"São João da Boa Vista"],
            "55527425839":["Geovana",2005,"São Paulo"],
            "36317871892":["Ana Clara",2004,"São Paulo"],
            "47415915810":["Fernanda",2003,"São Paulo"]
            }

while True:
    cpf = input("Digite o cpf da pessoa: ").lower()
    if cpf == "fim":
        break
    if cpf in cadastro:
        print(cadastro[cpf])
    else:
        print("Cpf não encontrado!")