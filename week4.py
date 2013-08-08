# INITIALIZE ADJACENCY LISTS AND OVERHEAD MAPS
G = {}
G_rev = {}
N = 875714
leader = [0] * (N + 1)
finish = [0] * (N + 1)
seen = [False] * (N + 1)
for i in xrange(1, N + 1):
    G[i] = []
    G_rev[i] = []

# READ THE FILE
f = open('SCC.txt')
for line in f:
    first, second = [int(x) for x in line.split()]
    G[first].append(second)
    G_rev[second].append(first)

def non_recurs_dfs(G, i):
    global time, s
    stack = [i]
    seen[i] = True
    leader[i] = s
    while stack:
        current = stack[-1]
        done = True
        for neigh in G[current]:
            if not seen[neigh]:
                done = False
                seen[neigh] = True
                leader[neigh] = s
                stack.append(neigh)
        if done:
            stack.pop()
            time += 1
            finish[current] = time

def dfs_loop(G):
    global time, s
    time = 0 # NUMBER OF NODES PROCESSED
    s = N # CURRENT SOURCE
    for i in xrange(N, 0, -1):
        if not seen[i]:
            s = i
            non_recurs_dfs(G, i)

# RUN DFS LOOP ON THE REVERSE GRAPH
dfs_loop(G_rev)

# CREATE NEW GRAPH
newGraph={}
for i in range(1, N + 1):
    temp = []
    for x in G[i]:
        temp.append(finish[x])
    newGraph[finish[i]] = temp

# REINITIALIZE OVERHEAD
leader = [0] * (N + 1)
finish = [0] * (N + 1)
seen = [False] * (N + 1)

#RUN DFS LOOP ON NEW GRAPH
dfs_loop(newGraph)

# COLLECT LEADERS FOR SCC
leader_counts = [0] * (N + 1)
for val in leader[1:]:
    leader_counts[val] = leader_counts[val] + 1

print sorted(leader_count, reverse=True)[0:5]
