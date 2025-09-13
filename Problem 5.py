
import heapq
graph2 = {
    'S': {'A': 3, 'B': 2},
    'A': {'C': 4, 'D': 1},
    'B': {'E': 3, 'F': 1},
    'E': {'H': 5},
    'F': {'I': 2, 'G': 3},
    'C': {}, 'D': {}, 'H': {}, 'I': {}, 'G': {}
}

def a_star(start, goal, graph, heuristic):
    PQ = [(heuristic[start], 0, start, [start])]
    Expanded = []

    step = 1
    while PQ:
        f, g, node, path = heapq.heappop(PQ)

        print(f"\nStep {step}: Expanding {node}")
        step += 1

        if node == goal:
            print("\n Goal reached!")
            print("Expanded order:", Expanded + [node])
            return path, g

        if node not in Expanded:
            Expanded.append(node)

            for v, cost in graph.get(node, {}).items():
                g_v = g + cost
                h_v = heuristic[v]
                f_v = g_v + h_v
                heapq.heappush(PQ, (f_v, g_v, v, path + [v]))

        frontier = [(n, f, g, heuristic[n]) for f, g, n, _ in PQ]
        print("Frontier (node,f,g,h):", frontier)
        print("Expanded so far:", Expanded)

    return None, float("inf")


heuristic2 = {
    'S': 13, 'A': 12, 'B': 4, 'C': 7, 'D': 3,
    'E': 8, 'F': 2, 'H': 4, 'I': 9, 'G': 0
}

path, cost = a_star('S', 'G', graph2, heuristic2)
print("\nFinal Path:", path)
print("Total Cost:", cost)
