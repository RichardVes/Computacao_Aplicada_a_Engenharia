#Escreva um programa que solicite ao usuário um vetor de números e exiba a soma de seus elementos.
vetor=[]
total=0
condicao=False
# for contador in range(1,5):
while condicao!= True:
  saida=str(input(f'Vocẽ quer adicionar mais um numero?: [S/N]')).upper()
  if saida in 'Ss':
    num=(int(input('Digite um valor Inteiro: ')))
    total+=num
    vetor.append(num)
  else:
    break
print(f'Vetor {vetor}, soma total = {total}')   