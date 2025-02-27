[![en](https://raw.githubusercontent.com/mpcabete/bombcrypto-bot/main/readme-images/lang-en.svg)](https://github.com/mpcabete/bombcrypto-bot/blob/main/README.en.md)

# Sobre:
Este bot tem o seu código aberto, de forma que qualquer pessoa pode vê-lo, fazer uma fork, ou updates.

Desenvolvi esse bot inicialmente para o meu uso pessoal. Eu decidi publica-lo
aqui para ajudar o pessoal e com a esperança de ganhar um trocadinho com
doações.  Com o tempo mais e mais pessoas foram abrindo issues, pedindo ajuda,
e dando sugestões. Eu tento responder todo mundo, mas ultimamente tem sido
difícil acompanhar a demanda. 

Eu gostaria de manter este bot grátis e com o código aberto. Para que isso
seja possível eu estou criando algumas metas de doação para que o bot possa
ser financiado coletivamente. Atualmente eu atualizarei a barra das metas
manualmente de forma diária, talvez no futuro eu automatize o processo de
alguma forma.

1 - Diariamente passar um tempo respondendo os issues, organizando o
repositório e revisando pull requests.

2 - Um tutorial de como identificar e resolver os problemas mais comuns no
bot, talvez com um diagrama de fluxo.

3 - Um tutorial de como hostear o bot em um computador virtual usando o plano
de testes de 3 meses da google cloud.

4 - Terminar de implementar e fazer a manutenção e os ajustes necessários na
função de enviar os heróis para casa.

5 - Inserir um valor aleatório em todos os movimentos e os intervalos de
espera do bot para dificultar ainda mais sua detecção.

6 - Arrumar e ajustar os problemas que tem ocorrido durante o processo de
login.

7 - Trabalhar com o pessoal para arrumar os erros que ocorrem quando o bot é
usado em um setup windows com dois monitores.


``` 
             1(15%)        2,3(30%)     4(40%)               5(60%)          6(75%)     7(85%)
[xxxxxxxxxxxxxx|xxxxxxxxxxx=====|==========|====================|===============|==========|===============] (500$)
                          |
                         120$

```
- 25/11/21
 
### Smart Chain Wallet:
#### 0xbd06182D8360FB7AC1B05e871e56c76372510dDf

### Paypal:
[Donate:](https://www.paypal.com/donate?hosted_button_id=JVYSC6ZYCNQQQ)
https://www.paypal.com/donate?hosted_button_id=JVYSC6ZYCNQQQ

## Aviso:

Os desenvolvedores do jogo ainda não se pronunciaram oficialmente em relação
ao uso de bots, faça sua pesquisa e use o bot por sua própria conta e risco.
Não me responsabilizo por eventuais penalidades sofridas por quem usar o bot.

# Instalação:
### Baixe e instale o Python pelo [site](https://www.python.org/downloads/) ou pela [windows store](https://www.microsoft.com/p/python-37/9nj46sx7x90p?activetab=pivot:overviewtab).

Se você baixar pelo site é importante marcar a opção para adicionar o
python ao PATH:
![Check Add python to PATH](https://github.com/mpcabete/bombcrypto-bot/raw/ee1b3890e67bc30e372359db9ae3feebc9c928d8/readme-images/path.png)

### Realize o download do codigo no formato zip, e extraia o arquivo.

### Copie o caminho até a pasta do bot:

![caminho](https://github.com/mpcabete/bombcrypto-bot/raw/main/readme-images/address.png)

### Abra o terminal.

Aperte a tecla do windows + r e digite "cmd":

![launch terminal](https://github.com/mpcabete/bombcrypto-bot/raw/main/readme-images/cmd.png)

### Navegue até a pasta do bot:
Digite o comando "cd" + caminho que você copiou:

![cd](https://github.com/mpcabete/bombcrypto-bot/raw/main/readme-images/cd.png)

### Instale as dependências:

```
pip install -r requirements.txt
```

  
![pip](https://github.com/mpcabete/bombcrypto-bot/raw/main/readme-images/pip.png)

### Pronto! Agora é só iniciar o bot com o comando

```
python index.py
```

![run](https://github.com/mpcabete/bombcrypto-bot/raw/main/readme-images/run.png)


# Como usar?

Abra o terminal, se ainda não tiver navegado para a pasta do bot dê novamente o comando

```
"cd" + caminho que você copiou
```

Para iniciar use o comando 

```
python index.py
```

Assim que ele iniciar ele vai começar mandando os bonecos trabalhar. Para que ele funcione é preciso que a janela do game esteja aparecendo na sua tela.
Ele vai constantemente checar se você foi desconectado para realizar o login novamente, e se o botão “new map” tá na tela para clicar nele.
A cada 15 minutos ele manda todos os heróis taralharem.

## Como funciona?

O bot não interage diretamente com o jogo, ele somente tira print da tela do
game para encontrar os botões e simula movimentos do mouse, isso faz com que
diferenciar o bot de um humano seja muito difícil.

### Algumas configuraçoes podem ser mudadas no arquivo config.yaml, nao se
### esqueça de reiniciar o bot caso mude as configuraçoes.

## Curtiu? Dê aquela fortalecida :)

### Wallet:
#### 0xbd06182D8360FB7AC1B05e871e56c76372510dDf
### Paypal:
[Donate](https://www.paypal.com/donate?hosted_button_id=JVYSC6ZYCNQQQ)
