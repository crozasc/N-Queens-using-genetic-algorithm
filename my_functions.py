import random
        
def geneticAlgorithm(population, bestFitness, cross_probability, mutation_probability):
    # A function that create a new generation of chromosomes with Roulette Wheel
    new_population = []
    probabilities = [probability(n, bestFitness) for n in population] 
    populationWithProbabilty = zip(population, probabilities)
    populationWithProbabilty = list(populationWithProbabilty)

    while(len(new_population)!=len(population)):

        if myFloatRandom() <= cross_probability:
            x = rouletteWheel(populationWithProbabilty)
            y = rouletteWheel(populationWithProbabilty) 
            while x == y:
                y = rouletteWheel(populationWithProbabilty) 
            child = reproduce(x, y)
            child = correction(child)

            if myFloatRandom() <= mutation_probability:
                child = mutate(child) 
            
            if child not in new_population:
                new_population.append(child)

    return new_population

def printGeneration(population, populationFitnesss, i):
    # A function that print the generation and his respectives chromosomes
    print("Generation "+ str(i+1) + ":")
    for i in range(len(population)):
        print("Chromosome = " + str(population[i]) + " Fitness = " + str(populationFitnesss[i]))

def solution(population, populationFitness, bestFitness):
    # Afunction that return an array with the solutions of the problem
    solutions = []

    for i in range(len(population)):
        if(populationFitness[i] == bestFitness):
            solutions.append(population[i])

    return solutions

        
def myFloatRandom():
    # A simple function that return a random float number between 0 and 1
    return (random.uniform(0,1))

def myIntRandom(a, b):
    # A simple function that return a random int number between a and b
    if(a < b):
        return (random.randint(a, b))

    elif (a > b):
        return (random.randint(b, a))

    else:
        return (a)

def maxCombinations(nqueens):
    # A function that return nqueens!, that is, factorial
    aux = 1
    for i in range(1,nqueens+1):
        aux = aux * i
    return aux

def firstPopulation(nqueens, sizePopulation):
    # A function that return a array with the population with unique chromosomes with genes unrepeated
    population = []
    uniqueNumbers = []
    i = 0
    maxPopulation = maxCombinations(nqueens)
    if(sizePopulation > maxPopulation):
        sizePopulation = maxPopulation
    while i != sizePopulation:
        for x in range(nqueens):
            uniqueNumbers.append(x)
        j = 0
        chromosome = []
        while j != nqueens:
            quitar = myIntRandom(0, len(uniqueNumbers)-1)
            chromosome.append(uniqueNumbers[quitar])
            uniqueNumbers.pop(quitar)
            j += 1
        if chromosome not in population:
            population.append(chromosome)
            i += 1
    return population

def diagonalCollisions(chromosome):
    # A function that return the number of collisions in diagonal
    diagonal_collisions = 0
    n = len(chromosome)
    left_diagonal = [0] * 2 * n
    right_diagonal = [0] * 2 * n
    
    for i in range(n):
        for j in range(len(chromosome)):
            if ( i != j):
                dx = abs(i-j)
                dy = abs(chromosome[i] - chromosome[j])
                if(dx == dy):
                    diagonal_collisions += 1
    return (diagonal_collisions)

def fitness(chromosome, bestFitness):
    # A function that return the fitness of a chromosome
    diagonal_collisions = diagonalCollisions(chromosome)
    return int(bestFitness - (diagonal_collisions))

def probability(chromosome, bestFitness):
    # A function that return the probability of a chromosome succesful
    return (fitness(chromosome, bestFitness) / bestFitness)

def rouletteWheel(populationWithProbabilty):
    # A function that pick a random chromosome according to its succesful
    total = sum(prob for chromosome, prob in populationWithProbabilty)
    wheelNum = random.uniform(0, total)

    aux = 0
    for chromosome, prob in populationWithProbabilty:
        if (wheelNum <= aux + prob):
            return chromosome
        else : aux = aux + prob

def reproduce(x, y):
    # A function that pick two chromosomes and reproduces them to return a mixture of their genes
    n = len(x)
    crossPoint = myIntRandom(0, n - 1)
    return x[0:crossPoint] + y[crossPoint:n]

def correction(x):
    #A function that makes a correction of a chromosome after a reproduction, preventing the chromosome from having repeated genes
    posRepeated = []
    nonSeen = []

    for i in range(len(x)):
        nonSeen.append(i)

    for i in range(len(x)):
        if (x[i] in nonSeen): 
            nonSeen.remove(x[i])
        for j in range (i+1, len(x)):
            if (x[i] == x[j]):
                posRepeated.append(i)

    for i in range(len(posRepeated)):
        unique = myIntRandom(0, len(posRepeated)-1)
        x[posRepeated[0]] = nonSeen[unique]
        posRepeated.pop(0)
        nonSeen.pop(unique)

    return x

def mutate(x):
    # A function that pick a chromosome and mutate one gene
    n = len(x)
    pos1 = myIntRandom(0, len(x)-1)
    pos2 = myIntRandom(0, len(x)-1)

    while pos1 == pos2:
        pos2 = myIntRandom(0, len(x)-1)

    x[pos1], x[pos2] = x[pos2], x[pos1]

    return x

def printBoard(nqueens, solutions):
    # A function that print the solution's board
    board = []

    for x in range(nqueens):
        board.append(["X"] * nqueens)

    for i in range(nqueens):
        z = int(solutions[i])
        board[i][z]="Q"

    for row in board:
        print (" ".join(row))

