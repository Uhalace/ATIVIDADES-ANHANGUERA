#Atividade proposta: Você foi contratado para desenvolver um sistema simples de gestão de 
#notas de alunos. O sistema deve permitir que o usuário adicione notas, calcule a média das notas, 
#determine a situação do aluno (aprovado ou reprovado), e exiba um relatório final. Utilize 
#estruturas condicionais, de repetição e funções.

#O ALUNO PRECISA TIRAR 7 PARA SER APROVADO
#O SISTEMA VAI EXIBIR A SITUAÇÃO DESTE ALUNO BASEADA NA MÉDIA
#TAMBEM DEVO LISTAR AS NOTAS QUE ESSE ALUNO TIROU

#AGORA VAMOS AO CÓDIGO

#PRIMEIRO VAMOS CRIAR UMA LISTA VAZIA, VISTO QUE O USUÁRIO VAI PREENCHER AS NOTAS
notas= [] #AS NOTAS SERÃO LANCADAS NO FORMATO LISTA
#CRIANDO LOOPIN PARA A INSERÇÃO DAS NOTAS NA LISTA
while True:
    try:
        #O USUÁRIO DEVERÁ DIGITAR UM NÚMERO INTEIRO
        #USAREMOS O .REPLACE(",",".") PARA ACEITAR TANTO NOTAS COMO 5,5 E 5.5
        entrada = input("Digite uma nota: ").replace(",", ".")
        #CONVERTENDO PARA FLOAR PARA QUE O NUMERO SEJA DECIMAL
        nota = float(entrada)
        #VERIFICAR SE A NOTA JÁ FOI INFORMADA
        if nota not in notas: #FIZ ESSA PARTE PARA EVITAR QUE SEJA LANCADA 2X A MESMA NOTA
            #INSERINDO A NOTA NA LISTA NOTAS 
            notas.append(nota)
            #INFORMADO QUE A NOTA FOI LANCADA
            print("Nota inserida com sucesso!")
        else: #AQUI ELE VERIFICARA SE A NOTA JÁ FOI LANCADA, CASO SIM ELE MANDA UMA MENSAGEM
            print("Você já informou essa nota, por isso não posso salvá-la")
    except NotaErro: #CASO O USUÁRIO DIGITE ALGO DIFERENTE DE UM NÚMERO
        print("Você está digitando algo diferente de um número, são permitidos números inteiros ou decimais")
        continue #REPETE O LOOPING
    while True:
        continuar = input("Deseja inserir mais alguma nota? \n Digite S para SIM e N para NÃO ").strip().upper()
        if continuar in ("S","N"): #SÓ ACEITA S OU N
            break
        print("Digite apenas S para SIM ou N para NÃO")
    if continuar == "N": #SE O USUÁRIO ESCOLHEU N, SAIRA DO LOOP PRINCIPAL
        print("Você digitou N, agora vou calcular as coisa aqui! \n")
        break

#ORDENANDOOS NÚMERO EM ORDEM CRESCENTE
notas.sort()

#AGORA VAMOS CALCULAR A MÉDIA
#FUNÇÃO REGULAR PARA CALCULAR A MÉDIA
def calcular_media(notas):
    total = sum(notas)
    media = total/len(notas)
    return media

#ARREDONDAR A MÉDIA
arredondar_media = lambda media: round(media,2)

#CALCULANDO A MÉDIA
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

#AGORA VAMOS VERIFICAR SE O ALUNO ESTÁ APROVADO OU NÃO E EXIBINDO O RELATÓRIO
if media_arredondada >= 7:
    print("\n Relatório do aluno")
    print(f"Notas digitadas: {notas}")
    print(f"Sua média é: {media_arredondada}")
    print("Você está: APROVADO")
else :
    print("\n Relatório do aluno")
    print(f"Notas digitadas: {notas}")
    print(f"Sua média é: {media_arredondada}")
    print("Você está: REPROVADO")
