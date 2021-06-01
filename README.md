# Descrição do jogo
RunAway é um jogo em que um jogador descobre pistas, resolve quebra-cabeças e realiza tarefas em uma ou mais salas para cumprir um objetivo específico em um período de tempo limitado. O objetivo geralmente é escapar da sala, porém, se decidir explorar esse jogo, vai encontrar algo a mais!

## Projeto-RunAway
Esse projeto foi desenvolvido para a conclusão do módulo de lógica de programação da instituição de ensino Blue Edtech.
Este projeto buscou aprovar os conhecimentos relacionados a Programação orientada à objetos. 
Foram utilizados os seguintes recursos:

 - Classes 
 - Heranças e Heranças múltiplas
 - Bibliotecas

## Bibliotecas

O projeto necessita instalar algumas bibliotecas.

 * Pygame utilizando o seu terminal(cmd,prompt de comando) executa o seguinte código:
     `pip install pygame`
 * OS-Sys
    `pip install os-sys`
 * Pyinstaller
    `pip install pyinstaller`

## Gerando o executavel 

Para gerar um executavel do projeto é bem simples, utilizaremos a biblioteca pyinstaller, basta executar o seguinte comando no caminho aonde a pasta do projeto se encontra:

`pyinstaller --onefile -windowed main.py`

E necessita colocar a pasta _music dentro da página dist, que será criada após gerar o executavel.
