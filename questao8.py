
peso = float(input("Digite seu peso, em Kg: "))

altura = float(input("Digite sua altura em metros: \n[ultilize o '.' para dividir metros e centimetros] "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Peso ideal")
elif 25 <= imc < 30:
    print("Acima do peso")
else:
    print("Obesidade.")
