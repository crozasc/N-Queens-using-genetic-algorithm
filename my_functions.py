import random

class Queen:
    def __init__(self, bestFitness, cross_probability, mutation_probability, population, generation):
        self.generation = generation
        self.bestFitness = bestFitness
        self.cross_probability = cross_probability
        self.mutation_probability = mutation_probability
        self.population = population
        self.populationFitness = [fitness(chromosome, bestFitness) for chromosome in self.population]
        self.solutions = self.solution()
        self.newPopulation = self.genetic_algorithm()

    def newGeneration(self):
        avg = 0
        for i in range(len(self.population)):
            avg = avg + self.populationFitness[i]
        avg = avg / (len(self.population))
        avg = round(avg)
        for i in range(len(self.population)):
            if (self.populationFitness[i] <= avg) and (myFloatRandom()>=0.25):
                self.population[i] = self.newPopulation[i]
        return self.population
        
    def genetic_algorithm(self):
        new_population = []
        probabilities = [probability(n, self.bestFitness) for n in self.population] #Roulette Wheel
        populationWithProbabilty = zip(self.population, probabilities)
        populationWithProbabilty = list(populationWithProbabilty)
        for _ in range(len(populationWithProbabilty)):
            x = random_pick(populationWithProbabilty)
            y = random_pick(populationWithProbabilty) 
            if myFloatRandom() <= self.cross_probability:
                child = reproduce(x, y)
            else: child = x
            if myFloatRandom() <= self.mutation_probability:
                child = mutate(child)
            new_population.append(child)
        return new_population

    def printQueen(self):
        print("Generation "+ str(self.generation) + ":")
        #for i in range(len(self.population)):
        #    print("Chromosome = " + str(self.population[i]) + " Fitness = " + str(self.populationFitness[i]))
    
    def solution(self):
        solutions = []
        for i in range(len(self.population)):
            if(self.populationFitness[i] == self.bestFitness):
                solutions.append(self.population[i])
        return solutions


        
def myFloatRandom():
    return(random.uniform(0,1))

def myIntRandom(a, b):
    if(a <= b):
        return (random.randint(a, b-1))
    else:
        return (random.randint(b, a-1))

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
        if (r <= aux + prob):
            return chromosome
        else : aux = aux + prob

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

def print_board(nqueens, solutions):
    board = []
    for x in range(nqueens):
        board.append(["x"] * nqueens)
    for i in range(nqueens):
        z = int(solutions[i])
        board[i][z]="Q"
    for row in board:
        print (" ".join(row))

