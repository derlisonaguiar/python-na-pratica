# Aula 07 — Funções e organização do código

**Referência no livro:** Capítulo VII: funções. Material complementar autoral.

## Objetivos

Ao terminar esta aula, você deve conseguir explicar a ideia central, executar o exemplo e modificar o programa com segurança.

## Entenda o conceito

Funções encapsulam comportamentos reutilizáveis. Defina entradas e retornos claros, trate casos inválidos e escreva testes pequenos.

## Demonstração

```python
def calcular_media(valores: list[float]) -> float:
    if not valores:
        raise ValueError("A lista não pode estar vazia")
    return sum(valores) / len(valores)

print(calcular_media([7.0, 8.5, 9.0]))
```

## Vamos investigar

1. Preveja o resultado antes de executar.
2. Execute o exemplo no notebook e confira.
3. Altere um valor por vez e registre o que mudou.
4. Tente provocar um erro de propósito e descreva como o corrigiu.

## Desafio da aula

Separe em funções o cadastro e a consulta do inventário.

**Critérios de conclusão:** o programa executa, tem nomes claros e você consegue explicar cada passo sem ler o código.

## Para aprofundar

- [Documentação oficial do Python](https://docs.python.org/3/tutorial/)
- Notebook correspondente: [`../notebooks/07-funcoes.ipynb`](../notebooks/07-funcoes.ipynb)

## Anotações da turma

- O que aprendi:
- O que ainda não entendi:
- Uma aplicação prática:
