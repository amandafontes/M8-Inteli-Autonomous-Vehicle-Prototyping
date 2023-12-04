<h2>Semana 3 | Implementação de SLAM</h2>
<br>

O presente diretório é destinado à entrega da atividade ponderada referente à navegação com o Turtlebot3.

<h3>Introdução à atividade</h3>

Desenvolva um pacote em ROS com as funcionalidades de mapeamento e navegação utilizando o Turtlebot3 (simulado ou real). O objetivo é interagir de forma programática com o stack de navegação do ROS.

<h3>Implementação</h3>

O primeiro passo para o desenvolvimento da atividade foi a estruturação do sistema: optei pela criação de três diferentes pacotes, sendo um deles destinado ao mapeamento do ambiente simulado, outro ao salvamento do mapa renderizado e o último à navegação do robô através do mapa criado. Desse modo, são descritos, abaixo, os componentes da solução:

<code>mapping</code> Pacote responsável por lançar, simultaneamente, o controle teleoperacional do Turtlebot3, um ambiente de simulação no Gazebo e o Rviz, software responsável pela parte de cartografia.<br>

<code>map_saver</code> Pacote responsável por lançar o comando capaz de salvar o mapa renderizado pelo Rviz, uma vez que o ambiente de simulação é mapeado.<br>

<code>navigation</code> Pacote responsável por lançar, simultaneamente, um novo ambiente simulado no Gazebo, o Rviz com o mapa renderizado na durante a primeira etapa, e o script Python de navegação do robô.<br>

Cada pacote contém uma launch file responsável por executar os comandos necessários para a execução dos componentes descritos acima. As launch files podem ser identificadas no diretório <code>launch</code> de cada pacote. Além disso, o pacote <code>navigation</code> contém um script Python que realiza a navegação do robô por meio do mapa renderizado.

Para executar os pacotes corretamente, é necessário fazer o download do diretório <code>workspace</code>, onde se encontram os pacotes desenvolvidos. Posteriormente, o terminal deve ser aberto e os comandos descritos abaixo devem ser executados.

**Setup**

Para interagir com o stack de navegação do ROS2 ‒ especialmente com o Nav2 e com o Turtlebot3 ‒, é necessário executar os comandos abaixo. Os comandos são apropriados para o terminal **zsh**, que foi utilizado para o desenvolvimento da atividade.
<br>

```zsh
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup "ros-humble-turtlebot3*"
```
<br>

```zsh
sudo apt install ros-humble-rmw-cyclonedds-cpp
```
<br>

```zsh
echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.zshrc
```
<br>

**Execução dos pacotes**

Será necessário abrir três terminais, sendo que cada um será destinado ao lançamento de um pacote. Para isso, o diretório <code>workspace</code> deve ser aberto em cada um dos terminais.

Primeiramente, o comando abaixo deve ser executado para a construção do workspace ROS2.

```zsh
colcon build
```

Posteriormente, será necessário dar source no script de setup do workspace.

```zsh
source install/local_setup.zsh
```

Por fim, o comando abaixo deve ser executado para a execução do pacote.

```zsh
ros2 launch <nome_do_pacote> launch.py
```

Substitua <code><nome_do_pacote></code> por <code>mapping</code>, <code>map_saver</code> ou <code>navigation</code>, a depender do pacote que será executado no terminal em questão.


<h3>Vídeo demonstrativo</h3>

Abaixo, encontra-se o vídeo de demonstração que gravei para a atividade. Na gravação, executei os três pacotes criados de forma bem-sucedida: após concretizar o mapeamento do ambiente simulado, o mapa renderizado foi salvo e a navegação por meio do script foi realizada.

https://github.com/amandafontes/M8-Inteli-Autonomous-Vehicle-Prototyping/assets/77015911/832a5ab7-9fc9-4a82-955a-4571f202df1b

<h3>Desafios e limitações</h3>

Ao realizar a atividade, foi necessário lidar com uma série de erros relacionados às configurações do ROS2, ao terminal utilizado, ao Gazebo e ao Rviz, entre outras inconsistências que foram surgindo ao desenvolver as launch files e o script de navegação. Dessa forma, embora o objetivo principal da atividade tenha sido atingido, tenho incertezas quanto ao atendimento integral do padrão de qualidade estabelecido para a atividade. Acredito que a solução possa ser refinada posteriormente.

<h3>Estrutura de pastas</h3>

<p>Abaixo, encontra-se a estrutura básica de pastas da atividade.</p>

:file_folder: &nbsp; workspace<br>
&nbsp; &nbsp; &nbsp; :file_folder: &nbsp; build<br>
&nbsp; &nbsp; &nbsp; :file_folder: &nbsp; install<br>
&nbsp; &nbsp; &nbsp; :file_folder: &nbsp; log<br>
&nbsp; &nbsp; &nbsp; :file_folder: &nbsp; src<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :file_folder: &nbsp; build<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :file_folder: &nbsp; install<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :file_folder: &nbsp; log<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :file_folder: &nbsp; map_saver<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :file_folder: &nbsp; mapping<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; :file_folder: &nbsp; navigation<br>
&nbsp; &nbsp; &nbsp; :page_with_curl: &nbsp; mapa.pgm<br>
&nbsp; &nbsp; &nbsp; :page_with_curl: &nbsp; mapa.yaml<br>
