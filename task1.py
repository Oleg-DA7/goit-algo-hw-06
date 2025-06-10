import networkx as nx
import matplotlib.pyplot as plt

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

plt.title = 'Spanning tree protocol'
plt.show()

d_centrality = nx.degree_centrality(DG)
c_centrality = nx.closeness_centrality(DG)
b_centrality = nx.betweenness_centrality(DG)
