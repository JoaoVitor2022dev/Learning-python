#bliblioteca 
import math 
num = 16
print(math.sqrt(num))


# request 
import requests 

response = requests.get("https://joaovitor2022dev.github.io/")

print(response.text)


# data e horas 

import datetime

now = datetime.datetime.now()

print("Data e hora atuais são ", now)


# Numero aleatorio com intervalo 

import random 

numero_aleatorio = random.randint(1, 100)

print("Numero aleatorio: ", numero_aleatorio)


