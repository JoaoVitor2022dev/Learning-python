""""
1 - MEMBROS: Para representar os mebros da academia 
2 - TREINO: Para representar os treinos dos membros:
3 - ACADEMIA: Para gerenciar os membros e seus treinos, 
permitindo adicionar, listar e salvar essas informações em um arquivo texto 

"""

# BACK END 

class Membro:
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade = idade
        self.treinos =[]

    def adicionar_treino(self, treino):
        self.treinos.append(treino)

    def mostrar_informacoes(self):
        info = f'Nome: {self.nome}, idade: {self.idade}, \n'       
        for treino in self.treinos:
            info +=  f'\n - {treino.descricao}'
        return info


class Treino:
    def __init__(self, descricao, duracao, data):
        self.descricao = descricao
        self.duracao = duracao
        self.data = data

    def mostrar_informacao(self):
        return f'Descrição: {self.descricao}, Duração: {self.descricao}, Data: {self.data}'    


class Academia:
    def __init__(self):
        self.membros = []

    def adicionar_membro(self, membro):
        self.membros.append(membro) 

    def listar_membros(self):
        for membro in self.membros:
            print(membro.mostrar_informacoes()) 

    def salvar_membros_em_arquivos(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            for membro in self.membros:
                arquivo.write(f'{membro.nome} e {membro.idade}')    
                for treino in membro.treinos:
                    arquivo.write(f'{treino.descricao}, {treino.duracao}, {treino.data}')            
        print(f'Membros e treinos salvos com sucesso!')    

# FRONT END

def main():
    academia = Academia()

    while True:
        print("\n1. Adicionar Membro")
        print("2. Adicionar treino ao mebros")
        print("3. Listar Membros e treinos")
        print("4. Salvar Membros e treinos")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite seu nome: ")
            idade = input("Digite seu idade: ")
            membro =  Membro(nome, idade)
            academia.adicionar_membro(membro)

            print("Membro adicionado com sucesso!")

        elif escolha == '2':
            nome = input("Digite a descrição do treino: ") 
            for membro in academia.membros:
                if membro.nome == nome:
                    descricao = input("Digite a descrição de treino: ")   
                    duracao = input("Digite a duração do treino: ")
                    data = input("Digite a data do treino: ")
                    treino = Treino(descricao, duracao, data)
                    membro.adicionar_membro(treino)
                    print("Treino adicionado com sucesso!")
                    break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


