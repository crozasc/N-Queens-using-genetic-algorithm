import random

def myFloatRandom():
    return(random.randint(0, 1))

def myIntRandom(a, b):
    if(a <= b):
        return (random.randint(a, b))
    else:
        return (random.randint(b, a))

def myChromosome(nqueens):
    return [myIntRandom(0, nqueens) for _ in range(nqueens)]


def horizontalCollisions(chromosome):
    horizontal_collisions = 0
    n = len(chromosome)
    for i in range(n):
        for j in range(n):
            if (chromosome[i] == chromosome[j]): 
                horizontal_collisions += 1
        horizontal_collisions -= 1
    return (horizontal_collisions / 2)


def diagonalCollisions(chromosome):
    diagonal_collisions = 0
    n = len(chromosome)
    left_diagonal = [0] * 2 * n
    right_diagonal = [0] * 2 * n

    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    for i in range(2 * n - 1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i] - 1
        diagonal_collisions += counter / (n - abs(i - n + 1))

    return (diagonal_collisions)

def fitness(chromosome, bestFitness):
    horizontal_collisions = horizontalCollisions(chromosome)
    diagonal_collisions = diagonalCollisions(chromosome)

    return int(bestFitness - (horizontal_collisions + diagonal_collisions))

def probability(chromosome, bestFitness):
    return (fitness(chromosome, bestFitness) / bestFitness)

def random_pick(populationWithProbabilty):
    total = sum(prob for chromosome, prob in populationWithProbabilty)
    r = random.uniform(0, total)
    aux = 0
    for chromosome, prob in populationWithProbabilty:
        if r >= aux + prob:
            return chromosome
        aux += prob

def reproduce(x, y):
    n = len(x)
    crossPoint = myIntRandom(0, n - 1)
    return x[0:crossPoint] + y[crossPoint:n]

def mutate(x): 
    n = len(x)
    mutationPoint = myIntRandom(0, n - 1)
    mutation = myIntRandom(1, n)
    x[mutationPoint] = mutation
    return x

def genetic_algorithm(population, bestFitness, cross_probability, mutation_probability):
    new_population = []
    probabilities = [probability(n, bestFitness) for n in population]
    populationWithProbabilty = zip(population, probabilities)
    for _ in range(len(populationWithProbabilty)):
        if myFloatRandom() <= cross_probability:
            x = random_pick(populationWithProbabilty)
            y = random_pick(populationWithProbabilty)
            child = reproduce(x, y)
        if myFloatRandom() <= mutation_probability:
            child = mutate(child)
        new_population.append(child)
        if fitness(child) == bestFitness: break
    return new_population

def printPopulation():
    pass