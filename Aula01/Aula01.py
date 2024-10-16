import os
os.system('clear')
i=0
while True:
  i+=1
  print("1 -Pizza")
  print("2 -hotdog")
  print("3 -bebida")
  print("4 -doce")
  print("0 Para sair")
  cond=int(input("Digite uma entrada:"))
  if cond==1:
    print("Pizza 50,00")
  if cond==2:
    print("hotdog 10,00")
  if cond==3:
    print("Coca cola 12,00")
  if cond==4:
    print("Brigadeiro  2,00")
  if cond==0:
    break
print("Saida i= ",i)