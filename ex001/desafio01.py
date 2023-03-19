def valor_total (quantidade, valor_unitario, moeda="real"):
    valor_bruto = valor_unitario * quantidade
    if moeda == 'real':
         resultado=valor_bruto
         return print(f"Valor total: R$ {resultado}.")
    elif moeda == 'euro':
         resultado=valor_bruto * 5.70
         return print(f"Valor total: R$ {resultado}.")
    elif moeda == 'dólar':
         resultado=valor_bruto * 5
         return print(f"Valor total: R$ {resultado}.")
    else:
        print("Digite uma moeda válida!")
        return 0

valor_pagar = valor_total(quantidade=10, valor_unitario=50, moeda="euro")
print(f"{valor_pagar}")


