salario, imposto, salatual = 0, 0, 0
salario = float(input("Digite o valor bruto do salário: R$ "))

if salario <= 1900:
    print(f"Valor isento de imposto.")
elif salario <= 2800:
    imposto = salario * 0.05
    salatual = salario - imposto
    print(f"O valor do salário atual, descontado o imposto de 5% é: R$ {salatual}")
    print(f"Salário bruto: R$ {salario}")
    print(f"Imposto: R$ {imposto}")
elif salario <= 3500:
    imposto = salario * 0.10
    salatual = salario - imposto
    print(f"O valor do salário atual, descontado o imposto de 10% é: R$ {salatual}")
    print(f"Salário bruto: R$ {salario}")
    print(f"Imposto: R$ {imposto}")
elif salario <= 4600:
    imposto = salario * 0.15
    salatual = salario - imposto
    print(f"O valor do salário atual, descontado o imposto de 15% é: R$ {salatual}")
    print(f"Salário bruto: R$ {salario}")
    print(f"Imposto: R$ {imposto}")
else: 
    salatual = salario - 900
    print(f"Deverá ser descontato R$ 900,00 de imposto. Salário atual, descontado o valor do imposto: {salatual}")
    print(f"Salário bruto: R$ {salario}")
