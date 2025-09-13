import heapq

def ucs(start, goal, graph):
    PQ = [(0, start, [start])]
    Expanded = []

    step = 1
    while PQ:
        g, node, path = heapq.heappop(PQ)

        print(f"\nStep {step}: Expanding {node}")
        step += 1

        if node == goal:
            print("\nGoal reached!")
            print("Expanded order:", Expanded + [node])
            return path, g

        if node not in Expanded:
            Expanded.append(node)

            for v, cost in graph.get(node, {}).items():
                g_v = g + cost
                heapq.heappush(PQ, (g_v, v, path + [v]))

        frontier = [(n, g) for g, n, _ in PQ]
        print("Frontier:", frontier)
        print("Expanded so far:", Expanded)

    return None, float("inf")

graph2 = {
    'S': {'A': 3, 'B': 2},
    'A': {'C': 4, 'D': 1},
    'B': {'E': 3, 'F': 1},
    'E': {'H': 5},
    'F': {'I': 2, 'G': 3},
    'C': {}, 'D': {}, 'H': {}, 'I': {}, 'G': {}
}

path, cost = ucs('S', 'G', graph2)
print("\nFinal Path:", path)
print("Total Cost:", cost)
