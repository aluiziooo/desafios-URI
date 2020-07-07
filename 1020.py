N = int(input())
ano = int(N / 365)
mes = int((N % 365) / 30)
dia =  (N % 365 % 30)

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(ano,mes,dia))