from my_functions import *
import sys

seed = int(sys.argv[1])
nqueens = int(sys.argv[2])
sizePopulation = int(sys.argv[3])
cross_probability = float(sys.argv[4])
mutation_probability = float(sys.argv[5])
max_generations = int(sys.argv[6])

'''python main.py 100 9 30 0.95 0.05 100'''


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
