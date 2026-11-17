# Aula 08 — Classes e objetos

**Referência no livro:** Capítulo VIII: introdução à orientação a objetos. Material complementar autoral.

## Objetivos

Ao terminar esta aula, você deve conseguir explicar a ideia central, executar o exemplo e modificar o programa com segurança.

## Entenda o conceito

Classes definem objetos com dados e comportamentos. Use métodos para operações ligadas ao estado e evite classes quando uma função simples resolver.

## Demonstração

```python
from dataclasses import dataclass

@dataclass
class Computador:
    nome: str
    memoria_gb: int

    def descricao(self) -> str:
        return f"{self.nome}: {self.memoria_gb} GB"

pc = Computador("LAB-01", 16)
print(pc.descricao())
```

## Vamos investigar

1. Preveja o resultado antes de executar.
2. Execute o exemplo no notebook e confira.
3. Altere um valor por vez e registre o que mudou.
4. Tente provocar um erro de propósito e descreva como o corrigiu.

## Desafio da aula

Crie uma classe Chamado com prioridade, estado e método para encerrar.

**Critérios de conclusão:** o programa executa, tem nomes claros e você consegue explicar cada passo sem ler o código.

## Para aprofundar

- [Documentação oficial do Python](https://docs.python.org/3/tutorial/)
- Notebook correspondente: [`../notebooks/08-orientacao-a-objetos.ipynb`](../notebooks/08-orientacao-a-objetos.ipynb)

## Anotações da turma

- O que aprendi:
- O que ainda não entendi:
- Uma aplicação prática:
