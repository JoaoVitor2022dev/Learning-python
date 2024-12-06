class Carro:
    
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}')

    def calcular_idade(self, ano_atual):
        return ano_atual - self.ano       
    

carro1 = Carro("Toyota", "Corola", 2015)
carro2 = Carro("Honda", "Civic", 2018)

carro1.exibir_informacoes()
carro2.exibir_informacoes()

print(f'Idade do carro 1: {carro1.calcular_idade(2024)} anos')
print(f'Idade do carro 2: {carro2.calcular_idade(2024)} anos')