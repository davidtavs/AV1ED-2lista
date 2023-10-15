class CaixaEletronico:
    def __init__(self):
        self.saldo = 0

    def consultar_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} efetuado com sucesso."
        else:
            return "Valor de depósito inválido."

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} efetuado com sucesso."
        elif valor > self.saldo:
            return "Saldo insuficiente."
        else:
            return "Valor de saque inválido."

def main():
    caixa = CaixaEletronico()

    while True:
        print("\nBem-vindo ao Caixa Eletrônico")
        print("1. Consultar Saldo")
        print("2. Depositar Dinheiro")
        print("3. Sacar Dinheiro")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print(caixa.consultar_saldo())
        elif escolha == "2":
            valor = float(input("Digite o valor a ser depositado: R$"))
            print(caixa.depositar(valor))
        elif escolha == "3":
            valor = float(input("Digite o valor a ser sacado: R$"))
            print(caixa.sacar(valor))
        elif escolha == "4":
            print("Obrigado por usar o Caixa Eletrônico. Tenha um bom dia!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
