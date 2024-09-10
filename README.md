# Estrutura de Dados no Python

### [Listas Ligadas:](/linkedlists)
- [Lista Simplesmente Ligada](/linkedlists/singlylinkedlist/singlylinkedlist.py)
- [Lista Duplamente Ligada](/linkedlists/doublylinkedlist/doublylinkedlist.py)

### [Filas:](/queues)
- [Fila Simples](/queues/simplequeue.py): Implementada utilizando o [deque](https://docs.python.org/pt-br/3/library/collections.html)
- [Fila](/queues/queue.py): Implementada utilizando a [Lista Simplesmente Ligada](/linkedlists/singlylinkedlist/singlylinkedlist.py)
- [Fila LIFO](/queues/lifoqueue.py): Implementada utilizando a [Pilha](stacks/stack.py)
- [Fila de Prioridade](/queues/priorityqueue.py): A implementar

### [Pilhas:](/stacks)
- [Pilha Simples](/stacks/simplestack.py): Implementada utilizando o [deque](https://docs.python.org/pt-br/3/library/collections.html)
- [Pilha](/stacks/stack.py): Implementada utilizando a [Lista Duplamente Ligada](/linkedlists/doublylinkedlist/doublylinkedlist.py)

### Importações:
```python
from linkedlists import SinglyLinkedList, DoublyLinkedList
from queues import SimpleQueue, Queue, LifoQueue, PriorityQueue
from stacks import SimpleStack, Stack
```

> Para mais detalhes, visite o README de cada estrutura de dados.