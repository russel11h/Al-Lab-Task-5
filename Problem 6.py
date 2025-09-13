import heapq
graph2 = {
    'S': {'A': 3, 'B': 2},
    'A': {'C': 4, 'D': 1},
    'B': {'E': 3, 'F': 1},
    'E': {'H': 5},
    'F': {'I': 2, 'G': 3},
    'C': {}, 'D': {}, 'H': {}, 'I': {}, 'G': {}
}
heuristic2 = {
    'S': 13, 'A': 12, 'B': 4, 'C': 7, 'D': 3,
    'E': 8, 'F': 2, 'H': 4, 'I': 9, 'G': 0
}
def gbfs(start, goal, graph, heuristic):
    PQ = [(heuristic[start], start, [start])]
    Expanded = []

    step = 1
    while PQ:
        h, node, path = heapq.heappop(PQ)

        print(f"\nStep {step}: Expanding {node}")
        step += 1

        if node == goal:
            print("\n Goal reached!")
            print("Expanded order:", Expanded + [node])
            return path

        if node not in Expanded:
            Expanded.append(node)

            for v in graph.get(node, {}):
                heapq.heappush(PQ, (heuristic[v], v, path + [v]))

        frontier = [(n, heuristic[n]) for h, n, _ in PQ]
        print("Frontier (node,h):", frontier)
        print("Expanded so far:", Expanded)

    return None


path = gbfs('S', 'G', graph2, heuristic2)
print("\nFinal Path:", path)
