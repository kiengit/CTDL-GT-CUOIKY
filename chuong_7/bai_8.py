class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)

    # Hàm đệ quy để kiểm tra đường đi từ đỉnh u đến đỉnh v
    def is_reachable_dfs(self, u, v, visited):
        visited[u] = True
        if u == v:
            return True
        for i in self.adj[u]:
            if not visited[i]:
                if self.is_reachable_dfs(i, v, visited):
                    return True
        return False

    # Phương thức chính để kiểm tra đường đi từ đỉnh v1 đến đỉnh v2
    def DuongDi(self, v1, v2):
        visited = [False] * self.V
        return self.is_reachable_dfs(v1, v2, visited)

# Ví dụ sử dụng
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print(g.DuongDi(1, 3))  # Output: True
print(g.DuongDi(3, 1))  # Output: False
