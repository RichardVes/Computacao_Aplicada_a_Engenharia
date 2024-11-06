def fun_menu():
    print('''[0] sair
[1]somar
[2]sub
[3]div
[4]mult''')
    menu=int(input("Escolha um valor: ")) 
    x=10
    y=1
    return menu,x,y

var=fun_menu()
print(var)