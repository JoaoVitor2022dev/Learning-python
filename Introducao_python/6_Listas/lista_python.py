# listas 
frutas =[]

while True:
    fruta = input("Digite o nome da fruta para ser cadastrada, caso não digite 'sair'. ")
    if fruta.lower() == 'sair':
        break

    frutas.append(fruta)

print("Lista de frutas")
for fruta in frutas:
    print(fruta)



