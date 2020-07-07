valor = int(input())
qtdCed = 0

cedulas = [100,50,20,10,5,2,1]
qtddeCed = [0,0,0,0,0,0,0]
print(valor)

for cedula in cedulas:
    qtdCed = valor//cedula
    qtddeCed[cedulas.index(cedula)] = qtdCed
    valor = valor%cedula


for qtd in qtddeCed:
    #print(qtddeCed.index(qtd))
    destroyer = qtddeCed.index(qtd)

    print("{} nota(s) de R$ {},00".format(qtd,cedulas[qtddeCed.index(qtd)]))

    qtddeCed[destroyer] = -1