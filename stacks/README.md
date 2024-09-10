# Filas

### Importação:
```python
from stacks import SimpleStack
```

```python
from stacks import Stack
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
- ***push(\*items: Any):***
  - Parâmetros Obrigatórios:
    - items: Elemento ou elementos a serem inseridos na fila
  - Parâmetros Opcionais: Nenhum
  - Definição: Insere um ou mais elementos na fila
  - Retorno: *None*
- ***pop():***
  - Parâmetros Obrigatórios: Nenhum
  - Parâmetros Opcionais: Nenhum
  - Definição: Remove o último elemento da fila e retorna o elemento removido
  - Retorno: *Any or IndexError*

### Implementações:
- [Pilha Simples](/stacks/simplestack.py) 
- [Pilha](/stacks/stack.py)