# Aula 06 — Dicionários e dados estruturados

**Referência no livro:** Capítulo VI: dicionários. Material complementar autoral.

## Objetivos

Ao terminar esta aula, você deve conseguir explicar a ideia central, executar o exemplo e modificar o programa com segurança.

## Entenda o conceito

Dicionários associam chaves a valores. São úteis para registros, configurações e dados semiestruturados; `.get()` permite acessar chaves opcionais.

## Demonstração

```python
computador = {"nome": "PC-01", "ip": "192.168.1.10", "online": True}
computador["sala"] = "Laboratório A"
for chave, valor in computador.items():
    print(f"{chave}: {valor}")
```

## Vamos investigar

1. Preveja o resultado antes de executar.
2. Execute o exemplo no notebook e confira.
3. Altere um valor por vez e registre o que mudou.
4. Tente provocar um erro de propósito e descreva como o corrigiu.

## Desafio da aula

Monte um inventário com pelo menos três computadores e filtro por status.

**Critérios de conclusão:** o programa executa, tem nomes claros e você consegue explicar cada passo sem ler o código.

## Para aprofundar

- [Documentação oficial do Python](https://docs.python.org/3/tutorial/)
- Notebook correspondente: [`../notebooks/06-dicionarios.ipynb`](../notebooks/06-dicionarios.ipynb)

## Anotações da turma

- O que aprendi:
- O que ainda não entendi:
- Uma aplicação prática:
