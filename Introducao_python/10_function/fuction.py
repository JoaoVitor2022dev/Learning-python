def verificar_maioridade(idade):
    if idade >= 18:
         return "Maior de idade"
    else:
         return "Menor de idade"
    
idade_usuario = int(input("Digite sua idade: "))

status = verificar_maioridade(idade_usuario)

print(f"Você é {status}")