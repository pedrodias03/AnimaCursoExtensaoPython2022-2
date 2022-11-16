#criação de funções

preco = 1999.90

#Calcular 5% de imposto, guardar na variável e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)


#Criar uma função calcular_imposto() que calcula um imposto de 5% e retorna a quem pediu...
#Isso é a declearação da função
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

#Aqui é o uso da função ... o imposto  a calcuar ... e exibir na tela
preco = 299

imposto = calcular_imposto(preco)
print(imposto)
