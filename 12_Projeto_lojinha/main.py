# projeto lojinha 

def cadastro_cliente(nome, email,telefone):
    with open("clientes.txt","a") as arquivo:
        arquivo.write(f"{nome}, {email}, {telefone}\n")
    print("Cliente cadastrado com sucesso!")


# listar dados dos clientes 
def listar_clients():
    try:
        with open("clentes.txt", "r") as arquivo:
            clientes = arquivo.readlines()
            if not clientes:
                print("Nenhum cliente cadastrado.")
            else:
                print("Listar de clientes cadastrados:")
                for cliente in clientes:
                    nome,email,telefone = cliente.strip().split(",")
                    print(f"Nome: {nome}, E-mail: {email}, Telefone: {telefone}") 
    except FileNotFoundError:
        print("Nenhum cliente cadastrado.")                    


# Manipulção do arquivo 
def salvar_em_arquivos(dados, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for dado in dados:
            arquivo.write(f"{dado}")


# Ler arquivos 
def ler_arquivo_de_dados(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            return arquivo.readlines()
    except FileNotFoundError:
        return []    
    

    