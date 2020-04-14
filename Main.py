from FileReader import readnetwork
from GA import *

def run(network,populationSize,gen):
    fcEval = routeFitness
    gaParam = {'popSize': populationSize, 'noGen': gen}
    problParam = {'function': fcEval, 'network': network}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()
    bestChromo=None;
    for g in range(gaParam['noGen']):
        #ga.oneGeneration()
        ga.oneGenerationElitism()
        #ga.oneGenerationSteadyState()

        bestChromo = ga.bestChromosome()
        print('Best solution in generation ' + str(g+1) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(bestChromo.fitness))

    print("Solution is: ",bestChromo)




def main():
    while True:
        print("Menu:")
        print("1. Start \n")
        print("0. Exit")

        cmd = input()
        if cmd == "1":
            print("Insert file name: ")
            fileName = input()
            if (fileName!=""):
                print("Insert population size:")
                populationSize = int(input())
                print("Insert number of populations: ")
                generatii=int(input())
                network = readnetwork(fileName)

                run(network,populationSize,generatii)
        else:
            break

main()


