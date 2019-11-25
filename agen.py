# Import package search
from search import *

# Map searching nya
the_map = UndirectedGraph(dict(
    Sheffield=dict(Nottingham=40),
    Liverpool=dict(Nottingham=110, Shrewsbury=70),
    Cardif=dict(Bristol=50),
    Manchester=dict(Liverpool=30, Sheffield=40),
    Oxford=dict(Southampton=70),
    Nottingham=dict(Bham=50, Oxford=100),
    Bham=dict(Oxford=70, Bristol=90),
    Shrewsbury=dict(Bham=50, Aberystwyth=80, Cardiff=110),
    Bristol=dict(Southampton=80),
    Aberystwyth=dict(Cardiff=120)
))

# Buat model permasalahannya
problem = GraphProblem('Manchester', 'Southampton', the_map)

# Hasil BFS
print("Hasil BFS :")
bfs = [node.state for node in breadth_first_graph_search(problem).path()]
print(bfs)

# Hasil DFS
print("Hasil DFS :")
dfs = [node.state for node in depth_first_graph_search(problem).path()]
print(dfs)