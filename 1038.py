def transFloat(lista):
    try:
        lista_float = [float(num) for num in lista]
        return lista_float
    except:
        return exit(0)

TabeladeLanche = {'1' : 4.00, '2' : 4.50, '3' : 5.00, '4' : 2.00, '5' : 1.50}
pedidos = input()
pedido_lista = pedidos.split()

codigo = pedido_lista[0]
qtd = int(pedido_lista[1])

total = qtd*TabeladeLanche[codigo]

print("Total: R$ {0:.2f}".format(total))



