# AULA 06

## Vetores em Python é igual Lista

### Chamada

```
nome=[]
vetor=[0,1,2,3,4,5]
```

### Saida do Vetor

`print(vetor)`

### Manipulação do Vetor

```
for i in range(min,max):
vetor[i]= (mudança)
vetor[i]=vetor[i]\*2
print(f'{vetor}')
```

### Comandos do Vetor

```
vetor=[]
```

### adicionar item

```
vetor.append("item")
```

### Ordena o vetor

```
vetor.sort()
```

### Remove o item do vetor

```
vetor.pop(posição)
variavel=vetor.pop(posição)
```

### Inserir elemento

```
vetor.insert(posição,"item")
```

### Contagem de ocorrencia

```
vetor.count("item")
variavel=vetor.count("item")
```

### Limpando Vetor

```
vetor.clear()
```

---

# ROTINAS

## função

```
def nome():
parametros
```

**chamada**;

```
nome()
```

## parametros

```
def nome(parametro,parametro2):
ex
def linha(parametro,parametro2):
print('-='*parametro)
print(parametro2)
print('-='*parametro)
```

# DOCSTRINGS

**Se usa comando help(função), para mostrar a documentação da função;**

```
def nome():
"""
Texto de documentação da sua função
"""
```

**Para ler digite**

```
help(nome)
```
