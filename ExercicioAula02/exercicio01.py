import os
os.system('clear')

nome = input("Entre com o produto: ")
valor = float(input("Entre com o valor: "))

if valor > 0:
    desconto = 0
    if valor >= 50 and valor < 200:
        desconto = 0.95
    elif valor >= 200 and valor < 500:
        desconto = 0.94
    elif valor >= 500 and valor < 1000:
        desconto = 0.93
    elif valor >= 1000:
        desconto = 0.92
        
    print(f"Nome: {nome}")
    print(f"Valor: {round(valor,2)}")
    print(f"Valor com desconto {round((valor*desconto), 2)}")

else:
    print("Valor Menor de Zero")