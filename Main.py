#hit = encontrou no cache
#miss = nao encontrou no cache

import time #registrar tempo de execucao
from functools import lru_cache #armazenar no cache

@lru_cache()
def atividadeLenta(n):
    total = 0

    for i in range(5_000_000): #loop de 5 milhoes de vezes para simular uma atividade complexa (o uso de "_" so serve para facilitar a leitura do numero 5000000)
        total += i * n  
    return total

def teste(x):
    inicio = time.time()   #marca o tempo de inicio
    resultado = atividadeLenta(x)   #chama a funcao demorada
    duracao = time.time() - inicio  #tempo decorrido - tempo do inicio


    #o numero de hits aumentou desde a ultima vez? se sim = hit (nao foi preciso executar nada, apenas puxar do cache)
    if atividadeLenta.cache_info().hits > teste.hitsAnteriores:
        situacao = 'HIT!'
        
    #se nao, ele teve que fazer toda a atividade de alguma etapa do programa 
    else:
        situacao = 'MISS!'

    teste.hitsAnteriores = atividadeLenta.cache_info().hits #atualiza a quantidade de hitsAnteriores para que a proxima chamada possa comparar 

    print (f'[{situacao}] Valor da operacao: {resultado} | Tempo de execucao: {duracao:.2f}s')


teste.hitsAnteriores = 0  #valor inicial para comparar

#testes:
teste(4) #sempre miss pois é a primeira vez que chama o valor
teste(4) #sempre hit pois o valor ja esta no cache

teste(50) #sempre miss pois é a primeira vez que chama o valor
teste(50) #sempre hit pois o valor ja esta no cache


'''
       _ 
    __(.)= 
    \___) 
    
'''