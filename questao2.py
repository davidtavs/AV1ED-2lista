
lista = []
arq2 = open("agenda.csv", "r")
lista = arq2.readlines()
arq2.close

def menu():
    print("\n", "-" * 40)
    print("1 - Adicionar um novo contato")
    print("2 - Excluir contato")
    print("3 - Listar contatos")
    print("4 - Sair")

def lista_agenda(nome, telefone, opcao):
    if (opcao ==1):
        contato = nome+";"+telefone+"\n"
        lista.append(contato)
        lista.sort()

        print("Contato adicionado a agenda!")
        
        print(lista)
    if (opcao ==2):
        tamanho = len(lista)
        for i in range(tamanho):
            print(i,"-",lista[i])
        delete = int(input("Qual contato deseja apagar? "))
        lista.pop(delete)
        print("Contato excluido")
    if(opcao==3):
        tamanho = len(lista)
        for i in range(tamanho):
            print(lista[i])

    arq = open("agenda.csv", "w")
    tamanho = len(lista)

    for i in range(tamanho):
        arq.write(lista[i])
    arq.close()    


o = 0
while True:

    menu()
    o = int(input("Opção: "))

    if (o==1):
        n = input("Digite um nome: ")
        t = input("Digite o numero do celular: ")
        lista_agenda(n,t,1)

    if(o==2):
        lista_agenda(0,0,2)

    if(o==3):
        lista_agenda(0,0,3)
    if(o==4):
        break    