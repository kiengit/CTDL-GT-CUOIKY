class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    # Thêm cạnh vào đồ thị vô hướng
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    # Kiểm tra xem một đỉnh có tồn tại trong đồ thị hay không
    def ChuaDinh(self, v):
        return v in range(self.V)

# Ví dụ sử dụng
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

print(g.ChuaDinh(2))  # Output: True
print(g.ChuaDinh(5))  # Output: False
