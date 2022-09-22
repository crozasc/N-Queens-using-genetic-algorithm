from my_functions import *

seed = int(input("Seed: "))
nqueens = int(input("Number of Queens: "))
sizePopulation = int(input("Size of Population: "))
cross_probability = float(input("Cross probability: "))
mutation_probability = float(input("Mutation probability: "))
max_generations = int(input("Maximum of generations: "))

'''
Test
seed = 1
nqueens = 7
sizePopulation = 500
cross_probability = 0.95
mutation_probability = 0.05
max_generations = 100
'''
random.seed(seed)
bestFitness = (nqueens * (nqueens - 1)) / 2
population = [myChromosome(nqueens) for _ in range(sizePopulation)]

for i in range(max_generations):
    queen = Queen(bestFitness, cross_probability, mutation_probability, population, i+1)
    queen.printQueen()
    newpopulation = queen.newGeneration()
    
    if (queen.solutions):
        print("Solved in generation " + str(queen.generation))
        print("The solution is " + str(queen.solutions[0]))
        print_board(nqueens, queen.solutions[0])
        break
#print(str(bestFitness))