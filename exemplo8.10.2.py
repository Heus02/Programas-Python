# Exemplo 8.10.2

nomes = ["Ana", "Carlos", "Maria"]
try:
    i = int(input("Digite o índice que quer imprimir: "))
    print (nomes[i])
except ValueError as e:
    print (f"Digite um número!")
finally:
    print (f"Sempre o finally é executado");
    


