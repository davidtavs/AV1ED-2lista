dolar = 5.05  
euro = 5.32  
iene = 0.034  
real = 1.0  

print("Bem-vindo ao conversor de moedas!")
moeda_origem = input("Digite a moeda de origem (dolar, euro, iene, real): ").lower()
moeda_destino = input("Digite a moeda de destino (dolar, euro, iene, real): ").lower()
quantia = float(input("Digite a quantia a ser convertida: "))

if moeda_origem == "dolar" and moeda_destino == "real":
    resultado = quantia * dolar
elif moeda_origem == "dolar" and moeda_destino == "euro":
    resultado = quantia * dolar / euro
elif moeda_origem == "dolar" and moeda_destino == "iene":
    resultado = quantia * dolar / iene
elif moeda_origem == "euro" and moeda_destino == "dolar":
    resultado = quantia * euro / dolar
elif moeda_origem == "euro" and moeda_destino == "iene":
    resultado = quantia * euro / iene
elif moeda_origem == "euro" and moeda_destino == "real":
    resultado = quantia * euro
elif moeda_origem == "iene" and moeda_destino == "dolar":
    resultado = quantia * iene / dolar
elif moeda_origem == "iene" and moeda_destino == "euro":
    resultado = quantia * iene / euro
elif moeda_origem == "iene" and moeda_destino == "real":
    resultado = quantia * iene
elif moeda_origem == "real" and moeda_destino == "dolar":
    resultado = quantia * real / dolar
elif moeda_origem == "real" and moeda_destino == "euro":
    resultado = quantia * real / euro
elif moeda_origem == "real" and moeda_destino == "iene":
    resultado = quantia * real / iene
else:
    resultado = "Conversão não suportada"

if resultado != "Conversão não suportada":
    print(f"quantia {moeda_origem} equivale a {resultado} {moeda_destino}.")
else:
    print("Conversão não suportada.")


