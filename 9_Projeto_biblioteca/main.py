from pathlib import Path

# Criar um arquivo e direcionar seu caminho 
caminho_do_cliente = Path("clientes_biblioteca.txt")

caminho_livros = Path("livros_clientes.txt")

#Gerando o numero do cartão baseado na quantidade de linhas no arquivo de cliente 
try:
    with caminho_do_cliente.open() as arquivo:
        linhas = arquivo.readlines()
        numero_cartao = len(linhas) + 1
except FileNotFoundError:
    numero_cartao = 1

#Solicitando dads do cliente 
nome = input("Digite seu nome: ")          
telefone = input("Digite seu telefone: ")    

# abrindo o arquivo no modo 'a' (append)
with caminho_do_cliente.open(mode='a') as arquivo:
    arquivo.write(f"{nome}, {telefone}, {numero_cartao}\n")

print(f"Cliente cadastrado com sucesso! Seu número de cartão é: {numero_cartao}")    


#Criando a interação do livro
numero_cartao = int(input("Digite seu número de cartão: "))
livros = input("Digite os livros que você quer pegar (separados por vírgula): ")

# Abrindo  arquivo no modo 'a' (append)
with caminho_livros.open(mode='a') as arquivo:
    arquivo.write(f"{numero_cartao}, {livros}\n")

print("livros adicionado com sucesso!")

# Solicitação do numero do cartão 
numero_cartao = int(input("Digite seu numero de cartão: "))
try:
    with caminho_livros.open() as arquivo:
        linhas = arquivo.readlines()
        encontrou = False
        for linha in linhas:
            num_cartao, livros = linha.strip().strip(',',1)
            if int(num_cartao) == numero_cartao:
                print(f"Livros pegados: {livros}")
                encontrou = True
        if not encontrou:
            print("Nenhum livro encontrado para este número do cartão.")
except FileNotFoundError:
    print("Nenhum registro encontrado.")                    
        

