import datetime as datetime

class Carro: 
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def info(self):
        return f'Carro: {self.marca} {self.modelo}, Ano: {self.ano}'
    
    def idade_do_carro(self):
        ano_atual = datetime.now().year
        return ano_atual - self.ano 


carro1 = Carro('Toyota', 'Corrola', 2010)
carro2 = Carro('Honda', 'Civic', 2019) 

print(carro1.info)
print(carro2.info)