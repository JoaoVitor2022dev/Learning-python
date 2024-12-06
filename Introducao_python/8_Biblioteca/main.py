from pathlib import Path

# Criar um arquivo e direcionar seu caminho 
caminho_do_arquivo = Path("clientes_biblioteca.xls")

# Inserção de dados
nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")
numero_do_cartao = input("Digite o número do seu cartão: ")

# Método para escrever no arquivo criado
with caminho_do_arquivo.open(mode='a') as arquivo:
    arquivo.write(f"{nome}, {telefone}, {numero_do_cartao}\n")

print("Cliente criado com sucesso!\n")

# Interação com o cliente
print("Bem-vindo à Biblioteca em Python!")
print("1. Verificar um livro.")
print("2. Verificar os seus dados de cadastro.")
print("3. Sair do sistema.")

escolha = int(input("Escolha qual procedimento você deseja: "))

if escolha == 1:
    print("Escolha um livro.")
elif escolha == 2:
    # Leitura de dados de cadastro
    with caminho_do_arquivo.open(mode='r') as arquivo:
        cadastros = arquivo.readlines()
    
    if cadastros:
        print("Seus dados de cadastro:")
        for linha in cadastros:
            print(linha.strip())
    else:
        print("Nenhum cadastro encontrado.")
else:
    print("Você saiu do sistema.")
