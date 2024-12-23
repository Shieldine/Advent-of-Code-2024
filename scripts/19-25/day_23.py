import networkx as nx

connections = []

with open("../../inputs/19-25/day_23.txt") as file:
    for line in file:
        connections.append(tuple(line.strip().split("-")))

g = nx.from_edgelist(connections)

all_cliques = nx.enumerate_all_cliques(g)
triad_cliques = [x for x in all_cliques if len(x) == 3]

filtered = []

for clique in triad_cliques:
    for node in clique:
        if node.startswith("t"):
            filtered.append(clique)
            break

print(len(filtered))
