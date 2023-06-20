# Music Mentor
Repositório criado para a disicplina EEL418 - Programação Avançada. Foi escrita na linguagem [Python3]((https://www.python.org/)), utilizando [Flask](https://flask.palletsprojects.com/en/2.3.x/).

## Descrição

Music Mentor é uma aplicação web desenvolvido utilizando Python e Flask. Ela utiliza a APi do Spotify para fazer consultas sobre atributos de músicas passadas como entradas e retorna uma lista de músicas recomendadas, baseadas nessa entrada. 

## Pré-requisitos

* [Python 3](https://www.python.org/) (com pip)

### Instalando dependências

Para instalar todas as dependências com uma venv:

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
## Rodando a aplicação

Para rodar a aplicação, basta instalar as dependências e baixar o código do projeto. Com isso em mãos, é necessário rodar o arquivo `main.py` presente no diretório `website`.
Um exemplo de utilização é mostrado:

```python3
python main.py
```

Isso fará com que o servidor seja inicializado. Para abrir e utilizar a aplicação, basta entrar em um browser e colocar o endereço de localhost `127.0.0.1:3000`.
