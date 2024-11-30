from config import histories, members, seniority_table, sprint_deadline
from genetic_algorithm import run_genetic_algorithm
from utils import display_results, save_results

def main():
    best_solution, total_time = run_genetic_algorithm(histories, members, seniority_table)
    allocation_table = display_results(histories, members, seniority_table, best_solution, total_time)
    
    save_results(allocation_table, total_time, sprint_deadline)

if __name__ == "__main__":
    main()
