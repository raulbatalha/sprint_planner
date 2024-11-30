import pandas as pd
from tabulate import tabulate

def display_results(histories, members, seniority_table, best_solution, total_time):
    allocation_table = pd.DataFrame(histories)
    allocation_table["Member"] = [seniority_table.iloc[member]["Member"] for member in best_solution]
    allocation_table["Complexity"] = [history["complexity"] for history in histories]
    allocation_table = allocation_table[["id", "Member", "Complexity"]]
    allocation_table.columns = ["História de Usuário", "Membro", "Complexidade"]

    print("\nAlocação de Tarefas e Membros:")
    print(tabulate(allocation_table, headers="keys", tablefmt="grid"))
    print(f"\nTempo Total da Sprint: {total_time}")
    return allocation_table

def save_results(allocation_table, total_time, sprint_deadline):
    filename = "resultado/planejamento_sprint_scrum_equipe_normal.txt"
    with open(filename, "w") as file:
        file.write(tabulate(allocation_table, headers="keys", tablefmt="grid"))
        file.write(f"\n\nTempo Total da Sprint: {total_time}\n")
        if total_time <= sprint_deadline:
            file.write("A sprint será concluída dentro do prazo estipulado!")
        else:
            file.write("A sprint terá atraso na entrega!")
    print(f"\nPlanejamento salvo em: {filename}")
