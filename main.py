# comando input(): quer perimitir que
# o usuário digite algo...

nome = input("Digite seu nome: ")

#pede a idade para o usuário "Qual a sua idade?"
idade = int (input("Digite sua idade: "))

#comando de saída...exibir na tela
print(f"Boa noite, seu nome é {nome}")
print("sua idade é {}".format(idade))

#E se eu quisesse mostrar o dobro da idade?
dobro = idade * 2
print("o dobro da idade informada é {}".format(dobro))