#Gabriel Silva e Kaio Henrique
import gerarConexoes as gCon
import pickle

def contLinhasHist(conexoes):
    cont = 0
    for u in conexoes:
        for x in conexoes[u][0]:
            cont+=1
        for x in conexoes[u][2]:
            cont += 1
    return cont

def backup(usuarios, conexoes):
    with open("D:\\IFES\\Prog II\\TRABALHO TINDER\\backup.bin", "wb") as f:
        pickle.dump(usuarios, f)
        pickle.dump(conexoes, f)

    """with open("D:\\IFES\\Prog II\\TRABALHO TINDER\\historico.bin", "w") as f:
        for u in conexoes:
            for x in conexoes[u][1]:
                t = (conexoes[u][1], x)
                pickle.dump(t, f)
            for x in conexoes[u][2]:
                t = (conexoes[u][2], x)
                pickle.dump(t, f)"""
    
    with open("D:\\IFES\\Prog II\\TRABALHO TINDER\\historico.bin", "wb") as f:
        pickle.dump(str(contLinhasHist(conexoes)), f)
        for u in conexoes:
            for x in conexoes[u][0]:
                t = (u, x)
                pickle.dump(t, f)
            for x in conexoes[u][2]:
                t = (u, x)
                pickle.dump(t, f)

def main():
    #          {LOGIN : (LOGIN, CIDADE, NASCIMENTO)}
    usuarios = {"kaio" : ("Kaio", "Serra", (9,1,2003)),
                "ju" : ("Julia", "Serra", (12,5,1995)),
                "will" : ("Will Smith", "Philadelphia", (20,10,1984)),
                "thais" : ("Thais Araujo", "Sao Paulo", (12,8,1977))
                }
    
    #          {LOGIN : ([GOSTEI], [GOSTOU], [MUTUOS])}
    conexoes = {"kaio" : (["ju"], [], ["thais"]),
                "ju" : ([], ["kaio"], ["will"]),
                "will" : (["thais"], [], ["ju"]),
                "thais": ([], ["will"], ["kaio"])
                }
    
    conexoes1 = {"kaio" : (["ju"], [], ["thais"]),
                "ju" : (["thais"], ["kaio"], ["will"]),
                "will" : (["thais"], [], ["ju"]),
                "thais": ([], ["will", "ju"], ["kaio"]),
                }
    
    backup(usuarios, conexoes1)
    conexoes = gCon.gerarConexoes(conexoes)
    print(conexoes)

if __name__ == "__main__":
    main()