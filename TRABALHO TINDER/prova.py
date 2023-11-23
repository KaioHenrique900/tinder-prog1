def usersDisp(login, conexoes):
    disp = []
    gostou, mutuos = conexoes[login]
    for login2 in conexoes:
        if (login2 not in gostou) and (login2 not in mutuos) and (login2 != login):
            disp.append(login2)
    return disp[:20]

def calcIdade(d1, d2):
    ano = d2[2] - d1[2]

    if d2[1] - d1[1] < 0:
        ano -= 1
    elif d2[0] - d1[0] > 0:
        ano -= 1
    
    return ano

def dist(login, disp):
    return 0

def f_interessantes(login, d, x1, x2, hoje, disponiveis, usuarios, gps):
    interes = []
    for disp in disponiveis:
        idade = calcIdade(usuarios[disp][2], hoje)
        distancia = dist(gps[login], gps[disp])

        if (idade >= x1 and idade <= x2) and (usuarios[login][1] == usuarios[disp][1] or distancia <= d):
            interes.append(disp)
    
    return interes