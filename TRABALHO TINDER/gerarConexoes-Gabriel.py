import pickle
import os

os.system("cls")

def attConexoes(historico, conexoes):

    for tentativas in historico:
        # Se quem foi curtido não estiver na lista de likes de quem deu like:
        if tentativas[1] not in conexoes[tentativas[0]][0]:
            #Adicionando quem foi curtido na lista
            conexoes[tentativas[0]][0].append(tentativas[1])
            #adicionando quem gostou na lista do curtido
            conexoes[tentativas[1]][1].append(tentativas[0])
    

    # Para cada login do dicionário
    for logins in conexoes:
        # Para cada usuario na lista de GOSTEI
        for usuarios in conexoes[logins][0]:
            # Se o usuário estiver no GOSTOU & na lista de GOSTEI, significa que é mútuo
            if usuarios in conexoes[logins][1] and usuarios in conexoes[logins][0]:
                # Apago da lista de GOSTEI E GOSTOU
                conexoes[logins][0].remove(usuarios)
                conexoes[logins][1].remove(usuarios)
                # Adiciono na lista de Mútuos
                conexoes[logins][2].append(usuarios)


    
    return conexoes

def gerarConexoes():

    # Alterar o caminho para o encontrar o arquivo de acordo com o computador no qual for avaliado.
    with open ("C:\\Users\\gsdog\\Downloads\\backup10000.bin", "rb") as f:
        usuarios = pickle.load(f)
        conexoes = pickle.load(f)
        historico = pickle.load(f)
        
    #Função para atualizar o dicionário de conexões com base no histórico de tentativas de interesse.
    atualizados = attConexoes(historico, conexoes)
    

    with open ("dados.bin", "wb") as arq:
        pickle.dump(usuarios, arq)
        pickle.dump(atualizados, arq)

    return arq
