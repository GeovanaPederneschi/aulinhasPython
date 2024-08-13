cadastro = {"55586798958": ["Tainara", 1967, "Diadema"],
            "55586798957": ["Fernando", 1987, "São João da Boa Vista"],
            "55527425839": ["Geovana", 2005, "São Paulo"],
            "36317871892": ["Ana Clara", 2004, "São Paulo"],
            "47415915810": ["Fernanda", 2003, "São Paulo"]
            }

print(cadastro)

print(cadastro["55586798958"])

cadastro["55586798958"][1] = 1995

print(cadastro["55586798958"])

del cadastro["55586798958"]
print(cadastro)
print("55586798958" in cadastro)

print(cadastro.keys())
print(cadastro.values())