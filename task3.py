import networkx as nx

def dijkstra_single(graph, source, rkey = 'distances'):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    paths = {node: [] for node in graph}
    paths[source] = [source]
    visited = set()

    while len(visited) < len(graph):
        min_dist = float('inf')
        min_node = None
        for node in graph:
            if node not in visited and distances[node] < min_dist:
                min_dist = distances[node]
                min_node = node

        if min_node is None:
            break

        visited.add(min_node)
        for neighbor, edge_data in graph[min_node].items():
            if neighbor not in visited:
                weight = edge_data['weight']
                new_dist = distances[min_node] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    paths[neighbor] = paths[min_node] + [neighbor] 
        if rkey == 'paths':           
            result = {node: path for node, path in paths.items()}
        else: 
            result = {node: dist for node, dist in distances.items()}

    return result

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
    distances = dijkstra_single(G, source)   # nx.single_source_dijkstra_path_length(G, source, weight='weight')
    paths = dijkstra_single(G, source, rkey = 'paths') 
    all_paths[source] = paths
    all_distances[source] = distances

print("Найкоротші шляхи та відстані між усіма парами вершин:")
for source in all_paths:
    print(f"\nВід вершини {source}:")
    for target in all_paths[source]:
        if target != source:
            print(f"  До {target}: шлях = {' -> '.join(all_paths[source][target])}, відстань = {all_distances[source][target]}")

