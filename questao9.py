filmesdisp = [1,2,3]
while True:
    print("Bem vindo ao CinemaDTV! Esses são os filmes em cartaz:")
    # Abre o arquivo para leitura
    with open('cinema.txt', 'r') as arquivo:
    # Lê o conteúdo do arquivo
        conteudo = arquivo.read()
    
    # Imprime o conteúdo no terminal
    print(conteudo)

    filme = int(input("qual das 3 opções você deseja assistir? \n[digite 00 para sair] \nOpção-> "))

    if filme == 1 or 2 or 3:
        while filme == 1:
            hor = str(input("qual horario você deseja assistir ao filme? \n "))
            if hor == "19:00" or hor == "22:00":
                print("voce comprou o ingresso para as: ",hor)
                break
            else: print("horario inválido! os horários disponíveis são: ", conteudo)
        while filme == 2:
            hor = str(input("qual horario você deseja assistir ao filme? \n"))
            if hor == "12:00" or hor == "17:20":
                print("voce comprou o ingresso para as: ",hor)
                break
            else: print("horario inválido! os horários disponíveis são: ", conteudo)
        while filme == 3:
            hor = str(input("qual horario você deseja assistir ao filme? \n"))
            if hor == "17:00" or hor == "20:40":
                print("você comprou o ingresso para as:", hor)
                break
            else:
                print("horario inválido! os horários disponíveis são: ", conteudo)
        break
    if filme == 00:
        print("Saindo...")
        break

    