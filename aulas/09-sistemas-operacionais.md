# Aula 09 — Processos, concorrência e escalonamento

**Referência no livro:** Capítulo IX: aplicações de sistemas operacionais. Material complementar autoral.

## Objetivos

Ao terminar esta aula, você deve conseguir explicar a ideia central, executar o exemplo e modificar o programa com segurança.

## Entenda o conceito

Concorrência permite lidar com tarefas sobrepostas. Threads ajudam em esperas de I/O, mas não garantem aceleração para cálculos pesados em Python; escalonamento é a decisão sobre quando executar tarefas.

## Demonstração

```python
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def tarefa(numero: int) -> str:
    sleep(0.1)
    return f"Tarefa {numero} concluída"

with ThreadPoolExecutor(max_workers=3) as executor:
    for resultado in executor.map(tarefa, range(1, 6)):
        print(resultado)
```

## Vamos investigar

1. Preveja o resultado antes de executar.
2. Execute o exemplo no notebook e confira.
3. Altere um valor por vez e registre o que mudou.
4. Tente provocar um erro de propósito e descreva como o corrigiu.

## Desafio da aula

Simule a fila de execução de tarefas e compare processamento sequencial e concorrente.

**Critérios de conclusão:** o programa executa, tem nomes claros e você consegue explicar cada passo sem ler o código.

## Para aprofundar

- [Documentação oficial do Python](https://docs.python.org/3/tutorial/)
- Notebook correspondente: [`../notebooks/09-sistemas-operacionais.ipynb`](../notebooks/09-sistemas-operacionais.ipynb)

## Anotações da turma

- O que aprendi:
- O que ainda não entendi:
- Uma aplicação prática:
