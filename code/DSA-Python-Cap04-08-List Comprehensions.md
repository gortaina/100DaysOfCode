
# <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 4</font>

## Download: http://github.com/dsacademybr

## List Comprehension


```python
# Retornar cada caracter em uma sequência de caracteres
lst = [x for x in 'python']
```


```python
# Check
lst
```




    ['p', 'y', 't', 'h', 'o', 'n']




```python
type(lst)
```




    list




```python
# Variável x elevada ao quadrado para um range de números e retornar uma lista
lst = [x**2 for x in range(0, 11)]
```


```python
lst
```




    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]




```python
# Verificar os números pares em um range de números
lst = [x for x in range(11) if x % 2 == 0]
```


```python
lst
```




    [0, 2, 4, 6, 8, 10]




```python
# Converter Celsius para Fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [ ((float(9)/5)*temp + 32) for temp in celsius ]

fahrenheit
```




    [32.0, 50.0, 68.18, 94.1]




```python
# Operações aninhadas
lst = [ x**2 for x in [x**2 for x in range(11)]]
```


```python
lst
```




    [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]



# FIM

### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
