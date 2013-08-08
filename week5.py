
# G is a list of tuples with (node, dist)
def Dijkstra(G, source):
    dist = {}
    prev = {}
    
    for node in range(len(G)):
        dist[node] = float('inf')
        prev[node] = 0

    dist[source] = 0
    Q = range(1, len(G))

    while Q:
        best = Q[0]
        for v in Q:
            if dist[best] > dist[v]:
                best = v
        # vertex in Q with smallest distance

        Q.remove(best)

        if dist[best] == float('inf'):
            break

        for (neigh, dist_to_neigh) in G[best]:
            alt = dist[best] + dist_to_neigh
            if alt < dist[neigh]:
                dist[neigh] = alt
                prev[neigh] = best
    return dist

G = []
G.append([])
for line in open('dijkstraData.txt'):
    l = line.split()
    G.append([])
    node = int(l.pop(0))
    for n in l:
        [neigh, dist] = [int(x) for x in n.split(',')]
        G[node].append((neigh, dist))

dists = Dijkstra(G, 1)

print [dists[x] for x in (7,37,59,82,99,115,133,165,188,197)]
