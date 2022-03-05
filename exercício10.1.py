# Exercício 10.1

class Televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.marca = 'LG'
        self.tamanho = 32 
tv = Televisão ()
print(tv.ligada)
print(tv.canal)

tv_sala = Televisão()
tv_sala.ligada = True
tv_sala.canal = 4
print (tv.canal)
print(tv_sala.canal)

print(tv.marca)
print(f"{tv.tamanho} polegadas")
