import heapq

def a_star(start, goal, graph, heuristic):

    PQ = [(heuristic[start], 0, start, [start])]
    Expanded = set()  

    while PQ:  
        f, g, node, path = heapq.heappop(PQ)

        if node == goal:
            return path, g

        if node not in Expanded:
            Expanded.add(node)

            for v, cost in graph[node].items():
                g_v = g + cost
                h_v = heuristic[v]
                f_v = g_v + h_v
                heapq.heappush(PQ, (f_v, g_v, v, path + [v]))

    return None, float("inf")

graph1 = {
    'S': {'A': 1, 'B': 5},
    'A': {'B': 2, 'C': 3, 'D': 4},
    'B': {'D': 3, 'E': 3},
    'C': {'B': 4, 'F': 5},
    'D': {'F': 6},
    'E': {'D': 6, 'G': 10},
    'F': {'G': 5},
    'G': {}
}

graph1_h = {'S':9,'A':8,'B':6,'C':7,'D':4,'E':6,'F':3,'G':0}

path, cost = a_star('S', 'G', graph1, graph1_h)
print("Path:", path)
print("Cost:", cost)


#output(path:S-A-C-F-G, cost:14)