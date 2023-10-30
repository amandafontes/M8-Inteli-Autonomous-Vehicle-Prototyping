import csv

def calcular_media(notas):
    return sum(notas) / len(notas)

with open('data/notas.csv', mode='r') as file:
    reader = csv.DictReader(file)
    dados = {}
    for row in reader:
        nome = row['nome']
        nota = float(row['notas'])
        if nome in dados:
            dados[nome].append(nota)
        else:
            dados[nome] = [nota]

for nome, notas in dados.items():
    media = calcular_media(notas)
    print(f'A média das notas de {nome} é {media:.2f}.')
