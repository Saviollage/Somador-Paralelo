import time
from multiprocessing import Pool
from timeit import default_timer as timer


def add(numbers):
    #   Função que recebe uma lista e retorna o somatorio desta
    out = 0
    for n in numbers:
        out += n
    return out


def addSync(numbers, threads):
    print('Utilizando Paralelismo')
    #   Inicia o contador de tempo
    start = timer()

    #   Executa um filtro na lista recebida, dividindo-a em N partes a serem computadas, sendo N definido pela variavel threads
    filteredNumbers = [numbers[i::threads] for i in range(threads)]

    #   Instancia da biblio de threads, que inicia a quantidade de threads desejadas
    pool = Pool(processes=threads)


    #   Uma variação assincrona da função map, que executa a funcao add() em cada elemento da minha lista tratada, ressaltando que cada elemento da lista tratada é uma sublista de numbers
    result = pool.map_async(add, filteredNumbers)

    #   Enquanto computa, mostro uma mensagem ao user
    while not result.ready():
        print("Aguarde...", end='\r')
    print('\n ---- Concluído! ----')

    #   Retorno o somatório dos elementos da lista tratada
    finalResult = sum(result.get())
    time = timer() - start

    print("Resultado: {}".format(finalResult))
    print("Tempo percorrido: {}s".format(time))

def simpleAdd(numbers):
    print('\nSem utilizar paralelismo')
    start = timer()
    r = add(numbers)
    time = timer() - start
    print("Resultado: {}".format(r))
    print("Tempo percorrido: {}s".format(time))




if __name__ == '__main__':

    numbers = range(100000000)
    #   Chamando a funcao a seguir, significa uma execução do somatorio utilizando 5 threads
    addSync(numbers, 5)
    simpleAdd(numbers)



    

