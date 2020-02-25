
# <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 4</font>

## Download: http://github.com/dsacademybr

## Exercícios 


```python
# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
```


```python
list1 = [2,3,4]
listaR = list(map(lambda x:x**3, list1))
print(listaR)
#outra solução
listCubo = [item**3 for item in list1]
print(listCubo)
```

    [8, 27, 64]
    [8, 27, 64]
    


```python
# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)
```

    ['A', 'a', 1]
    ['DATA', 'data', 4]
    ['SCIENCE', 'science', 7]
    ['ACADEMY', 'academy', 7]
    ['OFERCE', 'oferce', 6]
    ['OS', 'os', 2]
    ['MELHORES', 'melhores', 8]
    ['CURSOS', 'cursos', 6]
    ['DE', 'de', 2]
    ['ANÁLISE', 'análise', 7]
    ['DE', 'de', 2]
    ['DADOS', 'dados', 5]
    ['DO', 'do', 2]
    ['BRASIL', 'brasil', 6]
    


```python
palavras1 = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
listag = list(map(lambda w: [w.upper(), w.lower(), len(w)] , palavras1))
for i in listag:
    print (i)
```

    ['A', 'a', 1]
    ['DATA', 'data', 4]
    ['SCIENCE', 'science', 7]
    ['ACADEMY', 'academy', 7]
    ['OFERCE', 'oferce', 6]
    ['OS', 'os', 2]
    ['MELHORES', 'melhores', 8]
    ['CURSOS', 'cursos', 6]
    ['DE', 'de', 2]
    ['ANÁLISE', 'análise', 7]
    ['DE', 'de', 2]
    ['DADOS', 'dados', 5]
    ['DO', 'do', 2]
    ['BRASIL', 'brasil', 6]
    


```python
# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]
```


```python

matrix1 = [[1, 2],[3,4],[5,6],[7,8]]
# 1 2
# 3 4   -> 1 3 5 7
# 5 6      2 4 6 8 
# 7 8

# resulado em tuplas - uso do zip
listam = list(zip(matrix1[0], matrix1[1],matrix1[2],matrix1[3]))
# resultado em array - zip e lista compreensivas
listam1 = [list(x) for x in zip(matrix1[0], matrix1[1],matrix1[2],matrix1[3])]
print("tuplas ",listam)
print("Array", listam1)
print("\n")
#outra solução
transposta =  [y for y in matrix1]
transposta1 = [x for x in range(2)]
transposta11= [a for a in range(4)]
transposta2 = [matrix1[x] for x in range(2)]
transposta3 = [matrix1[0][x] for x in range(0)]
transposta4 = [matrix1[0][x] for x in range(1)]
transposta5 = [matrix1[0][x] for x in range(2)]
transposta6 = [matrix1[y][0] for y in range(2)]
transposta7 = [matrix1[y][0] for y in range(3)]
transposta9 = [matrix1[y][0] for y in range(4)]

transposta9 =  [[col,row] for row in range(2) for col in range(4)]

transposta99 = [[row for row in range(2)] for col in range(4)]

transposta10 = [[row for row in range(4)] for col in range(2)]

transposta11 = [[row for row in transposta99] for col in range(2)]

transposta12 = [[row[col] for row in transposta9] for col in range(2)]

transposta17 = [[row[col] for row in matrix1] for col in range(2)]


print("t   y      ",transposta)
print("t1   x 0-2 ",transposta1)
print("t11  x 0-4 ",transposta11)
print("t2  [x]    ",transposta2)
print("t3  [0][x] ",transposta3)
print("t4  [0][x] ",transposta4)
print("t5  [0][x] ",transposta5)
print("\nt6  [y][0] ",transposta6)
print("t7  [y][0] ",transposta7)
print("t8  [y][0] ",transposta8)
print("t9  [y][x] ",transposta9)
print("\nt99 [y][x] ",transposta99)
print("t10 [y][x] ",transposta10)
print("t11 [y][x] ",transposta11)
print("t12 [y][x] ",transposta12)
print("t17 [y][x] ",transposta17)
```

    tuplas  [(1, 3, 5, 7), (2, 4, 6, 8)]
    Array [[1, 3, 5, 7], [2, 4, 6, 8]]
    
    
    t   y       [[1, 2], [3, 4], [5, 6], [7, 8]]
    t1   x 0-2  [0, 1]
    t11  x 0-4  [[[0, 1], [0, 1], [0, 1], [0, 1]], [[0, 1], [0, 1], [0, 1], [0, 1]]]
    t2  [x]     [[1, 2], [3, 4]]
    t3  [0][x]  []
    t4  [0][x]  [1]
    t5  [0][x]  [1, 2]
    
    t6  [y][0]  [1, 3]
    t7  [y][0]  [1, 3, 5]
    t8  [y][0]  [1, 3, 5, 7]
    t9  [y][x]  [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1], [1, 1], [2, 1], [3, 1]]
    
    t99 [y][x]  [[0, 1], [0, 1], [0, 1], [0, 1]]
    t10 [y][x]  [[0, 1, 2, 3], [0, 1, 2, 3]]
    t11 [y][x]  [[[0, 1], [0, 1], [0, 1], [0, 1]], [[0, 1], [0, 1], [0, 1], [0, 1]]]
    t12 [y][x]  [[0, 1, 2, 3, 0, 1, 2, 3], [0, 0, 0, 0, 1, 1, 1, 1]]
    t17 [y][x]  [[1, 3, 5, 7], [2, 4, 6, 8]]
    


