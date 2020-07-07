# FUNÇÕES
def is_float(valor):
    try:
        float(valor)
        return True
    except:
        return False


def is_negative(valor, cent):
    valor -= cent
    if valor < 0:
        return True
    else:
        return False


# VARIAVEIS
valor = float(input())
notas = [10000, 5000, 2000, 1000, 500, 200]
centavos = [100, 50, 25, 10, 5, 1]
qtd_notas = [0, 0, 0, 0, 0, 0]
qtd_centavos = [0, 0, 0, 0, 0, 0]
qtd_var = 0

# CORPO DO CÓDIGO
while (True):
    if is_float(valor):
        valor = float(valor)
        if (valor >= 0) and (valor <= 1000000.00):
            break
        else:
            valor = input()
    else:
        valor = input()

valor = int(valor * 100)
for nota in notas:
    qtd_var = valor // nota
    valor = valor % nota
    qtd_notas[notas.index(nota)] = qtd_var
for cent in centavos:
    qtd_var = valor // cent
    if is_negative(valor, cent):
        continue
    valor = valor%cent
    qtd_centavos[centavos.index(cent)] = qtd_var

print("NOTAS:")
for qtd in qtd_notas:
    destroyer = qtd_notas.index(qtd)
    nota = (notas[qtd_notas.index(qtd)]//100)
    print("{} nota(s) de R$".format(qtd),"{0:.2f}".format(nota))

    qtd_notas[destroyer] = -1
print("MOEDAS:")
for qtd in qtd_centavos:
    destroyer = qtd_centavos.index(qtd)
    centavo = (centavos[qtd_centavos.index(qtd)]/100)
    print("{} moeda(s) de R$".format(qtd),"{0:.2f}".format(centavo))

    qtd_centavos[destroyer] = -1
