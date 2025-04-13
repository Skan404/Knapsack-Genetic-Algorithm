from itertools import compress
import random
import time
import matplotlib.pyplot as plt

from data import *

def initial_population(individual_size, population_size):
    return [[random.choice([True, False]) for _ in range(individual_size)] for _ in range(population_size)]

def fitness(items, knapsack_max_capacity, individual):
    total_weight = sum(compress(items['Weight'], individual))
    if total_weight > knapsack_max_capacity:
        return 0
    return sum(compress(items['Value'], individual))

def population_best(items, knapsack_max_capacity, population):
    best_individual = None
    best_individual_fitness = -1
    for individual in population:
        individual_fitness = fitness(items, knapsack_max_capacity, individual)
        if individual_fitness > best_individual_fitness:
            best_individual = individual
            best_individual_fitness = individual_fitness
    return best_individual, best_individual_fitness

def calculate_total_fitness(population):
    return sum(fitness(items, knapsack_max_capacity, individual) for individual in population)

def select_parents_roulete(population, total_fitness):
    selection_probabilities = [fitness(items, knapsack_max_capacity, individual) / total_fitness for individual in population]
    selected_parents = random.choices(population, weights=selection_probabilities, k=len(population))
    return selected_parents


def crossover_one_point_middle(parent1, parent2):
    point = len(parent1) // 2

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2


def mutate(individual):
    mutation_index = random.randrange(len(individual))

    individual[mutation_index] = not individual[mutation_index]

    return individual


items, knapsack_max_capacity = get_big()
print(items)

population_size = 100
generations = 200
n_selection = 20
n_elite = 1

start_time = time.time()
best_solution = None
best_fitness = 0
population_history = []
best_history = []
population = initial_population(len(items), population_size)
total_fitness = calculate_total_fitness(population)

for _ in range(generations):
    population_history.append(population)
    # TODO: implement genetic algorithm

    # TODO: selekcja
    parents = select_parents_roulete(population, total_fitness)

    # TODO: krzyżówka
    new_population = []
    while len(new_population) < n_selection:

        for i in range(5):
            parent1, parent2 = random.sample(parents, 2)

            child1, child2 = crossover_one_point_middle(parent1, parent2)
            new_population.extend([child1, child2])


    for i in range(len(new_population)):
        new_population[i] = mutate(new_population[i])

    elite = sorted(population, key=lambda individual: fitness(items, knapsack_max_capacity, individual), reverse=True)[
            :n_elite]
    new_population.extend(elite)


    population = new_population

    best_individual, best_individual_fitness = population_best(items, knapsack_max_capacity, population)
    if best_individual_fitness > best_fitness:
        best_solution = best_individual
        best_fitness = best_individual_fitness
    best_history.append(best_fitness)

end_time = time.time()
total_time = end_time - start_time
print('Best solution:', list(compress(items['Name'], best_solution)))
print('Best solution value:', best_fitness)
print('Time: ', total_time)

# plot generations
x = []
y = []
top_best = 10
for i, population in enumerate(population_history):
    plotted_individuals = min(len(population), top_best)
    x.extend([i] * plotted_individuals)
    population_fitnesses = [fitness(items, knapsack_max_capacity, individual) for individual in population]
    population_fitnesses.sort(reverse=True)
    y.extend(population_fitnesses[:plotted_individuals])
plt.scatter(x, y, marker='.')
plt.plot(best_history, 'r')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.show()
