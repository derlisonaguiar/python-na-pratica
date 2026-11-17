# Aula 04 — Laços e repetições

**Referência no livro:** Capítulo IV: while, range, for e break. Material complementar autoral.

## Objetivos

Ao terminar esta aula, você deve conseguir explicar a ideia central, executar o exemplo e modificar o programa com segurança.

## Entenda o conceito

Laços automatizam tarefas repetidas. `for` percorre sequências, `while` repete enquanto uma condição for verdadeira e `break` interrompe um laço.

## Demonstração

```python
temperaturas = [29, 31, 30, 28]
for dia, temperatura in enumerate(temperaturas, start=1):
    print(f"Dia {dia}: {temperatura} °C")
print("Média:", sum(temperaturas) / len(temperaturas))
```

## Vamos investigar

1. Preveja o resultado antes de executar.
2. Execute o exemplo no notebook e confira.
3. Altere um valor por vez e registre o que mudou.
4. Tente provocar um erro de propósito e descreva como o corrigiu.

## Desafio da aula

Implemente um jogo de adivinhação com limite de tentativas.

**Critérios de conclusão:** o programa executa, tem nomes claros e você consegue explicar cada passo sem ler o código.

## Para aprofundar

- [Documentação oficial do Python](https://docs.python.org/3/tutorial/)
- Notebook correspondente: [`../notebooks/04-repeticoes.ipynb`](../notebooks/04-repeticoes.ipynb)

## Anotações da turma

- O que aprendi:
- O que ainda não entendi:
- Uma aplicação prática:
