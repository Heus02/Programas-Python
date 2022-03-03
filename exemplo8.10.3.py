# Ex. 8.10.3

while True:
    try: 
        v = int(input("Digite um número inteiro (0 sai): "))
        if v == 0:
            break
    except Exception:
        print ("Valor inválido! Redigite")
    else: 
        print ("Parabéns, nenhuma exceção")
    finally:
        print ("Executado sempre, mesmo com o break")