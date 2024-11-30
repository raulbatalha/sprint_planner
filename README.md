# Sprint Planner - Planejamento de Sprint com Algoritmo Genético

O **Sprint Planner** é uma ferramenta para alocar histórias de usuário de maneira otimizada dentro de uma equipe, utilizando um algoritmo genético para distribuir as tarefas de acordo com a senioridade dos membros da equipe. A proposta é encontrar a melhor alocação possível para que o tempo total da sprint seja minimizado, respeitando um prazo determinado.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
sprint_planner/
│
├── config/
│   └── __init__.py
│   └── config.py
│
├── docs/
│   └── apresentação_planejamento_scrum.pdf
│   └── relatório_planejamento_scrum.pdf
│
├── evaluation/
│   └── __init__.py
│   └── evaluation.py
│
├── genetic_algorithm/
│   └── __init__.py
│   └── genetic_algorithm.py
│
├── resultados/
│   └── planejamento_sprint_scrum_equipe_maior.txt
│   └── planejamento_sprint_scrum_equipe_menor.txt
│   └── planejamento_sprint_scrum_equipe_normal.txt
│
├── utils/
│   └── __init__.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Como Usar

1. Clone este repositório em sua máquina local:

```bash
git clone https://github.com/seu_usuario/sprint_planner.git
cd sprint_planner
```

2. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

3. Execute o arquivo principal para calcular o planejamento da sprint:

```bash
python main.py
```

Isso irá gerar o planejamento da sprint, exibindo as alocações das tarefas e o tempo total da sprint. O arquivo `planejamento_sprint_scrum_equipe_normal.txt` será gerado com os resultados. Caso queira gerar com equipe maior ou menor faça a mudança de quantidade de membros no arquivo `config.py`.

## Como Funciona

O algoritmo genético utilizado neste projeto funciona da seguinte maneira:

1. **População Inicial**: A população inicial é gerada aleatoriamente, com cada indivíduo representando uma possível alocação das histórias de usuário para os membros da equipe.
2. **Avaliação (Fitness)**: A função de avaliação calcula o tempo total da sprint com base na carga de trabalho de cada membro da equipe, considerando sua senioridade.
3. **Seleção**: Utiliza o torneio para selecionar os indivíduos mais aptos para a próxima geração.
4. **Crossover (Cruzamento)**: O crossover é feito por um ponto de cruzamento aleatório para combinar duas alocações de tarefas.
5. **Mutação**: A mutação altera aleatoriamente a alocação de tarefas de um membro.
6. **Execução**: O algoritmo genético é executado por várias gerações até encontrar a melhor solução para alocação das tarefas dentro do tempo da sprint.

## Arquitetura

### Módulos

- **`config.py`**: Contém as configurações iniciais, como as histórias de usuário, membros da equipe, e tabelas de senioridade.
- **`evaluation.py`**: Implementa a função de avaliação (fitness function) que calcula o tempo total da sprint com base na alocação das tarefas.
- **`genetic_algorithm.py`**: Implementa o algoritmo genético, que realiza o cruzamento, mutação e seleção dos indivíduos para otimizar o tempo da sprint.
- **`utils.py`**: Contém funções auxiliares para exibir os resultados e salvar o planejamento em um arquivo.

## Exemplo de Saída

Após a execução, o planejamento da sprint será impresso no terminal e salvo em um arquivo de texto. O conteúdo do arquivo `planeamento_sprint_scrum_equipe_normal.txt` será algo como:

```
+---------------------+-----------+------------+
| História de Usuário | Membro    | Complexidade |
+---------------------+-----------+------------+
| 1                   | Membro A  | 5          |
| 2                   | Membro B  | 8          |
| 3                   | Membro C  | 3          |
| ...                 | ...       | ...        |
+---------------------+-----------+------------+

Tempo Total da Sprint: 42
A sprint será concluída dentro do prazo estipulado.
```

## Contribuições

Contribuições são bem-vindas! Se você tiver alguma sugestão ou correção, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). MIT © [Raul Batalha ](https://github.com/raulbatalha)