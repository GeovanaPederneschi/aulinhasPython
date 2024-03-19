salario = float(input("Digite o salário do funcionário: "))
if salario > 1250.00:
    aumento = (1250.00*0.1)
    salario_reajustado = salario + aumento
    print("O salário reajustado é: ", salario_reajustado)
else:
    aumento = (1250.00*0.15)
    salario_reajustado = salario + aumento
    print("O salário reajustado é: ", salario_reajustado)
