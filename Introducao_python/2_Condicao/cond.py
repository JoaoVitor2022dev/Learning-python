#Condição 

password =  int(input("Crie uma senha: "))

verific = int(input("Digite novamente a sua senha: "))

if password != verific:
    print("Senha incorreta")

else: 
    print("Senha criada com sucesso!")

    