```python
# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]
```


```python

lista = [0, 1, 2, 3, 4]
def pow2(p2):
    return p2**2
    
def pow3(p3):
    return p3**3
    
# [0, 1, 4, 9, 16]
list(map(lambda x: pow2(x), lista))    
# Aplica a função ao quadrado e depois a do cubo, map dentro de map
# [0, 1, 64, 729, 4096]
list(map(lambda x: pow3(x),list(map(lambda x: pow2(x), lista))))
# a solução acima aplica uma função após a outra

# a solução é criar uma lista de funções passando ao map por array!
oper = [pow2, pow3]

for i in lista:
    valor = map(lambda x:x(i), oper)
    print(list(valor))
```

    [0, 0]
    [1, 1]
    [4, 8]
    [9, 27]
    [16, 64]
    


```python
# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]
```


```python
listaA = [2, 3, 4]
listaB = [10, 11, 12]
rlist1 = list(map(lambda x,y: x**y, listaA, listaB))
print(rlist1)
#outra solução
rlist2 = list(map(pow, listaA, listaB))
print(rlist2)
```

    [1024, 177147, 16777216]
    [1024, 177147, 16777216]
    


```python
# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
range(-5, 5)
```




    range(-5, 5)




```python
klist1 = list(filter(lambda x: True if(x <0) else False, range(-5, 5)))
print(klist1)
# outra solução
klist2 = list(filter(lambda x: x < 0, range(-5, 5)))
print(klist2)
```

    [-5, -4, -3, -2, -1]
    [-5, -4, -3, -2, -1]
    


```python
# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
```


```python
a1 = [1,2,3,5,7,9]
b1 = [2,3,5,6,7,8]

# aplicado de a1-> b1 e de b1 -> a1
qList1 = list(filter(lambda b: True if(a1.count(b)) else False,(list(filter(lambda a: True if(b1.count(a)) else False, b1)))))
print(qList1)
# outra solução
qList2 = list(filter(lambda a: a in b1, a1))
print(qList2)
```

    [2, 3, 5, 7]
    [2, 3, 5, 7]
    


```python
# Exercício 8 - Considere o código abaixo. Obtenha o mesmo resultado usando o pacote time. 
# Não conhece o pacote time? Pesquise!
import datetime
print (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
```

    25/02/2020 12:52
    


```python
import time
agora = time.strftime("%d/%m/%Y %H:%M")
print(agora)

```

    25/02/2020 12:52
    


```python
# Exercício 9 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}
```


```python
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

# com tuplas
dList1 = list(zip(dict1,dict2.values()))
print(dList1)

#com dicionario
def trocar(dict1,dict2):
    dictTemp = {}
    for k1,v2 in zip(dict1, dict2.values()):
        print(k1, v2)
        dictTemp[k1] = v2

    return dictTemp

dict3 = trocar(dict1, dict2)    
print(dict3)
```

    [('a', 4), ('b', 5)]
    a 4
    b 5
    {'a': 4, 'b': 5}
    


```python
# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
```


```python
listaq = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for k,v in enumerate(listaq):
    if(k > 5):
        print(v)
  
#outra solução
for k,v in enumerate(listaq):
    if(k <= 5):
        continue
    else:
        print(v)

```

    g
    h
    g
    h
    

# Fim

### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
