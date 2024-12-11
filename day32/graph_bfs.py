def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    
    while queue:
        node = queue.pop(0)
        print(node, end="")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
graph = {
    0: [1,2],
    1: [0,2,3],
    2: [0,1,4],
    3: [1,4],
    4: [2,3]
}

bfs(graph, 0)