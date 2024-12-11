def DFS(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

graph = {
    "A": ["B",'E','F'],
    'B': ['A','C'],
    'C': ['B','D'],
    'D': ['C', 'E','G'],
    'E': ['A','D'],
    'F': ['A','G'],
    'G': ['D','F']
}

DFS(graph, 'A')