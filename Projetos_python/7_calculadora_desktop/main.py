# calculadora 

def adicionar(a,b):
    return a + b

def subitrair(a,b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b== 0:
        return "Não pode dividir por zero, matematica básica"
    return a / b;

def menu():

    while True:
     print("Selecione a operação:")
     print("1. Adição")
     print("2. Subtração")
     print("3. Multiplicação")
     print("4. Divisão")
     print("5. Sair")
     print("Digite sua escolha (1/2/3/4/5)")

     escolha = input("Digite a sua escolha: ") 
    
     if escolha == "5":
        print("Saindo do sistema...")
        break

     num1 = float(input("Digite o primeiro número: "))
     num2 = float(input("Digite o segundo número: "))

     if escolha == "1":
         print(f"{num1} + {num2} = {adicionar(num1,num2)}")

     elif escolha == '2':
         print(f"{num1} - {num2} = {subitrair(num1,num2)}")

     elif escolha == '3':
         print(f"{num1} - {num2} = {multiplicar(num1,num2)}")

     elif escolha == '4':
         print(f"{num1} - {num2} = {dividir(num1,num2)}") 
     else: 
         print("Escolha inválida.")    

menu()    