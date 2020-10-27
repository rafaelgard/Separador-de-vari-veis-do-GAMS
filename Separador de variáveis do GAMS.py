#Separador de variáveis do GAMS
#O código original está diponível neste link: https://github.com/rafaelgard/Separador-de-variaveis-do-GAMS

#O objetivo deste código é facilitar a construção da lista de variáveis que sejam utilizadas no modelo do Software GAMS.
#O código importa o código de um arquivo .txt, identifica as variáveis que começam com o caracter inicial da restrição e as separa numa lista já com virgula e espaçamento pronta para ser copiada e colada na secção "Equations" no seu código do GAMS.

#Importando as bibliotecas
import pandas as pd
import nltk

#Importando o código
#O código importado deve estar num arquivo .txt (bloco de notas) e salvo na mesma pasta deste código ou no local que você aponte na importação
#Aqui é apontado o local do arquivo e em seguida ele é importado através do pandas
df = pd.read_fwf("Código GAMS.txt",sep="..",encoding='UTF-8',header=None)
print(df)

#Definindo o primeiro caracter das restrições
#Aqui você define o primeiro caracter da restrição.
#Você deve alterar manualmente de maneira que ele encontre corretamente as restrições no código
Primeiro_caracter_da_restrição="R"

#Separando o código em palaras únicas
#Transforma o código em uma lista
df=df.values.tolist()

#Separa em frases
tokenized_text=nltk.sent_tokenize(str(df))

#Separa em palavras
tokenized_word=nltk.word_tokenize(str(df))

#Cria a lista de palavras
lista_de_palavras=tokenized_word

print("Lista de palavras:")
print(lista_de_palavras)

#Separa da lista as palavras que são restrições iniciadas com o 1º caracter da restrição definido no início do código
i=0
contador=0

while i<len(lista_de_palavras):        
    x=lista_de_palavras[i]
    if x[1:2]==Primeiro_caracter_da_restrição:
        print(x[1:5])
        if contador==0:
            lista_das_variaveis=x[1:5]
        else:
            lista_das_variaveis=lista_das_variaveis+", "+x[1:5]
        
        contador=contador+1
    i=i+1  
print("Foram encontradas: ", contador," variáveis")


#Imprimindo as variáveis em forma de lista já com virgula e espaçamento

print("A lista contem:", contador," variáveis\n")
print(lista_das_variaveis)