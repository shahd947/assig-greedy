from queue import PriorityQueue

def greedy_best_first_search(graph, start, goal, heuristic):
    open_list = PriorityQueue()
    open_list.put((heuristic[start], start))
    
    visited = set()
    
    path = []

    while not open_list.empty():
        _, current = open_list.get()
        path.append(current)
        
        if current == goal:
            return path
        
        visited.add(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                open_list.put((heuristic[neighbor], neighbor))

    return "Goal not reachable"

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 5,
    'F': 2,
    'G': 1,
    'H': 0  
}

start_node = 'A'
goal_node = 'H'
path = greedy_best_first_search(graph, start_node, goal_node, heuristic)

print("Path to goal:", path)