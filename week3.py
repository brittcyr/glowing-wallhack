from random import choice
import random


def contract(edge_list, num_nodes):
    for iteration in range(num_nodes-2):
        first, second = edge_list[0]

        # Merge nodes
        new = []
        for edge in edge_list:
            edge = [edge[0], edge[1]]
            if edge[0] == second:
                edge[0] = first
            if edge[1] == second:
                edge[1] = first
            if edge[0] != edge[1]:
                new.append((edge[0], edge[1]))
        edge_list = new

    return len(edge_list)

def genEdgeList():
    edges = []
    f = open('kargerMinCut.txt')
    for line in f:
        l = line.split('\t')
        l.remove('\n')
        l = [int(x) for x in l]
        first = l.pop(0)
        while l:
            n = l.pop()
            if n > first:
                edges.append((first, n))
    return edges

edges = genEdgeList()

best = 10000
for a in range(20**3):
    random.shuffle(edges)
    c = contract(edges, 200)
    best = min(best, c)
    print best

print best
