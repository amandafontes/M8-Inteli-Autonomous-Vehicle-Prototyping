<h2>Semana 7 | Treinamento de sistema para detecção de imagens (MNIST)</h2>
<br>

O presente diretório é destinado à entrega da atividade ponderada referente à criação e treinamento de uma rede neural convolucional para classificar imagens utilizando o dataset MNIST.

<h3>Introdução à atividade</h3>

Treinar e utilizar uma rede neural convolucional para classificar corretamente o dataset MNIST utilizando Tensorflow e Keras.

<h3>Implementação</h3>

Para a implementação da atividade, foi desenvolvido um arquivo <code>.ipynb</code>. A primeira célula importa as bibliotecas e módulos necessários, uma vez que estamos utilizando Tensorflow e Keras. Na segunda célula, carregamos o dataset MNIST e separamos as variáveis de treinamento e teste, as quais são normalizadas posteriormente. A terceira célula é dedicada à criação da rede neural convolucional, a qual é composta por duas camadas convolucionais, duas camadas de pooling, uma camada de flattening e duas camadas densas. A quarta célula é responsável por compilar a rede neural e realizar o seu treinamento. Por fim, a quinta célula é responsável por avaliar a acurácia da rede neural.

<h3>Execução</h3>

Recomenda-se que o código seja executado no Google Colab, uma vez que, para isso, basta carregar o notebook na plataforma. Caso a execução do arquivo seja local, o Tensorflow deve estar instalado na máquina, bem como as bibliotecas e módulos utilizados no código. Para executar o código, basta executar cada célula sequencialmente.
