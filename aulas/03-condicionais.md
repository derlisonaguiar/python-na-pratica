# Aula 03 — Decisões e condicionais

**Referência no livro:** Capítulo III: estruturas condicionais. Material complementar autoral.

## Objetivos

Ao terminar esta aula, você deve conseguir explicar a ideia central, executar o exemplo e modificar o programa com segurança.

## Entenda o conceito

Condições escolhem caminhos com base em expressões booleanas. Use `if`, `elif` e `else`; combine comparações com `and`, `or` e `not`.

## Demonstração

```python
nota = 7.5
frequencia = 85
if nota >= 7 and frequencia >= 75:
    print("Aprovado")
elif nota >= 5 and frequencia >= 75:
    print("Recuperação")
else:
    print("Reprovado")
```

## Vamos investigar

1. Preveja o resultado antes de executar.
2. Execute o exemplo no notebook e confira.
3. Altere um valor por vez e registre o que mudou.
4. Tente provocar um erro de propósito e descreva como o corrigiu.

## Desafio da aula

Monte um classificador de faixa etária com validação de entrada.

**Critérios de conclusão:** o programa executa, tem nomes claros e você consegue explicar cada passo sem ler o código.

## Para aprofundar

- [Documentação oficial do Python](https://docs.python.org/3/tutorial/)
- Notebook correspondente: [`../notebooks/03-condicionais.ipynb`](../notebooks/03-condicionais.ipynb)

## Anotações da turma

- O que aprendi:
- O que ainda não entendi:
- Uma aplicação prática:
