import pickle
from gerarConexoes import gerarConexoes


def quicksort(l, inf, sup, conexoes, usuarios):
    if inf < sup:
        pos =  particao(l,inf,sup, conexoes, usuarios)
        quicksort(l,inf, pos-1, conexoes, usuarios)
        quicksort(l,pos+1, sup, conexoes, usuarios)



def disputado(conexoes, usuario):
    
    # Utilizar a resposta dessa função dentro de um if para ordenar a lista segundo o 2° critério de ordenação no txt.
    tam = len(conexoes[usuario][1]) + len(conexoes[usuario][2])
    
    return tam


def nomes(usuarios):
    #Retornar a lista de nomes para depois ordená-los alfabeticamente
    nomes = []
    for logins in usuarios:
        nomes.append(usuarios[logins][0])
    
    return nomes


def particao(l, inf, sup, conexoes, usuarios):
    pivot = l[inf]
    i = inf+1
    j = sup

    while i <= j:
        while i <= j and anterior(l[i], pivot, conexoes, usuarios):
            i += 1
        while j >= i and not anterior(l[j], pivot, conexoes, usuarios):
            j -= 1
        if i < j: 
            l[i], l[j] = l[j], l[i]
    l[inf], l[j] = l[j], l[inf]
    
    return j


def anterior(x, y, conexoes, usuarios):
    if usuarios[x][1] < usuarios[y][1]: return True
    if usuarios[x][1] > usuarios[y][1]: return False

    if disputado(conexoes, x) > disputado(conexoes, y): return True
    if disputado(conexoes, x) < disputado(conexoes, y): return False

    if x < y: return True
    
    return False

def buscarDados(listaLogins, usuarios):
    with open ("top.txt", "w") as arq:
        cidadeAnterior = ''
        for login in listaLogins:
            nome = usuarios[login][0]
            cidade = usuarios[login][1]

            if cidadeAnterior != cidade:
                arq.write(cidade + " "+ nome+"\n")
                cidadeAnterior = cidade  
