# ordem de precedência: parênteses, exponenciação, multiplicação e divisão, soma e subtração.

a=2
b=0.5
c=1
x=input("Digite o valor de x: ")

x = float(x) #conversão da string para o tipo float (número)

y = a * x ** 2 + b * x + c

print(f"O resultado de y para x = {x} é {y}.")