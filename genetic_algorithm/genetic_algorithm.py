import random
from deap import base, creator, tools, algorithms
from evaluation import evaluate

def run_genetic_algorithm(histories, members, seniority_table):
    # Configuração do DEAP
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    toolbox = base.Toolbox()
    
    toolbox.register("attr_member", random.randint, 0, len(members) - 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_member, len(histories))
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", evaluate, histories=histories, seniority_table=seniority_table)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutUniformInt, low=0, up=len(members) - 1, indpb=0.1)
    toolbox.register("select", tools.selTournament, tournsize=3)

    # Parâmetros do algoritmo genético
    population_size = 100
    num_generations = 50

    # Inicializa a população
    population = toolbox.population(n=population_size)

    # Execução do algoritmo genético
    for _ in range(num_generations):
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
        fits = toolbox.map(toolbox.evaluate, offspring)
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit
        population = toolbox.select(offspring, k=population_size)

    best_solution = tools.selBest(population, k=1)[0]
    total_time = evaluate(best_solution, histories, seniority_table)[0]
    return best_solution, total_time
