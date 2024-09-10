# Filas

### Importação:
```python
from queues import SimpleQueue
```

```python
from queues import Queue
```

```python
from queues import LifoQueue
```

```python
from queues import PriorityQueue
```

### Métodos:
- ***length():***
  - Parâmetros Obrigatórios: Nenhum
  - Parâmetros Opcionais: Nenhum
  - Definição: Retorna o tamanho da lista
  - Retorno: *int*
- ***is_empty():***
  - Parâmetros Obrigatórios: Nenhum
  - Parâmetros Opcionais: Nenhum
  - Definição: Retorna se lista está vazia ou não
  - Retorno: *bool*
- ***enqueue(\*items: Any):***
  - Parâmetros Obrigatórios:
    - items: Elemento ou elementos a serem inseridos na fila
  - Parâmetros Opcionais: Nenhum
  - Definição: Insere um ou mais elementos na fila
  - Retorno: *None*
- ***dequeue():***
  - Parâmetros Obrigatórios: Nenhum
  - Parâmetros Opcionais: Nenhum
  - Definição: Remove o último elemento da fila e retorna o elemento removido
  - Retorno: *Any or IndexError*

### Implementações:
- [Fila Simples](/queues/simplequeue.py) 
- [Fila](/queues/queue.py)
- [Fila LIFO](/queues/lifoqueue.py)
- [Fila de Prioridade](/queues/priorityqueue.py)