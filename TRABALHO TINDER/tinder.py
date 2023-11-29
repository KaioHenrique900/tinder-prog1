# Alunos: Gabriel Silva de Oliveira, Kaio Henrique

import pickle
import gerarConexoes
import estatisticas

def main():

    gerarConexoes.gerarConexoes()
    with open("dados.bin", "rb") as arq:
        usuarios = pickle.load(arq)
        conexoes = pickle.load(arq)

        logins = list(usuarios.keys())

        estatisticas.quicksort(logins,0,len(logins)-1, conexoes, usuarios)

        estatisticas.buscarDados(logins, usuarios)

    

if __name__=="__main__":
    main()
