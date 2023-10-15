import random

nsecreto = random.randint(1, 50)

tent = 0

print("Seja muito bem vindo! esse é o jogo da adivinhação, um numero foi gerado entre 1 e 50, você consegue adivinhar?")

while True:
    tent = int(input("Digite um número: "))
    tent += 1

    if tent < nsecreto:
        print("O número é maior.")
    elif tent > nsecreto:
        print("O número é menor.")
    else:
        print(f"Parabéns! Você adivinhou o número secreto, que era: ({nsecreto}) em {tent} tentativas.")
        break
