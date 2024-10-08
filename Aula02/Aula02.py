# tupla=("A","B","C","D")
# lista=["A","B","C","D"]
# #tupla[3]=("R")
# lista[3]="Richard"
# lista.insert(0,"--")
# del lista[3]
# lista.pop(3)
# lista.pop()
# lista.remove("A")
# if "A" in lista:
#   lista.remove("--")
# print("Tupla: ",tupla)
# print("Lista: ",lista)
# var=len(lista)
# print(var)
# for c, v in enumerate(tupla):
# print(f'Na posição {c} encontrei o {v}!')
# print('Cheguei ao final da lista')

# valores =[]
# x=int(input("Digite o numero de repeticoes: "))
# for cont in range(0,x):
#   valores.append(int(input("Digite um numero: ")))
# for c,valor in enumerate(valores):
#   print(f'Na posição {c} encoontrei o {valor}! ')

lista=['arroz','feijao','macarrao']

for chave,valor in enumerate(lista):
  print(f"{chave}',{valor}")

for x in range(0,10):
  print(x)