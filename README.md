# Docker-Vigilancia-Tecnologica
Repositorio donde se dockeriza una herramienta de Vigilancia Tecnologica

* Jorge Andrés Lucero Hernández 20152020082
* Juliana Alexandra Capador Ochoa 20152020081

#Ejecución
* Realizar una copia del repositorio

git clone https://github.com/JulianaCapador/Docker-Vigilancia-Tecnologica.git

* Crear la imagen de docker y el contenedor

sudo docker build -t "herramienta" .

* Correr el docker

sudo docker run -it --rm --name buscador herramienta


