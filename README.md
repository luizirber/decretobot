# DECRETOBOT!

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/luizirber/decretobot/master?filepath=notebooks%2F01.Exploration.ipynb)

# Instalação

Para um tutorial bastante completo,
veja https://medium.com/@henriquebastos/guia-definitivo-para-organizar-meu-ambiente-python-a16e2479b753#.zdoot97pd

Mas vão aí algumas instruções rápidas!

## Python no seu sistema operacional

### Ubuntu

```bash
$ sudo apt-get install python3 python3-venv python3-pip wget
```

### macOS

Python já vem instalado no sistema,
mas é uma versão antiga.
A sugestão é usar [Anaconda][2] ou o [Homebrew][3] pra instalar.

### Windows

Eu sugiro instalar o [Bash on Ubuntu on Windows][0] e seguir as instalações pra [Ubuntu](#ubuntu),
mas você também pode instalar o [Python oficial][1] ou [Anaconda][2].

## Pip, virtualenv e dependências

```bash
$ python3 -mvenv .venv
$ source .venv/bin/activate
$ pip install python-telegram-bot
```

- Editar decretobot.py e adicionar o token

## Rodando o bot!

### Criando um token

Para criar um bot no Telegram você precisa conversar com o BotFather.
Pra fazer isso,
abra o Telegram e no campo de busca procure por "@BotFather".
Pode bater um papo bacana com ele,
mas o importante é digitar `/newbot` pra começar o processo de criação de um bot.
Ele vai fazer algumas perguntas (qual o nome? qual vai ser o usuário?)
e no fim dar informações sobre um **token**.
Tome nota,
vamos precisar disso depois!

### IT'S ALIVE! (interagindo com seu bot)

```bash
$ wget https://github.com/DragoesDeGaragem/decretobot/raw/master/decretobot.py
```

Editar e adicionar o token

```bash
$ source .venv/bin/activate
$ python decretobot.py
```

# Tarefas da semana

- Instalar o Python 3 (Linux ou Windows, fique a vontade);
- Instalar um editor de texto (Sublime, VIM ou Atom) ou um ambiente de desenvolvimento mais completo (PyCharm, Eclipse);
- Aprender a instalar bibliotecas no Python (pip);
- Dar uma olhada na biblioteca de desenvolvimento de Bot do Telegram (https://python-telegram-bot.org/);

Um tutorial bem completo,
mas que também faz bem mais coisa (e pode ser confuso pra iniciantes):
https://juliarizza.wordpress.com/2016/08/06/fazendo-um-bot-para-telegram-em-python/

[0]: https://msdn.microsoft.com/en-us/commandline/wsl/about
[1]: https://www.python.org/downloads/release/python-360/
[2]: https://www.continuum.io/downloads
[3]: http://brew.sh/index_pt-br.html
