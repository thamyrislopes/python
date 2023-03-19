texto = """Olá! Hoje é 18/03/2023. O meu nome é Thamyris, tenho 28 anos e sou Pernambucana. Sou formada em Administração, porém atualmente faço faculdade de Análise e Desenvolvimento de Sistemas. Já fiz alguns cursos na área da tecnologia, como: HTML, CSS e (ainda em andamento) o curso de Javascript, ministrado pelo professor Gustavo Guanabara."""

a = 0
e = 0
for i,v in enumerate(texto):
    if v=='a' or v=='e':
        print(f"Vogal '{v}' encontrada na posição {i}")
        if v=='a':
            a = a+1
        if v=='e':
            e = e+1
    else: 
        continue

print(f"Total de vogais A no texto: {a}")
print(f"Total de vogais E no texto: {e}")