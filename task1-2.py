import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Функція DFS для знаходження всіх шляхів між двома вершинами
def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            yield from dfs_paths(graph, neighbor, goal, path + [neighbor])

# Функція BFS для знаходження найкоротшого шляху
def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (vertex, path) = queue.popleft()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph.neighbors(vertex):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

G = nx.Graph()

G.add_nodes_from(["Core", "D1", "D2", "A1", "A2"])
G.add_edges_from([("Core", "D1"), ("Core", "D2"), 
                  ("D1", "D2"), ("D1", "A1"), 
                  ("D1", "A2"), ("D2", "A2"), 
                  ("D2", "A1"), ("A1", "A2")])
DG = nx.DiGraph(G)

pos = {
    "Core": (0, 2),     
    "D1": (-1, 1),      
    "D2": (1, 1),      
    "A1": (-1, 0),    
    "A2": (1, 0)       
}

nx.draw(DG, pos= pos, with_labels=True)
d_centrality = nx.degree_centrality(DG)
c_centrality = nx.closeness_centrality(DG)
b_centrality = nx.betweenness_centrality(DG)

print(f'Ступіні центральності: {d_centrality}')
print(f'Близькість вузлів: {c_centrality}')
print(f'Посередництво вузлів: {b_centrality}')


# Знаходження шляхів між "Core" і "A2" за допомогою DFS і BFS
start_node = "Core"
end_node = "A2"

print("Шляхи DFS від Core до A2:")
dfs_results = list(dfs_paths(DG, start_node, end_node))
for i, path in enumerate(dfs_results, 1):
    print(f"Шлях {i}: {' -> '.join(path)}")

print("\nШлях BFS від Core до A2:")
bfs_result = bfs_path(DG, start_node, end_node)
if bfs_result:
    print(f"Шлях: {' -> '.join(bfs_result)}")
else:
    print("Шлях не знайдено")


plt.title = 'Spanning tree protocol'
plt.show()

d_centrality = nx.degree_centrality(DG)
c_centrality = nx.closeness_centrality(DG)
b_centrality = nx.betweenness_centrality(DG)

# DFS: Досліджує глибоко по кожній гілці, тому може спочатку знайти довші шляхи (наприклад, Core -> D1 -> D2 -> A1 -> A2)
# BFS: Досліджує вершини пошарово, тому гарантовано знаходить найкоротший шлях першим.