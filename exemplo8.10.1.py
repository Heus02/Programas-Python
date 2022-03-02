# Exemplo 8.10.1

nomes = ["Ana", "Carlos", "Maria"]
for tentativa in range (3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print (nomes[i])
    except ValueError as e:
        print (f"Algo de errado aconteceu: {e}")
    finally:
        print (f"Tentativa {tentativa + 1}");
    


