
# <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 4</font>

## Download: http://github.com/dsacademybr

## Reduce


```python
# Importando a função reduce do módulo functools
from functools import reduce
```


```python
# Criando uma lista
lista = [47,11,42,13]
```


```python
lista
```




    [47, 11, 42, 13]




```python
# Função 
def soma(a,b):
    x = a + b
    return x
```


```python
# Usando reduce com uma função e uma lista. A função vai retornar o valor máximo
reduce(soma, lista)
```




    113




```python
from IPython.display import Image
Image('arquivos/reduce.png')
```




![png](output_7_0.png)




```python
# Criando uma lista
lst = [47, 11, 42, 123]
```


```python
# Usando a função reduce() com lambda
reduce(lambda x,y: x+y, lst)
```




    223




```python
# Podemos atribuir a expressão lambda a uma variável
max_find2 = lambda a,b: a if (a > b) else b
```


```python
type (max_find2)
```




    function




```python
# Reduzindo a lista até o valor máximo, através da função criada com a expressão lambda
reduce(max_find2, lst)
```




    123



# Fim

### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
