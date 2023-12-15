<h2>P2-M8-EC | Atividade Prática</h2>
<br>

O presente diretório é destinado à entrega da atividade prática referente à segunda prova do módulo 8 de Engenharia da Computação.

<h3>Introdução à atividade</h3>

Em um mundo onde a tecnologia é uma ferramenta chave para inclusão e acessibilidade, surge a necessidade de soluções inovadoras para auxiliar pessoas com desafios na comunicação verbal, como aqueles com condições que limitam a fala. Uma instituição sem fins lucrativos cujo objetivo é melhorar a qualidade de vida de indivíduos acometidos por essa limitação contratou-o como um consultor de tecnologia. Sua tarefa é montar uma prova de conceito de uma aplicação que utiliza arquiteturas modernas de aprendizado profundo como ferramenta de sintetização de voz, potencialmente agindo como uma ponte valiosa para a comunicação, permitindo que pessoas com desafios na fala, incluindo aquelas no espectro autista, se expressem de maneira mais eficaz em seu cotidiano. Para tal, deve-se desenvolver:

<li>Uma interface de terminal. O usuário deve ser capaz de inserir frases para sintetização de forma contínua, sem precisar reinicializar a aplicação cada vez que precisar inserir uma frase.
<li>Integração com um modelo de machine learning capaz de sintetização de fala.
<li>Reprodução do áudio gerado pelo modelo de sintetização de fala.

<h3>Implementação</h3>

Para a implementação da atividade, desenvolvi um script Python <code>script.py</code> que armazena o código responsável pelo sistema de conversão de texto para voz de forma contínua.

Primeiramente, importamos os módulos necessários para a realização dos procedimentos de conversão e execução do áudio:

```bash
import soundfile as sf
import simpleaudio as sa
from txtai.pipeline import TextToSpeech
```

Posteriormente, carregamos o modelo utilizado para realizar a sintetização do texto do usuário em formato de áudio:

```bash
tts = TextToSpeech("NeuML/ljspeech-jets-onnx")
```

Referência do modelo escolhido: [ljspeech-jets-onnx](https://huggingface.co/NeuML/ljspeech-jets-onnx), do Hugging Face.

O próximo passo foi criar uma função para capturar o input do usuário. Um loop é utilizado para manter a função em execução enquanto o comando do usuário for diferente de "Sair". Uma vez que o comando é enviado, ele é convertido para áudio e salvo em um arquivo de extensão <code>.wav</code>, o qual é lido e reproduzido para o usuário via terminal até que a função seja chamada novamente. Quando o usuário optar por sair da aplicação, deve digitar o comando "Sair", de modo que ele receba, como retorno, a frase "Você optou por sair da aplicação".

```bash
def user_input():
    # Solicitação do input do usuário, contendo a frase que ele deseja converter para áudio
    frase = input("Digite aqui a frase que você deseja converter para áudio. Caso deseje sair da aplicação, digite 'Sair'.\n")

    if frase != "Sair":
        # Conversão para áudio
        audio = tts(frase)

        # Salva o áudio em um arquivo
        sf.write("output.wav", audio, 22050)

        # Lê o arquivo de áudio gerado
        wave_obj = sa.WaveObject.from_wave_file("output.wav")

        # Toca o áudio para o usuário via terminal
        play_obj = wave_obj.play()
        play_obj.wait_done()

        user_input()

    return print("Você optou por sair da aplicação.")

user_input()
```

<h3>Execução</h3>

Para que o código seja executado, basta clonar o presente diretório e executar o comando abaixo:

```bash
python3 script.py
```

Desse modo, será possível interagir com a aplicação via terminal, de forma contínua, até que a execução do código seja interrompida.