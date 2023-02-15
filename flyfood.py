import time
tempo_inicial= time.time()

def gerar_combinacao(pontos_entrega):
    if len(pontos_entrega)==1:
        return [pontos_entrega]
    v=[]
    for u in range(len(pontos_entrega)):
        t=pontos_entrega[u]
        
        remPontos_entrega= pontos_entrega[:u]+ pontos_entrega[u+1:]

        for p in gerar_combinacao(remPontos_entrega):
            v.append([pontos_entrega[u]]+p)
    return v 

file= open('input.txt', 'r')
n, m= file.readline().split()
lines= file.read().splitlines()

cordenadas={}
pontos_entrega=[]

for i in range(int(n)):
    line= lines[i].split()
    for j in line:
        if j!='0':
            cordenadas[j]=(i, line.index(j))
            pontos_entrega.append(j)
print(cordenadas)
print(pontos_entrega)

pontos_entrega.remove('R')
menor_custo= float('inf')

ListaPermutaçao= gerar_combinacao(pontos_entrega)

for i in (ListaPermutaçao):
    custo_atual=0
    c=0

    i=list(i)
    i.append('R')
    i.insert(0, 'R')

    for j in range(len(i)-1):
        custo_y= abs(cordenadas[i[c]][0]- cordenadas[i[c+1]][0])
        custo_x= abs(cordenadas[i[c]][1]- cordenadas[i[c+1]][1])
        custo_atual+=custo_x+ custo_y
        c+=1
    
    if custo_atual< menor_custo:
        menor_custo=custo_atual
        rota=i
tempo_final= time.time()
print(f"O codigo demorou {tempo_final - tempo_inicial} segundos")
print(menor_custo)
print(' '.join(rota[1:-1]))
