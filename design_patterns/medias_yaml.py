import yaml

def calcular_media(notas):
    return sum(notas)/len(notas)

with open('data/notas.yaml', 'r') as file:
    dados = yaml.safe_load(file)

for aluno in dados['alunos']:
    nome = aluno['nome']
    notas = aluno['notas']
    media = calcular_media(notas)
    print(f'A média das notas de {nome} é {media:.2f}.')