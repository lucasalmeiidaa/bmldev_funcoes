#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from os import listdir
from os.path import join
# from bmldev.loads import txts_to_pd
from unicodedata import normalize
import re


# # remover_acentos

# In[3]:


def remover_acentos(txt):
    """Função para retirar acentos.
    Argumentos:
    txt: String a ser normalizada
    """
    
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


# # buscar_bases

# In[18]:


def buscar_bases(path, nomes=None):
    
    """Função para retornar o caminho das bases de forma genérica, desconsiderando acentos e letras maiúsculas.
    'AH, MAS QUAL A DIFERENÇA DESSA PRO GLOB?'
    R: O GLOB DIFERENCIA LETRAS MAIÚSCULAS DE MINÚSCULAS.
    
    Argumentos:
    path (STRING): Caminho da pasta que contem as bases.
        Ex.: 'bases', './Bases', './XXXXX/BaSeS'
    
    nomes (LISTA): Lista com as palavras-chave que deseja-se procurar nos arquivos bases.
        Ex.: Desejo procurar um arquivo na pasta 'bases' que contém a palavra 'manaus', 'MANAUS', 'Manaus', ou até mesmo
            'MaNaUs' e outro arquivo que contém a palavra 'Porto Velho', 'porto velho' ou 'PoRtO VelHo'. Como faço?
            No argumento 'nomes' eu atribuo uma lista com as palavras ['manaus', 'porto velho'].
            
        *OBS.: A ordem dessa lista é a ordem que serão retornados os caminhos
        
    Essa função utiliza expressões regulares, a famosa biblioteca 're'. Isso significa que você pode usar estrutura regex
    na lista de nomes, generalizando da sua maneira.
        Ex.: Eu desejo obter um caminho de um arquivo que possuir a palavra 'picolé' ou 'picolés'. Usando a expressão
        'picole[s]?' eu consigo obter o caminho tanto se o arquivo estiver com a palavra 'picolé' no plural ou não.
        
    A função retornará o caminho das bases que derem match com as palavras-chave passadas na lista 'nomes', por isso,
    ao utilizar a função, utilize as variaveis que você deseja armazenar os caminhos separas por vírgula.
        Ex.: Desejo encontrar as bases com as seguintes palavras-chave:
            - pf;
            - pj;
            - monofasicos e
            - glpca
            
            Então eu posso usar a função da seguinte forma:
            
            pf, pj, mono, glpca = buscar_bases('bases', nomes=['pf', 'pj', 'monofasico[s]?', 'glpca'])
        
            Em que pf, pj, mono e glpca retornam o caminho completo das bases.
        
                                                 ／　　　ヽ |_
                                                ￣＼　　　　 ＼
                                                ／￣　/|/| /ﾚ､ ヽ＿
                                                ￣＼ Yヘ |/ヘ幺　∠
                                                 ＜_|(･> <･) 6) ／
                                                   (ﾞ　_　ﾞ／＜
                                                    ＞､ーイ￣￣
                                                   ／厂ヽ／￣/＼
                                                   ( ｜　(🇧🇷)(>　)
                                                   (ﾐ)ﾆ只ニ(ﾐ_／
                                                    /〈/L〉 ヽ
                                                   ｜　ヽ　　|
                                                   〈＿／ ＼＿〉
                                                   ／　)　 (　＼
        """
    
    

    for nome in nomes:
        for file in listdir(path):
            if (re.search(nome, remover_acentos(file), flags=re.IGNORECASE)):
#             if re.findall(nome, remover_acentos(file), flags=re.IGNORECASE) != []:
            #         print (file)
                caminho = join(path, file)
                yield caminho 


# In[16]:


# if (re.search('monofasico[s]?', 'monofasico', flags=re.IGNORECASE)):
#     print('OK')
# else:
#     print('NO :(')


# In[15]:


# pf, pj, mono, glpca = buscar_bases('bases', nomes=['pf', 'pj', 'monofasico[s]?', 'glpca'])

