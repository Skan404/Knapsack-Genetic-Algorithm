# Knapsack Problem with Genetic Algorithm and Brute Force

## Project Description

This project provides a Python implementation of two different methods for solving the classic **Knapsack Problem**: a **Genetic Algorithm** and a **Brute Force** search. The goal is to find the most valuable combination of items that can fit into a knapsack without exceeding its weight capacity.

---

## Features

-   **Genetic Algorithm Implementation:**
    -   **Population-based optimization**: Evolves a population of potential solutions over multiple generations.
    -   **Fitness Function**: Evaluates each solution based on the total value of items. Solutions that exceed the knapsack's capacity are penalized with a fitness score of zero.
    -   **Roulette Wheel Selection**: Selects parents for the next generation, giving a higher probability to fitter individuals.
    -   **One-Point Crossover**: Creates new offspring by combining genetic information from two parents.
    -   **Mutation**: Introduces random changes into the population to maintain genetic diversity and explore the solution space.
    -   **Elitism**: Preserves the best solution from the current generation, ensuring it is not lost in subsequent generations.
-   **Brute Force Implementation:**
    -   **Exhaustive Search**: Systematically evaluates every possible combination of items.
    -   **Guaranteed Optimality**: Always finds the absolute best solution to the problem.
    -   Serves as a benchmark to evaluate the performance of the Genetic Algorithm.
-   **Data Handling & Visualization:**
    -   Loads item data (name, weight, value) from `.csv` files.
    -   Includes both a small and a large dataset for testing.
    -   Visualizes the Genetic Algorithm's performance and fitness progression over generations using `matplotlib`.

---

## Project Structure

-   **`for_students.py`**: The main script that runs the **Genetic Algorithm**. It handles the initialization, evolution, and visualization of the results.
-   **`brute_force.py`**: The script that implements the **Brute Force** approach to find the optimal solution.
-   **`data.py`**: A helper module responsible for loading the datasets from the CSV files using `pandas`.
-   **`knapsack-small.csv`**: A small dataset for quick testing and validation.
-   **`knapsack-big.csv`**: A larger dataset designed to test the performance and scalability of the algorithms.
-   **`requirements.txt`**: A file listing the libraries required to run the project.

---

## Installation

1.  Clone the repository to your local machine:
    ```bash
    git clone https://github.com/Skan404/Knapsack-Genetic-Algorithm
    cd Knapsack-Genetic-Algorithm
    ```

2.  Install the required dependencies from `requirements.txt`:
    ```bash
    pip install pandas matplotlib
    ```

---

## Usage

To run the project and compare the two approaches, execute the following commands in the main project directory.

1.  To run the **Genetic Algorithm**:
    ```bash
    python for_students.py
    ```

2.  To run the **Brute Force** algorithm:
    ```bash
    python brute_force.py
    ```
    *(**Warning**: Running the Brute Force script with the `knapsack-big.csv` dataset will be extremely time-consuming due to its high computational complexity.)*
