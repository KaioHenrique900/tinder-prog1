import pickle
from gerarConexoes import gerarConexoes

def disputado(conexoes, usuario):
    
    # Utilizar a resposta dessa função dentro de um if para ordenar a lista segundo o 2° critério de ordenação no txt.
    tam = len(conexoes[usuario][1]) + len(conexoes[usuario][2])
    
    return tam

def ordenar_alfabeticamente(lista):
    
    lista_ordenada = sorted(lista)
    
    return lista_ordenada

def nomes(usuarios):
    #Retornar a lista de nomes para depois ordená-los alfabeticamente
    nomes = []
    for logins in usuarios:
        nomes.append(usuarios[logins][0])
    
    return nomes

def cidades(usuarios):
    # Retornar a lista de cidades para depois ordená-las alfabeticamente
    cidades = []
    for logins in usuarios:
        cidades.append(usuarios[logins][1])
    
    return cidades


def main():
    with open("dados.bin", "rb") as arq:
        usuarios = pickle.load(arq)
        conexoes = pickle.load(arq)

        logins = list(usuarios.keys())
        CidadesUsuarios = (cidades(usuarios))
        NomesUsuarios = (nomes(usuarios))

        print(ordenar_alfabeticamente(NomesUsuarios))

if __name__=="__main__":
    main()   
