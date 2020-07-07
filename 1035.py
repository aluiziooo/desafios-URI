def transInteiro(lista):
    try:
        lista_inteiro = [int(num) for num in lista]
        return lista_inteiro
    except:
        return exit(0)

valInteiros = input()
valInteirosLista = valInteiros.split()
valInteirosLista = transInteiro(valInteirosLista)

A = valInteirosLista[0]
B = valInteirosLista[1]
C = valInteirosLista[2]
D = valInteirosLista[3]

CD = C+D
AB = A+B

if (B > C and D > A and CD > AB and CD > 0 and AB > 0 and A%2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")