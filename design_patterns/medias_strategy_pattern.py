import yaml
import csv

# Criação de classe abstrata para definir a interface de leitura de arquivos
class FileReaderStrategy:
    def __init__(self, filename):
        self.filename = filename

    # Método abstrato de leitura de arquivos
    def read_file(self):
        pass

# Criação de classe que herda de FileReaderStrategy para definir a leitura de um arquivo do tipo yaml
class YAMLFileReader(FileReaderStrategy):
    def read_file(self):
        with open(self.filename, 'r') as file:
            data = yaml.safe_load(file)
        return data['alunos']

# Criação de classe que herda de FileReaderStrategy para definir a leitura de um arquivo do tipo csv
class CSVFileStrategy(FileReaderStrategy):
    def read_file(self):
        dados = {}
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                nome = row['nome']
                notas = [float(row['notas'])]
                if nome in dados:
                    dados[nome].append(notas[0])
                else:
                    dados[nome] = [notas[0]]
        return [{'nome': nome, 'notas': notas} for nome, notas in dados.items()]

# Criação de método para calcular a média das notas, uma vez que elas forem processadas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Criação de método para processar o arquivo do tipo selecionado
def processar_arquivo(filename):
    if filename.endswith('.yaml'):
        reader = YAMLFileReader(filename)
    elif filename.endswith('.csv'):
        reader = CSVFileStrategy(filename)
    else:
        raise ValueError('Formato de arquivo inválido.')
    
    dados = reader.read_file()
    medias_calculadas = {}

    for aluno in dados:
        nome = aluno['nome']

        if nome not in medias_calculadas:
            notas = aluno['notas']
            media = calcular_media(notas)
            medias_calculadas[nome] = media
            print(f'A média das notas de {nome} é {media:.2f}.')

# Exemplo de uso com arquivo yaml
# arquivo = 'data/notas.yaml'
# processar_arquivo(arquivo)

# Exemplo de uso com arquivo csv
arquivo = 'data/notas.csv'
processar_arquivo(arquivo)