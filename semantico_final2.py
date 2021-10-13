# -*- coding: utf-8 -*-
"""
Analizador Léxico
Alunos: Pedro Artur
        Thuanny Luiza
"""
from types import SimpleNamespace

#atributos = {'lexema': '', 'token': None, 'tipo': None}

tabela_transicoes = [
[4   , 100 , 20  , 17 , 17 , 9  , 20 , 100, 0  , 0  , 0  , 3  , 12 , 15 , 14 , 17 , 18 , 19 , 11 , 17 , 1  , 100, 21],
[1   , 1   , 1   , 1  , 1  , 1  , 1  , 1  , 1  , 1  , 1  , 100, 1  , 1  , 1  , 1  , 1  , 1  , 1  , 1  , 1  , 2  , 1],
[100 , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[100 , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[4   , 5   , 7   , 100, 100, 100, 21, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[6   , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[6   , 7   , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[16  , 100 , 100 , 8  , 8  , 100, 21, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[16  , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[9	 , 9   , 9   , 9  , 9  , 10 , 9  , 9  , 9  , 9  , 9  , 100, 9  , 9  , 9  , 9  , 9  , 9  , 9  , 9  , 9  , 9  , 9],
[100 , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[100 , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[100 , 100 , 100 , 100, 13 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 14 , 14 , 100, 100, 100, 100, 100, 100, 21],
[100 , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[100 , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[100 , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,  14, 100, 100, 100, 100, 100, 100, 21],
[16  , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[100 , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[100 , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[100 , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[20  , 100 , 20  , 100, 100, 100, 20 , 20 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 21],
[100 , 100 , 100 , 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
]

dicionario = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0,
'.':1,
'+':3,
'-':4,
'"':5,
'a':6,'b':6,'c':6,'d':6,'e':2,'f':6,'g':6,'h':6,'i':6,'j':6,'k':6,'l':6,'m':6,
'n':6,'o':6,'p':6,'q':6,'r':6,'s':6,'t':6,'u':6,'v':6,'w':6,'x':6,'y':6,'z':6,
'A':6,'B':6,'C':6,'D':6,'E':2,'F':6,'G':6,'H':6,'I':6,'J':6,'K':6,'L':6,'M':6,
'N':6,'O':6,'P':6,'Q':6,'R':6,'S':6,'T':6,'U':6,'V':6,'W':6,'X':6,'Y':6,'Z':6,
'_':7,
'\t':8,
'\n':9,
' ':10,
'eof':11,
'<':12,
'>':13,
'=':14,
'*':15,
'(':16,
')':17,
';':18,
'/':19,
'{':20,
'}':21,
}

dicionario_EF = {
2:'Cometario',
3: 'eof',
4: 'Num',
6: 'Num',
10:'literal',
11:'PT_V',
12:'OPR',
13:'RCB',
14:'OPR',
15:'OPR',
16:'Num',
17:'OPM',
18:'AB_P',
19:'FC_P',
20:'id',
21:'erro',
}

tipo_EF = {
4 : 'inteiro',
6 : 'real',
10: 'literal',
11: ';',
12: '<',
13: '=',
15: '>',
16: 'real',
18: '(',
19: ')',        
}

dicionario_PC = { 
'inicio': 'inicio', 
'varinicio': 'varinicio',
'varfim': 'varfim',
'escreva': 'escreva',
'leia':'leia',
'entao':'entao',
'fimse':'fimse',
'fim':'fim',
'inteiro':'inteiro',
'lit': 'lit',
'real': 'real',
'int' : 'int',
'se':'se',
}

dicionario_tipo = {
'inicio' : None,
'varinicio': None,
'varfim': None,
'escreva': None,
'leia': None,
'entao': None,
'fimse': None,
'fim': None,
'inteiro': 'inteiro',
'lit': 'literal',
'real': 'double',
'int' : 'int',
'se': None,        
}

Erros = {
0:'Caractere inválido',
1:'caractere } esperado',
4:'Esperando numero',
5:'Esperando numero',
7:'Esperando numero, + ou -',
9:'caractere " esperado',
10:'caractere " esperado'         
}

def analisadorLexico(conteudo_Arq, indice, linha, coluna_caractere):
    indice_string = int(indice)
    pula_linha = 0
    estado_inicial = 0
    cont_linha = int(linha)
    cont_coluna = int(coluna_caractere)
    texto= ''
    tamanho_string = len(conteudo_Arq)
    lista = ['', '', '']
    erro = False

    for i in range(tamanho_string):
    #while True:
        
        #retorna fim de arquivo
        if(indice_string == tamanho_string):
            
            #reconhecer erro no comentário
            if(estado_inicial == 1):
                print('\n-----------ERRO LEXICO-------------')
                print(Erros.get(estado_inicial, 'caractere diferente do esperado'))
                print('linha: ', cont_linha, 'coluna: ', cont_coluna)
                print('-----------------------------------')
                erro = True
                
            indice_string = None
            texto = 'eof'
            lista = [texto, dicionario_EF.get(estado_inicial), 'eof']
            #print(lista)
            break
        
        #pesquisa o caractere de entrada no dicionario e atualiza o estado
        caractere = conteudo_Arq[indice_string]
        cont_coluna += 1
        coluna = dicionario.get(caractere, 22)   
        estadoAtual = tabela_transicoes[estado_inicial][coluna]
        
        #armazena estado em que ocorreu o erro
        if(estadoAtual == 21):
            estadoErro = estado_inicial
    
        #se o carctere anterior for pula linha
        if(pula_linha == 1):
            if(estadoAtual == 9):
                 print('\n----------ERRO LEXICO-------------')
                 print(Erros.get(estadoAtual, 'caractere diferente do esperado'))
                 print('linha: ', cont_linha, 'coluna: ', cont_coluna)
                 print('----------------------------------')
                 estadoAtual = 0
                 erro = True
                 
            cont_linha +=1
            cont_coluna = 0
            texto = ''
            pula_linha = 0
         
            
        if(caractere == '\n'):
            pula_linha = 1
            
        #ignorar comentário
        if((estado_inicial == 2)and(estadoAtual == 100)):
            estadoAtual = 0
            texto = ''
            
        # se final de caminho no automato
        if(estadoAtual == 100):
    
            if(dicionario_EF.get(estado_inicial)=='id'):
                #tirar espaço em branco do começo da palavra
                if(texto[0] == ' '):
                    texto = texto[1:]
                    
                if(texto not in dicionario_PC):
                    dicionario_PC[texto] = 'id'
                    dicionario_tipo[texto] = ''
                    
            types = tipo_EF.get(estado_inicial, '')
            if(estado_inicial == 14 or estado_inicial == 17):
                if(texto == '<>'):
                    types = '!='
                else:
                    types = texto
            lista = [texto, dicionario_EF.get(estado_inicial), types]
            #print(lista)
            texto= ''
            
            #retorna erro lexico
            if(dicionario_EF.get(estado_inicial)):
                if(dicionario_EF.get(estado_inicial) == 'erro'):
                    print('\n-----------ERRO LEXICO-------------')
                    print(Erros.get(estadoErro, 'caractere diferente do esperado'))
                    print('linha: ', cont_linha, 'coluna: ', cont_coluna)
                    print('-----------------------------------')
                    erro = True
                else:
                    break
                
            if(caractere == ' ' or caractere == '\n'): 
                indice_string += 1
            estadoAtual = 0              
        else:     
            texto = texto+caractere
            indice_string += 1
        estado_inicial = estadoAtual
    #pausa = input(' ') #caso queira mostrar todo de uma vez e só retira-lo   
    return SimpleNamespace(indice = indice_string, 
                           linha = cont_linha, 
                           coluna = cont_coluna, 
                           identificado = lista,
                           erro = erro
                           )

'''-------------------------------------------- SINTATICO ------------------------------------------'''
conteudo = ''
numTemp = 0
erro_semantico = False


tabela_ações = [
['S2',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1',	'E1'],
['E2',	'E2',	'E2','E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2'	'E2',	'E2',	'E2',	'Acc'],
['E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'E3',	'S4',	'E3'],
['E4',	'E4',	'S5',	'E4',	'E4',	'E4',	'S6',	'S7',	'E4',	'E4',	'E4',	'E4',	'S8',	'E4',	'E4',	'E4',	'S11',	'E4',	'E4',	'E4',	'E4',	'E4'],
['E11',	'S16',	'S18',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11'],
['E10',	'E10',	'E10',	'E10',	'E10',	'E10',	'E10',	'E10',	'E10',	'E10',	'S19',	'E10',	'E10',	'E10',	'E10',	'E10',	'E10',	'E10',	'E10',	'E10',	'E10',	'E10'],
['E6',	'E6',	'S20',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6',	'E6'],
['E9',	'E9',	'S24',	'E9',	'E9',	'E9',	'E9',	'E9',	'S22',	'S23',	'E9',	'E9',	'E9',	'E9',	'E9',	'E9',	'E9',	'E9',	'E9',	'E9',	'E9',	'E9'],
['E12',	'E12',	'E12',	'E12',	'E12',	'E12',	'E12',	'E12',	'E12',	'E12',	'E12',	'E12',	'E12',	'E12',	'E12',	'E12',	'E12',	'S25',	'E12',	'E12',	'E12',	'E12'],
['E7',	'E7',	'S5',	'E7',	'E7',	'E7',	'S6',	'S7',	'E7',	'E7',	'E7',	'E7',	'S8',	'E7',	'E7',	'S30',	'E7',	'E7',	'E7',	'E7',	'E7',	'E7'],
['E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'R2'],
['E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'R30'],
['E4',	'E4',	'S5',	'E4',	'E4',	'E4',	'S6',	'S7',	'E4',	'E4',	'E4',	'E4',	'S8',	'E4',	'E4',	'E4',	'S11',	'E4',	'E4',	'E4',	'E4',	'E4'],
['E4',	'E4',	'S5',	'E4',	'E4',	'E4',	'S6',	'S7',	'E4',	'E4',	'E4',	'E4',	'S8',	'E4',	'E4',	'E4',	'S11',	'E4',	'E4',	'E4',	'E4',	'E4'],
['E4',	'E4',	'S5',	'E4',	'E4',	'E4',	'S6',	'S7',	'E4',	'E4',	'E4',	'E4',	'S8',	'E4',	'E4',	'E4',	'S11',	'E4',	'E4',	'E4',	'E4',	'E4'],
['E17',	'E17',	'R3',	'E17',	'E17',	'E17',	'R3',	'R3',	'E17',	'E17',	'E17',	'E17',	'R3',	'E17',	'E17',	'E17',	'R3',	'E17',	'E17',	'E17',	'E17',	'E17'],
['E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'S58',	'E16',	'E16'],
['E11',	'S16',	'S18',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11',	'E11'],
['E5',	'E5',	'E5',	'S36',	'S37',	'S38',	'E5',	'E5',	'E5',	'E5',	'E5',	'E5',	'E5',	'E5',	'E5',	'E5',	'E5',	'E5',	'E5',	'E5',	'E5',	'E5'],
['E15',	'E15',	'S41',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'S42',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15'],
['E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'S43',	'E16',	'E16'],
['E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'S44',	'E16',	'E16'],
['E17',	'E17',	'R13',	'E17',	'E17',	'E17',	'R13',	'R13',	'E17',	'E17',	'E17',	'E17',	'R13',	'E17',	'E17',	'R13',	'R13',	'E17',	'E17',	'R13',	'E17',	'E17'],
['E17',	'E17',	'R14',	'E17',	'E17',	'E17',	'R14',	'R14',	'E17',	'E17',	'E17',	'E17',	'R14',	'E17',	'E17',	'R14',	'R14',	'E17',	'E17',	'R14',	'E17',	'E17'],
['E17',	'E17',	'R15',	'E17',	'E17',	'E17',	'R15',	'R15',	'E17',	'E17',	'E17',	'E17',	'R15',	'E17',	'E17',	'R15',	'R15',	'E17',	'E17',	'R15',	'E17',	'E17'],
['E15',	'E15',	'S41',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'S42',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15'],
['E17',	'E17',	'R23',	'E17',	'E17',	'E17',	'R23',	'R23',	'E17',	'E17',	'E17',	'E17',	'R23',	'E17',	'E17',	'R23',	'R23',	'E17',	'E17',	'R23',	'E17',	'E17'],
['E7',	'E7',	'S5',	'E7',	'E7',	'E7',	'S6',	'S7',	'E7',	'E7',	'E7',	'E7',	'S8',	'E7',	'E7',	'S30',	'E7',	'E7',	'E7',	'E7',	'E7',	'E7'],
['E7',	'E7',	'S5',	'E7',	'E7',	'E7',	'S6',	'S7',	'E7',	'E7',	'E7',	'E7',	'S8',	'E7',	'E7',	'S30',	'E7',	'E7',	'E7',	'E7',	'E7',	'E7'],
['E7',	'E7',	'S5',	'E7',	'E7',	'E7',	'S6',	'S7',	'E7',	'E7',	'E7',	'E7',	'S8',	'E7',	'E7',	'S30',	'E7',	'E7',	'E7',	'E7',	'E7',	'E7'],
['E17',	'E17',	'R29',	'E17',	'E17',	'E17',	'R29',	'R29',	'E17',	'E17',	'E17',	'E17',	'R29',	'E17',	'E17',	'R29',	'R29',	'E17',	'E17',	'E17',	'E17',	'E17'],
['E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'R10'],
['E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'R16'],
['E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'R22'],
['E17',	'E17',	'R4',	'E17',	'E17',	'E17',	'R4',	'R4',	'E17',	'E17',	'E17',	'E17',	'R4',	'E17',	'E17',	'E17',	'R4',	'E17',	'E17',	'E17',	'E17',	'E17'],
['E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'S50',	'E16',	'E16'],
['E17',	'R7',	'R7',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'R7',	'E17',	'E17'],
['E17',	'R8',	'R8',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'R8',	'E17',	'E17'],
['E17',	'R9',	'R9',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'R9',	'E17',	'E17'],
['E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'E16',	'S51',	'E16',	'E16'],
['E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'S52',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'E2',	'R19',	'E2',	'E2'],
['E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17', 'R20','E17',	'E17',	'R20',	'E17',	'E17',	'E17',	'R20',	'R20',	'E17',	'E17'],
['E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'R21',	'E17',	'E17',	'E17',	'R21',	'R21',	'E17',	'E17'],
['E17',	'E17',	'R11',	'E17',	'E17',	'E17',	'R11',	'R11',	'E17',	'E17',	'E17',	'E17',	'R11',	'E17',	'E17',	'R11',	'R11',	'E17',	'E17',	'E17',	'E17',	'E17'],
['E17',	'E17',	'R12',	'E17',	'E17',	'E17',	'R12',	'R12',	'E17',	'E17',	'E17',	'E17',	'R12',	'E17',	'E17',	'R12',	'R12',	'E17',	'E17',	'E17',	'E17',	'E17'],
['E13',	'E13',	'E13',	'E13',	'E13',	'E13',	'E13',	'E13',	'E13',	'E13',	'E13',	'E13',	'E13',	'E13',	'E13',	'E13',	'E13',	'E13',	'S53',	'E13',	'E13',	'E13'],
['E8',	'E8',	'E8',	'E8',	'E8',	'E8',	'E8',	'E8',	'E8',	'E8',	'E8',	'E8',	'E8',	'E8',	'S54',	'E8',	'E8',	'E8',	'E8',	'E8',	'E8',	'E8'],
['E17',	'R26',	'E17',	'E17',	'E17',	'E17',	'R26',	'R26',	'E17',	'E17',	'E17',	'E17',	'R26',	'E17',	'E17',	'R26',	'R26',	'E17',	'E17',	'E17',	'E17',	'E17'],
['E17',	'R27',	'E17',	'E17',	'E17',	'E17'	'R27',	'R27',	'E17',	'E17',	'E17',	'E17',	'R27',	'E17',	'E17',	'R27',	'R27',	'E17',	'E17',	'E17',	'E17',	'E17'],
['E17',	'E17',	'R28',	'E17',	'E17',	'E17',	'R28',	'R28',	'E17',	'E17',	'E17',	'E17',	'R28',	'E17',	'E17',	'R28',	'R28',	'E17',	'E17',	'E17',	'E17',	'E17'],
['E17',	'R6',	'R6',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17'],
['E17',	'E17',	'R17',	'E17',	'E17',	'E17',	'R17',	'R17',	'E17',	'E17',	'E17',	'E17',	'R17',	'E17',	'E17',	'R17',	'R17',	'E17',	'E17',	'E17',	'E17',	'E17'],
['E15',	'E15',	'S41',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'S42',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15'],
['E14',	'E14',	'E14',	'E14',	'E14',	'E14',	'E14',	'E14',	'E14',	'E14',	'E14',	'E14',	'E14',	'S56',	'E14',	'E14',	'E14',	'E14',	'E14',	'E14',	'E14',	'E14'],
['E15',	'E15',	'S41',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'S42',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15',	'E15'],
['E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'R18',	'E17',	'E17'],
['E17',	'E17',	'R24',	'E17',	'E17',	'E17',	'R24',	'R24',	'E17',	'E17',	'E17',	'E17',	'R24',	'E17',	'E17',	'R24',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17'],
['E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'E17',	'R25',	'E17',	'E17',	'E17'],
['E17',	'E17',	'R5',	'E17',	'E17',	'E17',	'R5',	'R5',	'E17',	'E17',	'E17',	'E17',	'R5',	'E17',	'E17',	'E17',	'R5',	'E17',	'E17',	'E17',	'E17',	'E17']
]

tabela_transições = [
[ 1,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	3,	None],
[None,	None,	None,	None,	None,	10,	None,	12,	13,	14,	9,	None,	None,	None,	None],
[None,	15,	   None,	17,	   None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	21],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	27,	28,	29,	9,	None,	26,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	31,	None,	12,	13,	14,	9,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	32,	None,	12,	13,	14,	9,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	33,	None,	12,	13,	14,	9,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	34,	None,	17,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	35,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	39,	None,	None,	None,	40,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	46,	None,	None,	None,	None,	45,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	27,	28,	29,	9,	None,	47,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	27,	28,	29,	9,	None,	48,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	27,	28,	29,	9,	None,	49,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	55,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	57,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
[None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None,	None],
        
]

terminais = {
'inicio' : 0,
'varfim' : 1,
'id' : 2,
'inteiro' : 3,
'real': 4,
'lit' : 5,
'leia' : 6,
'escreva' : 7,
'literal' : 8,
'Num' : 9,
'RCB' : 10,
'OPM': 11,
'se': 12,
'entao' : 13,
'OPR' : 14,
'fimse' : 15,
'fim' : 16,
'AB_P' : 17,
'FC_P' : 18,
'PT_V' : 19,
'varinicio':20,
'$' : 21,  
}


Erros_redução={
#1 P' → P
#2 P→ inicio V A
15:"3 V→varinicio LV /// ESPERADO: id ou leia ou escreva ou se ou fim",
34:"4 LV→D LV   ///  ESPERADO:  id ou leia ou escreva ou se ou fim",
58:"5 LV→varfim;   ///  ESPERADO: id ou leia ou escreva ou se ou fim",
50:"6 D→id TIPO;   ///  ESPERADO: varfim ou id",
36:"7 TIPO→inteiro   ///  ESPERADO: varfim ou id ou PT_V ",
37:"8 TIPO→real   ///  ESPERADO: varfim ou id ou PT_V ",
38:"9 TIPO→lit   ///  ESPERADO: varfim ou id ou PT_V ",
31:"10 A→ES A   ///  ESPERADO: PT_V ",
43:"11 ES→leia id;   ///  ESPERADO:  id ou leia ou escreva ou se ou fim ou fimse",
44:"12 ES→escreva ARG;   ///  ESPERADO: id ou leia ou escreva ou se ou fim ou fimse",
22:"13 ARG→literal   ///  ESPERADO: id ou leia ou escreva ou se ou fim ou fimse ou PT_V",
23:"14 ARG→num   ///  ESPERADO: id ou leia ou escreva ou se ou fim ou fimse ou PT_V",
24:"15 ARG→id   ///  ESPERADO: id ou leia ou escreva ou se ou fim ou fimse ou PT_V",
32:"16 A→CMD A   ///  ESPERADO: $",
51:"17 CMD→id rcb LD;   ///  ESPERADO: id ou leia ou escreva ou se ou fim ou fimse",
55:"18 LD→OPRD opm OPRD   ///  ESPERADO:  PT_V",
40:"19 LD→OPRD   ///  ESPERADO: PT_V",
41:"20 OPRD→id   ///  ESPERADO: OPM ou OPR ou FC_p ou PT_V",
42:"21 OPRD→num   ///  ESPERADO: OPR ou FC_p ou PT_V",
33:"22 A→COND A   ///  ESPERADO:  $",
26:"23 COND→CABEÇALHO CORPO   ///  ESPERADO: id ou leia ou escreva ou se ou fim ou fimse",
56:"24 CABEÇALHO→se (EXP_R) então   ///  ESPERADO: id ou leia ou escreva ou se ou fimse",
57:"25 EXP_R→OPRD opr OPRD   ///  ESPERADO: FC_P",
47:"26 CORPO→ES CORPO   ///  ESPERADO: varfim ou leia ou escreva ou fim ou fimse ",
48:"27 CORPO→CMD CORPO   ///  ESPERADO: varfim ou leia ou escreva ou fim ou fimse ",
49:"28 CORPO→COND CORPO   ///  ESPERADO: id ou leia ou escreva ou se ou fim ou fimse",
30:"29 CORPO→fimse   ///  ESPERADO:id ou leia ou escreva ou se ou fim ou fimse",
11:"30 A→fim   ///  ESPERADO:  $",
        }


nao_terminais = {
'P' : 0,
'LV' : 1,
'LD' : 2,
'D' : 3,
'TIPO': 4,
'A' : 5,
'OPRD' : 6,
'ES' : 7,
'CMD' : 8,
'COND' : 9,
'CABEÇALHO' : 10,
'EXP_R' : 11,
'CORPO' : 12,
'V' : 13,
'ARG' : 14,
}     

Erros_sintaticos ={
1 :"Expectativa inserção ''inicio'' .",
2 :"Expectativa inserção de Operadores Aritméticos (+, -, *, /).",###
3 :"Expectativa inserção ""varinicio"".",####
4 :"Expectativa inserção ""leia"", ""escreva"", ""id"", ""se"" e ""fim"".",
5 :"Expectativa inserção ""int"", ""real"" ou ""lit"".",####
6 :"Expectativa inserção ""id"".",####
7 :"Expectativa inserção ""leia"", ""escreva"", ""id"", ""se"" ou ""fimse"".",     ####   testar com E4
8 :"Expectativa inserção de Operadores Relacionais (<, >, <=, >=, = e <>).",####
9 :"Expectativa inserção ""literal"", ""num"" ou ""id"".",
10:"Expectativa inserção ""<-"" (RCB).",
11:"Expectativa inserção ""varfim"" ou ""id"".",
12:"Esperando ""("" ",
13:"Esperando "")"" ",
14:"Expectativa inserção ""entao""." ,
15:"Expectativa inserção ""id"" ou ""num"".",
16:"Faltou o ;      p.s. tipíco",
17:"redução imcompleta"         
} 


produz = {2: [3, "P"],
       3: [2, "V"],
       4: [2, "LV"],
       5: [2, "LV"],
       6: [3, "D"],
       7: [1, "TIPO"],
       8: [1, "TIPO"],
       9: [1, "TIPO"],
       10: [2, "A"],
       11: [3, "ES"],
       12: [3, "ES"],
       13: [1, "ARG"],
       14: [1, "ARG"],
       15: [1, "ARG"],
       16: [2, "A"],
       17: [4, "CMD"],
       18: [3, "LD"],
       19: [1, "LD"],
       20: [1, "OPRD"],
       21: [1, "OPRD"],
       22: [2, "A"],
       23: [2, "COND"],
       24: [5, "CABEÇALHO"],
       25: [3, "EXP_R"],
       26: [2, "CORPO"],
       27: [2, "CORPO"],
       28: [2, "CORPO"],
       29: [1, "CORPO"],
       30: [1, "A"]}


def analisadorSintatico(conteudo_Arq):
    global erro_semantico
    prod = ''
    indice = 0
    coluna = 0
    linha = 0
    lista_desempilhada = []
    #tok = []
   
    dados_lexico = analisadorLexico(conteudo_Arq, indice, linha, coluna)
    indice = dados_lexico.indice
    coluna = dados_lexico.coluna
    linha = dados_lexico.linha
    retorno = dados_lexico.identificado
    token = dicionario_PC.get(retorno[0], retorno[1])
    pilha = [0]
    atributo = [retorno[0], token, dicionario_tipo.get(retorno[0], retorno[2])]
    producao = [atributo]
    #print('atributo: ', atributo)
    
    while True:
        if(dados_lexico.erro == True):
            break
        s = pilha[0]
        #print('Estado s: ', s, 'token: ', token)
        #print('coluna: ', terminais.get(token))
        #print('------------------------------------------------------------------')
        pesquisa = tabela_ações[s][terminais.get(token,21)]

        if(pesquisa == 0):
            pesquisa ='a'
            
        if(pesquisa[0] == 'S'):
            pilha.insert(0, int(pesquisa[1:]))
            #print('tabela de acoes: ',pesquisa)
            #retornar linha, coluna e indice para o léxico
            dados_lexico = analisadorLexico(conteudo_Arq, indice, linha, coluna)
            retorno = dados_lexico.identificado
            indice = dados_lexico.indice
            coluna = dados_lexico.coluna
            linha = dados_lexico.linha
            token = dicionario_PC.get(retorno[0] , retorno[1])
            atributo = [retorno[0], token, dicionario_tipo.get(retorno[0], retorno[2])]
            #print('atributo: ', atributo)
            if(dados_lexico.erro == True):
                break
            #print('lexema: ', retorno[0])
            #print('token: ',token)
            #insere o token em uma lista de tokens
            #producao.insert(0, token)
            producao.insert(0, atributo)
            #print(producao)
        
        elif(pesquisa[0] == 'R'):
            regra = int(pesquisa[1:])
            dados_producao = produz.get(regra)
           
            #print('tabela de acoes: ', pesquisa)
            #print('quantidade de termos da producao: ')
            #print(dados_producao [0])
            #print('pilha de tokens: ',pilha)
            
            n = dados_producao[0] 
            
            #retira da pilha de estados a quantidade equivalente a beta
            #substitui a produção na pilha de tokens
            for i in range(dados_producao[0]):
                pilha.pop(0)
                #print(pilha)
                atributo_desempilhado = producao[n]
                prod = prod + ' ' + atributo_desempilhado[1]
                #print("\n\n\n prod: ", atributo_desempilhado)
                #print(prod)
                #print('pilha semantica: ', producao)
                lista_desempilhada.append(atributo_desempilhado) 
                
                producao.pop(n)
                if(i < dados_producao[0] -1):
                    n= n-1
                else:
                    producao.insert(n,['', dados_producao[1], ''])
            
            #print('producao: ')
            #print(producao)
            t = pilha[0]
            pilha.insert(0, int(tabela_transições[t][nao_terminais.get(dados_producao[1])]))
            #print('producao: ' + dados_producao[1] + ' -> ' + prod)
            #print(producao)
            
            semantico(producao, regra, lista_desempilhada, linha, coluna)
            
            prod = ''
            lista_desempilhada =[]
            
        elif(pesquisa == 'Acc'):
             if(erro_semantico == False):
                print("Criando obj:")
                analisadorSemantico()
            #print('Analise encerrada')
             break
        
        elif(pesquisa[0] == 'E'):
            print('------------------------------------------------------------------')
            print('ERRO SINTATICO')
            numero_erro = int(pesquisa[1:])
            print(Erros_sintaticos.get(numero_erro))
            print('linha: ', linha, 'coluna: ', coluna)
            
            if(numero_erro==17):
                print('Tal valor não corresponde á regra em curso', token )
                print(Erros_redução.get(s))
                print('linha: ', linha, 'coluna: ', coluna)
            
            # modo pânico: chama o lexico e verifica se o token é igual a ;, } ou ) 
            # se sim: continua a anlize normalmente. 
            # se não: descarta o token (chama o lexico novamente)
            while True:
                 dados_lexico = analisadorLexico(conteudo_Arq, indice, linha, coluna)
                 retorno = dados_lexico.identificado
                 indice = dados_lexico.indice
                 coluna = dados_lexico.coluna
                 linha = dados_lexico.linha
                
                 if(retorno[0] == ';' or retorno[0] == '}' or retorno[0] == ')'):
                     erro_semantico = True
                     token = dicionario_PC.get(retorno[0] , retorno[1])
                     atributo = [retorno[0], token, dicionario_tipo.get(retorno[0], retorno[2])]
                     break
                 
        
'''-------------------------------------------- SEMANTICO ------------------------------------------'''

#atributo = [lexema, token, tipo]
'''
nosso programa bugado ta usando 4 tipos: int, inteiro, real e double
esse dicionario é pra conveter real para double e inteiro pra int
é chamado na função tipos compativeis e na regra 6.
'''
converte_tipoEq = {
'real':'double',
'inteiro':'int',        
}

#usada para definir prioridade dos tipos
#e para converter o valor numerico em tipo novamente
prioridade_tipos = {
'inteiro': 1,
'int': 1,
'real': 2,
'double': 2, 
1: 'int',
2: 'double',       
}

#para definir o tipo da variavel temporaria
def tipos_prioridade(var_1, var_2):
    
    print(var_1, var_2)
    p1 = prioridade_tipos.get(var_1)
    p2 = prioridade_tipos.get(var_2)
    
    if(p1 == p2 or p1 > p2):
        tipo = prioridade_tipos.get(p1)
    elif(p1 < p2):
        tipo = prioridade_tipos.get(p2)   
    
    return tipo

    
#verifica tipos compativeis
def tipos_Compativeis(var_1, var_2):
    tipo_1 = converte_tipoEq.get(var_1, var_1)
    tipo_2 = converte_tipoEq.get(var_2, var_2)
    retorno = False
    
    if(tipo_1 == tipo_2):
        retorno = True
    elif((tipo_1 == 'double' and tipo_2 == 'int') or (tipo_1 == 'int' and tipo_2 == 'double')):
        retorno = True
    return retorno


def semantico(pilha_semantica, regra, lista_desempilhada, linha, coluna):
    
    global conteudo, numTemp, erro_semantico
    #print(regra)
    
    if(regra == 5):
        conteudo = conteudo + '\n\n\n' ## arquivo objeto=conteudo ; 
        
    elif(regra == 6):
    
        #id recebe tipo de TIPO
        manipulador_1 = lista_desempilhada[0] #id.tipo<-Tipo.tipo
        manipulador_2 = lista_desempilhada[1]
        #coloca no dicionario de palavras reservadas o novo tipo do id
        dicionario_tipo[manipulador_1[0]] = converte_tipoEq.get(manipulador_2[2], manipulador_2[2]) 
        lista_desempilhada[0][2] = dicionario_tipo.get(manipulador_1[0], manipulador_2[0])

        conteudo = conteudo + lista_desempilhada[0][2]+ ' ' +lista_desempilhada[0][0]+';\n'
        
    elif(regra==7 or regra ==8 or regra== 9):
       
        temp_1 = pilha_semantica[0]
        pilha_semantica.pop(0)
        pilha_semantica[0][2] = lista_desempilhada[0][2]
        pilha_semantica.insert(0, temp_1)
        
        
        
    elif(regra==11):
         
        if(lista_desempilhada[1][2] == 'literal'):
            conteudo = conteudo + 'scanf("%s", '+lista_desempilhada[1][0]+');\n'       
        elif(lista_desempilhada[1][2] == 'int' or lista_desempilhada[1][2] == 'inteiro'):
            conteudo = conteudo + 'scanf("%d", &'+lista_desempilhada[1][0]+');\n'
        elif(lista_desempilhada[1][2] == 'real' or lista_desempilhada[1][2] == 'double' ):
            conteudo = conteudo + 'scanf("%d", &'+lista_desempilhada[1][0]+');\n'
        else:
             print('------------------------------------------------------------------')
             print('Erro: Variável não declarada. \n Linha: ', linha,  ' \n Coluna: ',  coluna)
             erro_semantico = True
             

    
    elif(regra == 12):
        
        if(lista_desempilhada[1][2] == 'int' or lista_desempilhada[1][2] == 'inteiro'):
            conteudo = conteudo + 'printf("%d", '+lista_desempilhada[1][0]+');\n'
        elif(lista_desempilhada[1][2] == 'real' or lista_desempilhada[1][2] == 'double'):
            conteudo = conteudo + 'printf("%lf", '+lista_desempilhada[1][0]+');\n'
        elif(lista_desempilhada[1][2] == 'literal' and lista_desempilhada[1][1] == 'id'):
            conteudo = conteudo + 'printf("%s", '+lista_desempilhada[1][0]+');\n'
        else:
            conteudo = conteudo + 'printf('+lista_desempilhada[1][0]+');\n'
            
          
    elif(regra == 13 or regra == 14 or regra == 19 or regra ==21):

        temp_1 = pilha_semantica[0]
        pilha_semantica.pop(0)
       
        pilha_semantica[0][0] = lista_desempilhada[0][0]
        pilha_semantica[0][1] = lista_desempilhada[0][1]
        pilha_semantica[0][2] = lista_desempilhada[0][2]
 
        pilha_semantica.insert(0, temp_1)
        

    
    elif(regra == 15):

        if(lista_desempilhada[0][2] == ''):
            print('------------------------------------------------------------------')
            print('Erro 2: Variável não declarada.\nLinha: ', linha)
            erro_semantico = True
     
        else:    
            temp_1 = pilha_semantica[0]
            pilha_semantica.pop(0)
        
            pilha_semantica[0][0] = lista_desempilhada[0][0]
            pilha_semantica[0][1] = lista_desempilhada[0][1]
            pilha_semantica[0][2] = lista_desempilhada[0][2]  
            
            pilha_semantica.insert(0, temp_1)
        
    elif(regra == 17):
        
        verifica = tipos_Compativeis(lista_desempilhada[0][2], lista_desempilhada[2][2])
        if(lista_desempilhada[0][2] == ''):
            print('------------------------------------------------------------------')
            print('Erro 3: Variável não declarada.\nLinha: ', linha)
            erro_semantico = True
            
        elif(verifica == False):
            print('------------------------------------------------------------------')
            print('Erro: Tipos diferentes para atribuição.\nLinha: ', linha)
            erro_semantico = True
        else:
            conteudo = conteudo + lista_desempilhada[0][0]+ lista_desempilhada[1][2] + lista_desempilhada[2][0]+ ';\n'
        
    elif(regra == 18):

        verifica = tipos_Compativeis(lista_desempilhada[0][2], lista_desempilhada[2][2])
        if(verifica == False or lista_desempilhada[0][2] == 'lit'):
            print('------------------------------------------------------------------')
            print('Erro: Operandos com tipos incompatíveis.\nLinha: ', linha)
            erro_semantico = True

        else:
            tipo_varTemp = tipos_prioridade(lista_desempilhada[0][2], lista_desempilhada[2][2])
            temp_1 = pilha_semantica[0]
            pilha_semantica.pop(0)
        
            pilha_semantica[0][0] = 'T'+ str(numTemp)
            pilha_semantica[0][2] = tipo_varTemp 
            print(pilha_semantica[0])
            conteudo =  conteudo + 'T'+ str(numTemp) +' = '+lista_desempilhada[0][0]+' '+lista_desempilhada[1][2]+' '+lista_desempilhada[2][0]+';\n'
            numTemp = numTemp+1
        
            pilha_semantica.insert(0, temp_1)

    
    elif(regra == 20):

        if(lista_desempilhada[0][2] == ''):
            print('------------------------------------------------------------------')
            print('Erro 4: Variável não declarada.\nLinha: ', linha)
            erro_semantico = True
        else:
            
            temp_1 = pilha_semantica[0]
            pilha_semantica.pop(0)
            
            pilha_semantica[0][0] = lista_desempilhada[0][0]
            pilha_semantica[0][1] = lista_desempilhada[0][1]
            pilha_semantica[0][2] = lista_desempilhada[0][2] 
            
            pilha_semantica.insert(0, temp_1)
        
    elif(regra == 23):
        
        conteudo = conteudo +'}\n'
    
    elif(regra == 24):
        
        conteudo = conteudo +  'if(' + lista_desempilhada[2][0]+ '){\n'
        
    elif(regra == 25):
        
        verifica = tipos_Compativeis(lista_desempilhada[0][2], lista_desempilhada[2][2])
        if(verifica == False):
            print('------------------------------------------------------------------')
            print('Erro: Operandos com tipos incompatíveis.\nLinha: ', linha)
            erro_semantico = True
            
        else:
            temp_1 = pilha_semantica[0]
            pilha_semantica.pop(0)
            
            pilha_semantica[0][0] = 'T'+ str(numTemp)
            conteudo = conteudo + 'T'+ str(numTemp) +' = '+lista_desempilhada[0][0]+' '+lista_desempilhada[1][2]+' '+lista_desempilhada[2][0]+';\n'
            numTemp = numTemp+1
            
            pilha_semantica.insert(0, temp_1)


def analisadorSemantico():
    codigo = open('codigo.txt','w')
    codigo.write('#include<stdio.h>\ntypedef char literal[256];\n\nvoid main(void)\n{\n')
    codigo.write('/*----Variaveis temporarias----*/\n')
    for i in range(numTemp):
        codigo.write('int T'+ str(i) + ';\n')
    codigo.write('/*-----------------------------*/\n')
    for i in conteudo:
        codigo.write(i)
    codigo.write('}')
    codigo.close()
    
    arquivoC = open('codigo.c', 'w')
    codigo = open('codigo.txt')
    for line in codigo:
        arquivoC.write(line)
    arquivoC.close()
    codigo.close()
       

def main():
    
    nome = input('nome do arquivo:')
    arquivo = open(nome, 'r')
    conteudo_Arq = arquivo.read() + ' ' 
        
    analisadorSintatico(conteudo_Arq)

    #print('---------------------------------------------------------')
    #print(conteudo)
    arquivo.close() 
    #C:\Users\tldcardeal\Downloads\222.txt

main()
