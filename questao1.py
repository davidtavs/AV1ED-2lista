
total = 0
contagem = 0

while True:
    nota = float(input("Insira a nota (ou digite '000' para finalizar): "))

    if nota == 000:
        break

    if 0< nota <=10:
        nota = float(nota)
        total += nota
        contagem += 1
    else:
        print("Por favor, insira um número válido.")

if contagem > 0:
    media = total / contagem

    if media >= 90:
        nota_correspondente = 'A'
    elif media >= 80:
        nota_correspondente = 'B'
    elif media >= 70:
        nota_correspondente = 'C'
    elif media >= 60:
        nota_correspondente = 'D'
    else:
        nota_correspondente = 'F'

    print(f"Média das notas: {media:.2f}")
    print(f"Nota correspondente: {nota_correspondente}")
else:
    print("Nenhuma nota válida foi inserida.")
