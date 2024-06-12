N, Q = [int(x) for x in input().split()]
matriz = []

for i in range(N):
    linha = [int(x) for x in input()]
    matriz.append(linha)

def checarVizinhos(x, y):
    vizinhosVivos = 0
    try: # POS 1
        if matriz[y-1][x-1] == 1:
            vizinhosVivos += 1
    except:
        pass
    try: # POS 2
        if matriz[y-1][x] == 1:
            vizinhosVivos += 1
    except:
        pass
    try: # POS 3
        if matriz[y-1][x+1] == 1:
            vizinhosVivos += 1
    except:
        pass
    try: # POS 4
        if matriz[y][x-1] == 1:
            vizinhosVivos += 1
    except:
        pass
    try: # POS 5
        if matriz[y][x+1] == 1:
            vizinhosVivos += 1
    except:
        pass
    try: # POS 6
        if matriz[y+1][x-1] == 1:
            vizinhosVivos += 1
    except:
        pass
    try: # POS 7
        if matriz[y+1][x] == 1:
            vizinhosVivos += 1
    except:
        pass
    try: # POS 8
        if matriz[y+1][x+1] == 1:
            vizinhosVivos += 1
    except:
        pass

    return vizinhosVivos


for i in range(Q):
    # Passar Geraçao
    matrizNova = matriz

    for y in range(N):
        for x in range(N):
            celula = matriz[y][x]
            vizinhosVivos = checarVizinhos(x, y)
            '''print(f'celula[{x}][{y}]')
            print(f'tem {vizinhosVivos} vizinhos vivos')'''

            # Primeira e Segunda regra (caso de celula morta)
            if celula == 0 and vizinhosVivos == 3:
                matrizNova[y][x] = 1
                print(f'celula[{x}][{y}]')
                print(f'tem {vizinhosVivos} vizinhos vivos')
                print('viveu')
            
            # Caso de celula viva
            if (celula == 1) and (vizinhosVivos != 3 and vizinhosVivos != 2):
                matrizNova[y][x] = 0
                print(f'celula[{x}][{y}]')
                print(f'tem {vizinhosVivos} vizinhos vivos')
                print('morreu')

    matriz = matrizNova
    print(matriz)
        