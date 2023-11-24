import pickle

def gerarConexoes(conexoes):
    conHist = []
    with open("D:\\IFES\\Prog II\\TRABALHO TINDER\\historico.bin", "rb") as f:
        tam = int(pickle.load(f))
        for i in range(tam):
            h = pickle.load(f)
            conHist.append(h)

            if h[1] not in conexoes[h[0]][0] and h[1] not in conexoes[h[0]][2]:
                conexoes[h[0]][0].append(h[1])
    
    return conexoes