#while

senha_correta = "python123"
tentativa = ''

print("Bem-vindo! Por Favor, digite sua senha. ")

#verificação e loop de repetição 

while tentativa != senha_correta:
    tentativa = input("Digite a senha: ")
    if tentativa != senha_correta:
        print("Senha incorreta. Tente novamente.")

print("Senha correta! Acesso permitido.")


