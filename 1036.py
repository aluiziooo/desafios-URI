def transFloat(lista):
    try:
        lista_float = [float(num) for num in lista]
        return lista_float
    except:
        return exit(0)

valores = input()
valores_lista = valores.split()
valores_lista = transFloat(valores_lista)

A = valores_lista[0]
B = valores_lista[1]
C = valores_lista[2]

B_minus = -1*B
Delta = B**2 - 4*A*C
a2 = 2*A

if(Delta < 0 or a2 == 0):
    print("Impossivel calcular")
    exit()
else:
    X_linha = (B_minus + Delta**0.5)/a2
    X_duas_linhas = (B_minus - Delta**0.5)/a2

print("R1 = {0:.5f}".format(X_linha))
print("R2 = {0:.5f}".format(X_duas_linhas))