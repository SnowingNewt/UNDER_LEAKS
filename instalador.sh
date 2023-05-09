#!/bin/bash

#Atualiza o sistema
sudo apt update -y

#Baixa atualização
sudo apt upgrade -y

#Limpa pacotes
sudo apt autoclean && sudo apt autoremove

#Instala o Python
echo INSTALANDO O PYTHON
sudo apt install python

#Instala o pip
echo INSTALANDO O PIP
sudo apt install python3-pip

#Instalando o git
echo INSTALANDO O GIT
sudo apt install git

#Clona o repositorio
echo CLONANDO O REPOSITORIO
git clone https://github.com/SnowingNewt/UNDER_LEAKS.git

#Instala as dependências
echo INSTALANDO AS DEPENDENCIAS

#Instala o request
pip3 install requests

#Instala o json
pip3 install json

#Instala o colorama
pip3 install colorama

#Entra na pasta
cd UNDER_LEAKS

#Inicia o script
python3 Consultavel_v02.py
