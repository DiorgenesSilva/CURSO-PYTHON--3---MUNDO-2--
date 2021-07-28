#CONDIÇÕES ANINHADAS
print("""A estrutura condicional so tem 2 opçoes
Ou é um caminho ou é outro
Ja as condiçoes aninhadas voce tem
uma gama muito maior de possibilidades
if carroesquera:
   carro.siga()
   Carrodireita()
   carro.siga()
   carro.direita()
   carro.esquerda9)
   carro.siga()
   carro.direita()
   carro.siga()
elif carro direita:
   carro.siga()
   carro.esquerda()
   carro.siaga()
   carro.esquerda()
   carro.siga()
slse carro.siga():
   carro.siga()

Python 3 : Condições
JANEIRO 27, 2018 PYTHONHOJEDEIXE UM COMENTÁRIO
Condição Simples
if algumacoisa():

Condição Composta
if algumacoisa():

else:

Exemplo:

tempo = int(input('Quantos anos seu carro tem? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
    
Condição Simplificada
tempo = int(input('Quantos anos seu carro tem? '))
print('Carro novo' if tempo <=3 else 'carro velho')
print('FIM')

Condições aninhadas
São estruturas condicionais dentro de estruturas condicionais.

if algumacoisa():

   bloco1

elif algumacoisa():

   bloco2

else:

   bloco3

Você pode usar vários elif dentro de uma estrutura.
   
""")
#
# Na Pratica
#Estrutura Condicional Simples
nome = str(input("Qual é o seu nome?"))
if nome == "Dio":
   print("Bonito nome")   
else:
   print("Seu nome é bem normal") 
print("tenha um bom dia ".format(nome))

#
# Estrutura condicional aninhadas 
#
nome = str(input("Qual é o seu nome?"))
if nome == "Dio" :
   print("Bonito nome")
   
elif nome == "Pedro" or nome == "Joao" or nome == 'Maris':
   print("São nomes bem comum no Brasil")
   
else:
   print("Seu nome é bem normal") 
print("tenha um bom dia ".format(nome))

#
#Etrutura condicional Aninhada 
#

# Na Pratica
#
nome = str(input("Qual é o seu nome?"))
if nome == "Dio" :
   print("Bonito nome")
   
elif nome == "Pedro" or nome == "Joao" or nome == 'Maris':
   print("São nomes bem comum no Brasil")
   
elif nome in"Ana Claudia Regina Luiza":
   print("belo nome feminino") 

else:
   print("Seu nome é bem normal") 
print("tenha um bom dia ".format(nome))
