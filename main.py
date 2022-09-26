from my_functions import *

while True:
    try:
        seed = int(input("Seed: "))
    except ValueError:
        print("Numeric digits only please.")
    else:
        break

while True:
    try:
        nqueens = int(input("Number of Queens: "))
        if (nqueens <= 2):
            print("Must be positive and greater than 0.")
            continue
        else:
            break
    except ValueError:
        print("Numeric digits only please.")

while True:
    try:
        sizePopulation = int(input("Size of Population: "))
        if (sizePopulation <= 0):
            print("Must be positive and greater than 0.")
            continue
        else:
            break
    except ValueError:
        print("Numeric digits only please.")

while True:
    try:
        cross_probability = float(input("Cross probability: "))
        if (cross_probability < 0 or cross_probability > 1):
            print("Must be a number between 0 and 1.")
            continue
        else:
            break
    except ValueError:
        print("Decimal numbers only please.")

while True:
    try:
        mutation_probability = float(input("Mutation probability: "))
        if (mutation_probability < 0 or mutation_probability > 1):
            print("Must be a number between 0 and 1.")
            continue
        else:
            break
    except ValueError:
        print("Decimal numbers only please.")

while True:
    try:
        max_generations = int(input("Maximum of generations: "))
        if (max_generations <= 0):
            print("Must be positive and greater than 0.")  
            continue
        else:
            break 
    except ValueError:
        print("Numbers only please.")

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
