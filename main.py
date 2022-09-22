from myfunctions import *


'''
seed = int(input("Seed: "))
nqueens = int(input("Number of Queens: "))
sizePopulation = int(input("Size of Population: "))
cross_probability = float(input("Cross probability: "))
mutation_probability = float(input("Mutation probability: "))
max_generations = sizePopulation = int(input("Maximum of generations: "))
'''
seed = 5
nqueens = 5
sizePopulation = 10
cross_probability = 0.9
mutation_probability = 0.3
max_generations = sizePopulation = 1

random.seed(seed)
bestFitness = (nqueens * (nqueens - 1)) / 2
population = [myChromosome(nqueens) for _ in range(10)]
generation = 1
for _ in range(max_generations):
    genetic_algorithm(population, bestFitness, cross_probability, mutation_probability)
    generation += 1