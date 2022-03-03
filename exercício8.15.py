# Exercício 8.15

ESPAÇOS_POR_NÍVEL = 4

def imprime_elementos (l, nível = 0):
    espaços = ' ' * ESPAÇOS_POR_NÍVEL * nível
    if type(l) == list:
        print (espaços, "[")
        for e in l:
            imprime_elementos (e, nível + 1)

        print (espaços, "]")

    else:
        print (espaços, l)

L=[1, [2,3,4,[5,6,7]]]

imprime_elementos(L)






