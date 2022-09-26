from my_functions import *

'''           
argb
ejemplo de codigo ejecutable
entregar el mejor fitness
valores unicos en el cromosoma
'''


seed = 2
nqueens = 12
sizePopulation = 75
cross_probability = 0.95
mutation_probability = 0.05
max_generations = 500

random.seed(seed)
bestFitness = (nqueens * (nqueens - 1)) / 2
population = firstPopulation(nqueens, sizePopulation)
populationFitness = [fitness(chromosome, bestFitness) for chromosome in population]
printGeneration(population, populationFitness, int(0))
solutions = []
noSolution = 1
for i in range(max_generations-1):
    solutions = solution(population, populationFitness, bestFitness)
    if (solutions):
        print("Solved in generation " + str(i+1))
        print("The solution is " + str(solutions[0]) + " with " + str(bestFitness) + " fitness")
        printBoard(nqueens, solutions[0])
        noSolution = 0
        break

    population = geneticAlgorithm(population, bestFitness, cross_probability, mutation_probability)
    populationFitness = [fitness(chromosome, bestFitness) for chromosome in population]
    printGeneration(population, populationFitness, i+1)

if (noSolution==1):
        print("No solution founded")
        pos = 0
        theBest = int(0)
        for i in range(len(populationFitness)):
            if(populationFitness[i] > theBest):
                theBest = populationFitness[i]
                pos = i
        print("One of best chromosome is " + str(population[i]) + " with " + str(int(theBest)) + " fitness")
        printBoard(nqueens, population[i])
