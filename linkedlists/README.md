# Listas Ligadas

### Importação:
```python
from linkedlists import SinglyLinkedList
```

```python
from linkedlists import DoublyLinkedList
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
- ***print(reverse: bool):*** 
  - Parâmetros Obrigatórios: Nenhum
  - Parâmetros Opcionais:
    - reverse: Inverte ou não a ordem de exibição
  - Definição: Exibe a representação da lista ná saída padrão
  - Retorno: *str*
- ***append(data: Any):***
  - Parâmetros Obrigatórios: 
    - data: Elemento a ser inserido
  - Parâmetros Opcionais: Nenhum
  - Definição: Insere um elemento ao final
  - Retorno: *None*
- ***extend(iterable: Iterable):***
  - Parâmetros Obrigatórios: 
    - iterable: Objeto do tipo Iterable, que contem os elementos a serem inseridos
  - Parâmetros Opcionais: Nenhum
  - Definição: Adiciona os elementos (um por um) ao final
  - Retorno: *None*
- ***insert(index: int, data: Any):***
  - Parâmetros Obrigatórios: 
    - index: Índice a inserir o elemento
    - data: Elemento a ser inserido
  - Parâmetros Opcionais: Nenhum
  - Definição: Insere um elemento em um índice específico
  - Retorno: *None or IndexError*
- ***remove(value: Any):***
  - Parâmetros Obrigatórios: 
    - value: Elemento a ser removido
  - Parâmetros Opcionais: Nenhum
  - Definição: Remove um elemento específico
  - Retorno: *None or ValueError*
- ***pop(index: int):***
  - Parâmetros Obrigatórios: Nenhum
  - Parâmetros Opcionais: 
    - index: Índice do elemento a ser removido
  - Definição: Remove um elemento e retorna o elemento removido
  - Retorno: *Any or IndexError*
- ***clear():***
  - Parâmetros Obrigatórios: Nenhum
  - Parâmetros Opcionais: Nenhum
  - Definição: Remove todos os elementos
  - Retorno: *None*
- ***index(value: Any, start: int, stop: int):*** 
  - Parâmetros Obrigatórios:
    - value: Elemento a ser procurado
  - Parâmetros Opcionais: 
    - start: Índice a começar a procura
    - stop: Índice a terminar a procura (limite)
  - Definição: Retorna o índice do elemento procurado
  - Retorno: *int or ValueError*
- ***count(value: Any):***
  - Parâmetros Obrigatórios:
    - value: Elemento a ser contado
  - Parâmetros Opcionais: Nenhum
  - Definição: Retorna a quantidade de vezes em que o elemento aparece
  - Retorno: *int*
- ***sort(key: Callable, reverse: bool):***
  - Parâmetros Obrigatórios: Nenhum
  - Parâmetros Opcionais: 
    - key: Função que recebe um elemento da lista e retorna o elemento a ser usado na ordenação
    - reverse: Inverte ou não a ordem de ordenação
  - Definição: Ordena os elementos
  - Retorno: *None*
- ***reverse():***
  - Parâmetros Obrigatórios: Nenhum
  - Parâmetros Opcionais: Nenhum
  - Definição: Inverte a ordem dos elementos
  - Retorno: *None*
- ***copy():***
  - Parâmetros Obrigatórios: Nenhum
  - Parâmetros Opcionais: Nenhum
  - Definição: Retorna uma cópia idêntica da lista
  - Retorno: *[Singly or Doubly]LinkedList*

### Complexidades (Pior Caso):
| - | Lista Simplesmente Ligada | Lista Duplamente Ligada |
| ------- | ------------------------- | ----------------------- |
| ***\__str\__()*** | Temporal: O(N) <br>Espacial: O(N) | Temporal: O(N) <br>Espacial: O(N) |
| ***\__getitem\__()*** | Temporal: O(1) ao começo da lista ou O(N)  <br>Espacial: O(1)| Temporal: O(1) nas extremidades da lista (começo/fim) ou O(N/2)  <br>Espacial: O(1)|
| ***length()*** | Temporal: O(1) <br>Espacial: O(1) | Temporal: O(1) <br>Espacial: O(1) |
| ***is_empty()*** | Temporal: O(1)  <br>Espacial: O(1)| Temporal: O(1)  <br>Espacial: O(1)|
| ***print()***  | Temporal: O(N)  <br>Espacial: O(1)| Temporal: O(N)  <br>Espacial: O(1)|
| ***append()*** | Temporal: O(1)  <br>Espacial: O(1)| Temporal: O(1)  <br>Espacial: O(1)|
| ***extend()*** | Temporal: A definir  <br>Espacial: O(1)| Temporal: A definir  <br>Espacial: O(1)|
| ***insert()*** | Temporal: O(1) se o inserir ao começo ou O(N)  <br>Espacial: O(1)| Temporal: O(1) se o inserir nas extremidades (começo/fim) ou O(N)  <br>Espacial: O(1)|
| ***remove()*** | Temporal: O(1) se o remover do começo ou O(N)  <br>Espacial: O(1)| Temporal: O(1) se o remover das extremidades (começo/fim) ou O(N)  <br>Espacial: O(1)|
| ***pop()*** | Temporal: O(1) se o remover do começo ou O(N)  <br>Espacial: O(1)| Temporal: O(1) se o remover das extremidades (começo/fim) ou O(N)  <br>Espacial: O(1)|
| ***clear()*** | Temporal: O(1)  <br>Espacial: O(1)| Temporal: O(1)  <br>Espacial: O(1)|
| ***index()***  | Temporal: O(N)  <br>Espacial: O(1)| Temporal: O(N)  <br>Espacial: O(1)|
| ***count()*** | Temporal: O(N)  <br>Espacial: O(1)| Temporal: O(N)  <br>Espacial: O(1)|
| ***sort()*** | Temporal: O(N²)  <br>Espacial: O(1)| Temporal: O(N²)  <br>Espacial: O(1)|
| ***reverse()*** | Temporal: O(N)  <br>Espacial: O(1)| Temporal: O(N)  <br>Espacial: O(1)|
| ***copy()*** | Temporal: O(N)  <br>Espacial: O(N)| Temporal: O(N)  <br>Espacial: O(N)|


### Implementações:
- [Lista Simplesmente Ligada](/linkedlists/singlylinkedlist/singlylinkedlist.py)
- [Lista Duplamente Ligada](/linkedlists/doublylinkedlist/doublylinkedlist.py)