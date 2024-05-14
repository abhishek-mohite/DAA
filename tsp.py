import numpy as np
import heapq

def tsp_branch_and_bound(graph):
    def lower_bound(node, visited, bound):
        for i in range(len(graph)):
            if i not in visited:
                min_edge = float('inf')
                for j in range(len(graph)):
                    if j != i and j not in visited:
                        min_edge = min(min_edge, graph[i][j])
                bound += min_edge

        return bound

    def tsp_recursive(node, visited, bound, path):
        if len(visited) == len(graph):
            return bound + graph[node][0], path + [0]

        min_cost = float('inf')
        min_path = []

        for i in range(len(graph)):
            if i not in visited:
                new_bound = bound - graph[node][0] + graph[node][i]
                if new_bound < min_cost:
                    new_visited = visited + [i]
                    cost, new_path = tsp_recursive(i, new_visited, new_bound, path + [i])
                    if cost < min_cost:
                        min_cost = cost
                        min_path = new_path

        return min_cost, min_path

    start_node = 0
    initial_bound = lower_bound(start_node, [start_node], 0)
    min_cost, min_path = tsp_recursive(start_node, [start_node], initial_bound, [start_node])

    return min_cost, min_path

# Example usage:
graph = np.array([
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
])

min_cost, min_path = tsp_branch_and_bound(graph)
print("Minimum cost:", min_cost)
print("Optimal path:", min_path)
