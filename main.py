# comando input(): quer perimitir que
# o usuário digite algo...

nome = input("Digite seu nome: ")

#pede a idade para o usuário "Qual a sua idade?"
idade = int(input("Digite sua idade: "))

genero = input("Informe seu gênero (M = masculino, F = Feminino, O = Outro): ")

#comando de saída...exibir na tela
print(f"Boa noite, seu nome é {nome}")
print("Sua idade é {}".format(idade))

#E se eu quisesse mostrar o dobro da idade?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir."
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir.")
else:
  print("Você é xóvem ainda...")

# E se eu quisesse perguntar o gênero (M = Masculino e F = Feminino)

# Mostre (.. e você também precisa/precisou prestar o serviço militar obrigatório)

if idade >= 18 and genero == "M":
  print("E você também precisa/precisou prestar o serviço militar obrigatório")

elif idade >= 18:
  print("E você não precisa/precisou prestar o serviço militar obrigatório")
