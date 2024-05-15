class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    # Thêm cạnh vào đồ thị vô hướng
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    # Tính bậc của đỉnh v
    def BacDinh(self, v):
        return len(self.adj[v])

# Ví dụ sử dụng
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 4)

print(g.BacDinh(1))  # Output: 3
print(g.BacDinh(4))  # Output: 1
