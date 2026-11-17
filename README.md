# Python na prática: do zero a projetos reais

Curso aberto para estudar Python no **VS Code**, com aulas em Markdown e laboratórios em Jupyter Notebook. Os exemplos são autorais e usam situações próximas de TI.

> **Base bibliográfica:** Paiva, F. A. P. de; Nascimento, J. M. A. do; Martins, R. S.; Souza, G. R. de. *Introdução a Python com aplicações de sistemas operacionais*. Editora IFRN, 2019 (edição consultada com capa de 2020). ISBN 978-65-86293-38-8.
>
> Este projeto é uma adaptação didática independente: não é publicação oficial da Editora IFRN. Os textos e exemplos foram escritos para este curso. O PDF não está redistribuído no repositório.

## Começar em 5 minutos

1. Instale [Python](https://www.python.org/downloads/) e [VS Code](https://code.visualstudio.com/).
2. Instale as extensões **Python** e **Jupyter** no VS Code.
3. Abra esta pasta no VS Code e crie um ambiente virtual:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

No Linux/macOS, use `python3 -m venv .venv` e `source .venv/bin/activate`. Se o PowerShell bloquear a ativação, selecione diretamente o interpretador `.venv` pelo VS Code, sem alterar políticas de execução.

4. Em **Python: Select Interpreter**, escolha o Python de `.venv`.
5. Abra `notebooks/01-primeiros-passos.ipynb` e selecione o kernel do ambiente `.venv`.

## Trilha de aprendizagem

| Aula | Conteúdo | Laboratório |
| --- | --- | --- |
| 01 | [Primeiros passos com Python](aulas/01-primeiros-passos.md) | [Notebook](notebooks/01-primeiros-passos.ipynb) |
| 02 | [Variáveis, tipos e operações](aulas/02-variaveis-e-tipos.md) | [Notebook](notebooks/02-variaveis-e-tipos.ipynb) |
| 03 | [Decisões e condicionais](aulas/03-condicionais.md) | [Notebook](notebooks/03-condicionais.ipynb) |
| 04 | [Laços e repetições](aulas/04-repeticoes.md) | [Notebook](notebooks/04-repeticoes.ipynb) |
| 05 | [Listas e coleções](aulas/05-listas.md) | [Notebook](notebooks/05-listas.ipynb) |
| 06 | [Dicionários e dados estruturados](aulas/06-dicionarios.md) | [Notebook](notebooks/06-dicionarios.ipynb) |
| 07 | [Funções e organização do código](aulas/07-funcoes.md) | [Notebook](notebooks/07-funcoes.ipynb) |
| 08 | [Classes e objetos](aulas/08-orientacao-a-objetos.md) | [Notebook](notebooks/08-orientacao-a-objetos.ipynb) |
| 09 | [Processos, concorrência e escalonamento](aulas/09-sistemas-operacionais.md) | [Notebook](notebooks/09-sistemas-operacionais.ipynb) |


## Como estudar

Leia a aula (`aulas/`), execute as células do notebook correspondente e resolva o desafio sem olhar a resposta. Registre o que aprendeu e faça commits pequenos. No final, explore `projetos/inventario-ti`.

## Comandos úteis

```powershell
python -m pytest
python -m ruff check .
python -m ruff format --check .
```

## Organização

- `aulas/`: material teórico em Markdown.
- `notebooks/`: demonstrações, experimentos e exercícios executáveis.
- `projetos/`: aplicação integradora.
- `tests/`: testes automatizados.
- `.vscode/`: recomendações do editor.

## Referências e atualização

O livro orienta a **sequência dos assuntos**. O curso complementa a obra com ambiente virtual, Jupyter, dicas de depuração, anotações de tipo, testes e organização de repositórios. Recursos e APIs modernos devem ser conferidos na [documentação oficial do Python](https://docs.python.org/3/) e na [documentação do Jupyter](https://docs.jupyter.org/).

## Licença

O conteúdo autoral deste repositório é disponibilizado sob licença MIT (ver `LICENSE`). Essa licença **não se aplica ao livro utilizado como referência**.
