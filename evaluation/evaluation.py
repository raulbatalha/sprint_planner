def evaluate(individual, histories, seniority_table):
    total_workload = [0] * len(seniority_table)
    total_time = 0

    for i, member in enumerate(individual):
        history = histories[i]
        seniority = seniority_table.iloc[member]["Seniority"]
        total_workload[member] += history["complexity"] * seniority
        total_time = max(total_time, total_workload[member])

    return total_time,
