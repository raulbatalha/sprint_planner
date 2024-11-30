import pandas as pd

# Definição das histórias de usuário
histories = [
    {"id": 1, "complexity": 5},
    {"id": 2, "complexity": 8},
    {"id": 3, "complexity": 3},
    {"id": 4, "complexity": 13},
    {"id": 5, "complexity": 8},
    {"id": 6, "complexity": 5},
    {"id": 7, "complexity": 8},
    {"id": 8, "complexity": 13},
    {"id": 9, "complexity": 13},
]

# Definição dos membros da equipe e suas senioridades
members = {
    "Membro A": {"seniority": 3},
    "Membro B": {"seniority": 2},
    "Membro C": {"seniority": 1},
    "Membro D": {"seniority": 2},
    "Membro E": {"seniority": 1},
    "Membro F": {"seniority": 3},
}

# Tabela de senioridade
seniority_table = pd.DataFrame(members).T
seniority_table.columns = ["Seniority"]
seniority_table.index.name = "Member"
seniority_table.reset_index(inplace=True)

# Prazo da sprint (em horas)
sprint_deadline = 50
