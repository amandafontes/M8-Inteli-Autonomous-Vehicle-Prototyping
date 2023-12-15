<h2>Semana 7 | Aplicação prática de TTS e STT</h2>
<br>

O presente diretório é destinado à entrega da atividade ponderada referente à criação de um sistema de conversão Speech-to-Text e Text-to-Speech.

<h3>Introdução à atividade</h3>

Crie uma ferramenta de terminal capaz de receber como argumento o caminho para um arquivo de áudio contendo a fala de uma pessoa. Após ler o arquivo fornecido, a sua aplicação deve ser capaz de transformar o áudio em texto corretamente, usar esse texto gerado para alimentar um tradutor de texto (e.g. transforma um texto do português para o inglês) e, por fim, transforma o texto traduzido em áudio novamente e reproduz para o usuário.

<h3>Implementação</h3>

Para a implementação da atividade, foi desenvolvido um script Python <code>script.py</code> que instancia um modelo de conversão de voz para texto, um modelo de conversão de texto para voz e um método de tradução de texto. O script recebe, via terminal, o caminho para o arquivo de áudio que o usuário deseja trazudir. Desse modo, a conversão de áudio para texto é realizada por meio do modelo small do <code>whisper</code>. Posteriormente, o texto gerado é traduzido para a língua inglesa e transformado em áudio por meio do modelo <code>ljspeech</code>. Por fim, o áudio com o conteúdo já traduzido é reproduzido para o usuário.

<h3>Execução</h3>

Para que o código seja executado, basta realizar o download do presente diretório, o qual contém o script desenvolvido e o arquivo de áudio utilizado para teste. Posteriormente, será necessários instalar os pacotes necessários para o funcionamento do código. Para isso, basta executar o comando abaixo:

```bash
pip install -r requirements.txt
```

Por fim, será necessário executar o script:

```bash
python3 script.py
```