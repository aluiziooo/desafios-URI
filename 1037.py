def transFloat(valor):
    try:
        valor_float = float(valor)
        return valor_float
    except:
        return exit(0)

valor = input()
valor = transFloat(valor)

if (valor >= 0 and valor <= 25):
    print("Intervalo [0,25]")
elif(valor <= 50 and valor >25):
    print("Intervalo (25,50]")
elif(valor <= 75 and valor > 50):
    print("Intervalo (50,75]")
elif(valor > 75 and valor <= 100):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")