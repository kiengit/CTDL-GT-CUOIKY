class DiGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    # Thêm cung vào đồ thị có hướng
    def add_edge(self, u, v):
        self.adj[u].append(v)

    # Tính số cung đi ra từ đỉnh v
    def SoCungRa(self, v):
        count = 0
        for j in self.adj[v]:
            count += 1
        return count

# Ví dụ sử dụng
g = DiGraph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 4)

print(g.SoCungRa(1))  # Output: 2
print(g.SoCungRa(2))  # Output: 1
print(g.SoCungRa(4))  # Output: 0
