import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(["Core", "D1", "D2", "A1", "A2"])
G.add_weighted_edges_from([
    ("Core", "D1", 3), ("Core", "D2", 3),
    ("D1", "D2", 2), ("D1", "A1", 2),
    ("D1", "A2", 2), ("D2", "A2", 2),
    ("D2", "A1", 2), ("A1", "A2", 1)
])

all_paths = {}
all_distances = {}
for source in G.nodes():
    distances = nx.single_source_dijkstra_path_length(G, source, weight='weight')
    paths = nx.single_source_dijkstra_path(G, source, weight='weight')
    all_paths[source] = paths
    all_distances[source] = distances

print("Найкоротші шляхи та відстані між усіма парами вершин:")
for source in all_paths:
    print(f"\nВід вершини {source}:")
    for target in all_paths[source]:
        if target != source:
            print(f"  До {target}: шлях = {' -> '.join(all_paths[source][target])}, відстань = {all_distances[source][target]}")

