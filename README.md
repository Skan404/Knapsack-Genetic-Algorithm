**Knapsack Problem: Genetic Algorithm vs. Brute Force**

This project explores two different approaches to solving the classic Knapsack Problem: a Genetic Algorithm and a Brute Force method. The goal is to select a combination of items with the maximum total value that can fit into a knapsack with a limited weight capacity.

**Project Structure**

The repository contains the following key files:

for_students.py: The main implementation of the Genetic Algorithm.

brute_force.py: An implementation of the Brute Force approach, which guarantees an optimal solution but is much slower.

data.py: A helper script to load item data from CSV files.

knapsack-small.csv: A small dataset for quick testing and debugging.

knapsack-big.csv: A larger and more complex dataset to demonstrate the effectiveness of the Genetic Algorithm.

**Algorithms**

**Genetic Algorithm**

The Genetic Algorithm is a heuristic inspired by the process of natural selection. It works with a population of potential solutions and evolves them over several generations to find a high-quality solution.

The implementation in for_students.py includes the following key steps:

Initialization: A random population of solutions (individuals) is created. Each individual is a binary vector representing the presence or absence of an item in the knapsack.

Fitness Evaluation: Each individual's fitness is calculated based on the total value of the items it represents. If the total weight exceeds the knapsack's capacity, the fitness is zero.

Selection: Parents are selected from the population using roulette wheel selection, where individuals with higher fitness have a greater chance of being chosen.

Crossover: Selected parents are combined using a one-point crossover to create new offspring.

Mutation: A random bit in the offspring's chromosome is flipped to introduce diversity.

Elitism: The best individual from the current generation is carried over to the next to ensure the best-found solution is not lost.

The algorithm's progress and the fitness of the population over generations are visualized using matplotlib.

**Brute Force**

The Brute Force algorithm, implemented in brute_force.py, systematically checks every possible combination of items to find the absolute best solution. While it guarantees optimality, its computational complexity makes it impractical for large datasets.

**How to Run**

Ensure you have Python and the following libraries installed:

pandas, matplotlib

To run the Genetic Algorithm:

python for_students.py

To run the Brute Force algorithm (note: may be very slow with knapsack-big.csv):

python brute_force.py
