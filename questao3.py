import random

def jogo():
        
    print("-" * 40)
    print("JOGO DA FORCA")
    print("-" * 40)

    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while(not enforcou and not acertou):
        tentativa = input("Digite a letra: ")
        tentativa = tentativa.strip().upper()

        if tentativa in palavra_secreta: 
            tentativa_correta(palavra_secreta, tentativa, letras_acertadas)
        else:
            erros += 1
            print("Errado! essa letra não faz parte da palavra.")
            print(f"Você errou {erros} de 10 tentativas!")

        enforcou = erros == 10
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Vitória! você ganhou.")
    else:
        print("Derrota! você perdeu. A palavra era: ", palavra_secreta)

def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

    #substituir os espaços pela letra acertada
def tentativa_correta(palavra_secreta, tentativa, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if tentativa == letra:
            letras_acertadas[index] = letra
            
        index += 1

jogo()