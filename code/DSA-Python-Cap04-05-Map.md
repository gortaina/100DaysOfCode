
# <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 4</font>

## Download: http://github.com/dsacademybr

## Map


```python
# Criando duas funções

# Função 1 - Recebe uma temperatura como parâmetro e retorna a temperatura em Fahrenheit
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

# Função 2 - Recebe uma temperatura como parâmetro e retorna a temperatura em Celsius
def celsius(T):
    return (float(5)/9)*(T-32)
```


```python
# Criando uma lista
temperaturas = [0, 22.5, 40, 100]
```


```python
# Aplicando a função a cada elemento da lista de temperaturas. 
# Em Python 3, a funçãp map() retornar um iterator
map(fahrenheit, temperaturas)
```




    <map at 0x4bb26a0>




```python
# Função map() reotrnando a lista de temperaturas convertidas em Fahrenheit
list(map(fahrenheit, temperaturas))
```




    [32.0, 72.5, 104.0, 212.0]




```python
# Usando um loop for para imprimir o resultado da função map()
for temp in map(fahrenheit, temperaturas):
    print(temp)
```

    32.0
    72.5
    104.0
    212.0
    


```python
# Convertendo para Celsius
map(celsius, temperaturas)
```




    <map at 0x4cd0198>




```python
list(map(celsius, temperaturas))
```




    [-17.77777777777778, -5.277777777777778, 4.444444444444445, 37.77777777777778]




```python
# Usando lambda
map(lambda x: (5.0/9)*(x - 32), temperaturas)
```




    <map at 0x4cd0588>




```python
list(map(lambda x: (5.0/9)*(x - 32), temperaturas))
```




    [-17.77777777777778, -5.277777777777778, 4.444444444444445, 37.77777777777778]




```python
# Somando os elementos de 2 listas
a = [1,2,3,4]
b = [5,6,7,8]
```


```python
list(map(lambda x,y:x+y, a, b))
```




    [6, 8, 10, 12]




```python
# Somando os elementos de 3 listas
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]
```


```python
list(map(lambda x,y,z:x+y+z, a, b, c))
```




    [15, 18, 21, 24]



# Fim

### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
