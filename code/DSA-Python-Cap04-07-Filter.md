
# <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 4</font>

## Download: http://github.com/dsacademybr

## Filter


```python
# Criando uma função
def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False
```


```python
# Chamando a função e passando um número como parâmetro. Retornará 
# Falso de for ímpar e True se for par.
verificaPar(35)
```




    False




```python
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
```


```python
lista
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]




```python
filter(verificaPar, lista)
```




    <filter at 0x4ca10b8>




```python
list(filter(verificaPar, lista))
```




    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]




```python
list(filter(lambda x: x%2==0, lista))
```




    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]




```python
list(filter(lambda num: num > 8, lista))
```




    [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]



# Fim

### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
