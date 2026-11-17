# Aula 05 — Listas e coleções

**Referência no livro:** Capítulo V: listas. Material complementar autoral.

## Objetivos

Ao terminar esta aula, você deve conseguir explicar a ideia central, executar o exemplo e modificar o programa com segurança.

## Entenda o conceito

Listas guardam elementos ordenados e podem ser alteradas. Índices começam em zero; `append`, `pop`, `sort` e `enumerate` resolvem tarefas frequentes.

## Demonstração

```python
chamados = ["rede", "impressora", "sistema"]
chamados.append("acesso")
for indice, chamado in enumerate(chamados, 1):
    print(indice, chamado)
print("Total:", len(chamados))
```

## Vamos investigar

1. Preveja o resultado antes de executar.
2. Execute o exemplo no notebook e confira.
3. Altere um valor por vez e registre o que mudou.
4. Tente provocar um erro de propósito e descreva como o corrigiu.

## Desafio da aula

Crie uma fila de chamados com inclusão, remoção e listagem.

**Critérios de conclusão:** o programa executa, tem nomes claros e você consegue explicar cada passo sem ler o código.

## Para aprofundar

- [Documentação oficial do Python](https://docs.python.org/3/tutorial/)
- Notebook correspondente: [`../notebooks/05-listas.ipynb`](../notebooks/05-listas.ipynb)

## Anotações da turma

- O que aprendi:
- O que ainda não entendi:
- Uma aplicação prática:
