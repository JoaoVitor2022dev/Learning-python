
NumeroParcelas = int(input("Em quantas parcelas você precisa parcelar esse produto ? "))

divida = 3000; 

for i in range(1,NumeroParcelas):
      valorParcela = divida / NumeroParcelas
      print(f"{i} - parcela: R$ {valorParcela}")

# para que ele vá pulando de 2 é só usar desta maneira 
for i in range(1,10,2):
      print(i)
      