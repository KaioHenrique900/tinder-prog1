#Gabriel Silva e Kaio Henrique
import gerarConexoes as gCon
import pickle

def backup(usuarios, conexoes):
    with open("D:\\IFES\\Prog II\\TRABALHO TINDER\\backup.bin", "wb") as f:
        pickle.dump(usuarios, f)
        pickle.dump(conexoes, f)

    with open("D:\\IFES\\Prog II\\TRABALHO TINDER\\historico.bin", "wb") as f:
        for u in usuarios:
            for x in usuarios[u][1]:
                t = (usuarios[u][1], x)
                pickle.dump(t)
            for x in usuarios[u][2]:
                t = (usuarios[u][2], x)
                pickle.dump(t)

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
    
    backup(usuarios, conexoes)
    conexoes = gCon.gerarConexoes()

if __name__ == "__main__":
    main()