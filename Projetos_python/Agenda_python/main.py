class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def mostrar_informacoes(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}, E-mail: {self.email}'
    
class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def listar_contatos(self):
        for contato in self.contatos:
            print(contato.mostrar_informacoes())        

## Entrada de dados 

def main():
    agenda = Agenda()

    while True:
        print("1. Adicionar Contato")
        print("2. Listar Contato")
        print("3. Sair")
        escolha = int(input("Escolha uma opção: ")) 

        if escolha == '1': 
            nome =      input("Nome: ")
            telefone =  input("Telefone: ")
            email =     input("E-mail: ")
            
            contato = Contato(nome,telefone,email)
            
            agenda.adicionar_contato(contato) 

            print("Contato registrado com sucesso!") 
