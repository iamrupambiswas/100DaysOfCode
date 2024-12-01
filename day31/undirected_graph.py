class UndirectedGraph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)
        
    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)
        self.display()
        
    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")
            
            
graph = UndirectedGraph()
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "C")
graph.add_edge("D", "C")
graph.add_edge("C", "E")
graph.add_edge("F", "C")
graph.add_edge("E", "D")
graph.add_edge("E", "F")

graph.display()

graph.remove_edge("E", "F")