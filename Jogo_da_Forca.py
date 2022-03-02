#Programa 7.2 - Jogo da forca

import random

palavras = [
          "casa",
          "bola",
          "mangueira",
          "uva",
          "quiabo",
          "computador",
          "cobra",
          "lentilha",
          "arroz"
     ]

índice = random.randint(0, 8)

palavra = palavras[ (índice * 776) % len(palavras)]
for x in range (100):
    print ()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print (senha)
    if senha == palavra:
        print ("Você acertou!")
        break
    tentativa = input ("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print ("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print ("Você errou!")
        linha = list ("X------")
        linha [1] = "O"
        print ("X  0  " if erros >= 1 else "X")
        
        if erros == 2:
            linha [2] = "|"
        elif erros == 3:
            linha [3] = "/"
            linha [4] = "/"
        
        elif erros  >= 4:
            linha [2, 3, 4] = "/", "|", "/"
        print (f"X{linha}")
        linha3 = ""
        if erros == 5:
            linha [5] = "/"
        elif erros >= 6:
            linha [5, 6] += "/", "/"
        print (f"X{linha}")
        print (f"X\n========")
        if erros == 6:
            print (f"Enforcado!\n{palavra}")
            break
            
                       
