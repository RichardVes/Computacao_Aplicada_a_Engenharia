# Computação Aplicada a Engenharia

## Aula 07 Matriz

### Introdução ao Conceito de Matrizes em Python

> Matrizes são estruturas de dados compostas por elementos organizados em linhas e colunas. Elas são amplamente utilizadas em matemática e programação para representar dados multidimensionais, realizar cálculos algébricos, e resolver problemas como sistemas lineares e operações geométricas. Em termos simples, uma matriz pode ser vista como uma tabela onde os dados estão dispostos em um formato bidimensional.
>
> Em Python, podemos criar e manipular matrizes sem o uso de bibliotecas externas, utilizando apenas listas aninhadas. Listas em Python são coleções de elementos que podem armazenar diferentes tipos de dados, e ao criar uma lista dentro de outra lista, temos uma estrutura similar a uma matriz.

### Exemplo Simples de Matriz em Python

Vamos criar uma matriz 3x3, ou seja, com 3 linhas e 3 colunas, utilizando listas aninhadas:

```
# Criando uma matriz 3x3 manualmente com listas aninhadas
matriz = [
    [1, 2, 3],  # Primeira linha
    [4, 5, 6],  # Segunda linha
    [7, 8, 9]   # Terceira linha
]
# Exibindo a matriz
for linha in matriz:
    print(linha)
```

### Acessando Elementos da Matriz

Podemos acessar elementos específicos da matriz utilizando índices.

> Em Python, os índices começam do zero, então o primeiro elemento de cada linha está na posição 0. Por exemplo, para acessar o elemento da segunda linha e terceira coluna:

```
elemento = matriz[1][2]
print(f"O elemento na segunda linha e terceira coluna é: {elemento}")
```

### Operações Simples com Matrizes

Podemos realizar operações básicas manualmente, como a soma de duas matrizes. Abaixo, somamos duas matrizes 2x2, elemento por elemento:

```
# Definindo duas matrizes 2x2
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]

# Somando as duas matrizes
resultado = [[0, 0], [0, 0]]  # Matriz inicial para armazenar o resultado

for i in range(2):  # Percorrendo as linhas
    for j in range(2):  # Percorrendo as colunas
        resultado[i][j] = matriz1[i][j] + matriz2[i][j]

# Exibindo o resultado da soma
for linha in resultado:
    print(linha)
```

A saída será:

```
[6 , 8]
[10 , 12]
```
