<h2>Semana 4 | Criação de um chatbot simples</h2>
<br>

O presente diretório é destinado à entrega da atividade ponderada referente à criação de um rule-based chatbot.

<h3>Introdução à atividade</h3>

Desenvolva um nó de ROS que seja um chatbot capaz de entender comandos escritos em linguagem natural para interagir com um robô de serviço fictício. O chatbot deve fornecer ao usuário a possibilidade de enviar comandos de posição para o robô de forma simples e intuitiva.

<h3>Implementação</h3>

Para a construção da atividade, foi criado um nó em ROS, cujo conteúdo configura um script Python para o chatbot desenvolvido. O script utiliza expressões regulares para identificar o comando fornecido pelo usuário e, consequentemente, fornecer uma resposta que atenda à sua solicitação.

**Execução do nó**

É imperativo que seja feito o download do código-fonte e que seu workspace seja aberto no terminal. Primeiramente, o comando abaixo deve ser executado para a construção do workspace ROS2:

```zsh
colcon build
```

Posteriormente, será necessário dar source no script de setup do workspace.

```zsh
source install/local_setup.zsh
```

Por fim, o comando abaixo deve ser executado para a execução do nó.

```zsh
ros2 run chatbot script3
```

<h3>Vídeo demonstrativo</h3>

https://github.com/amandafontes/M8-Inteli-Autonomous-Vehicle-Prototyping/assets/77015911/dc0b055d-504d-4da6-bcff-d4f874b5adff

