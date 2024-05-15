class DiGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    # Thêm cung vào đồ thị có hướng
    def add_edge(self, u, v):
        self.adj[u].append(v)

    # Tính số cung đi vào đỉnh v
    def SoCungVao(self, v):
        count = 0
        for i in range(self.V):
            for j in self.adj[i]:
                if j == v:
                    count += 1
        return count

# Ví dụ sử dụng
g = DiGraph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 4)

print(g.SoCungVao(1))  # Output: 1
print(g.SoCungVao(3))  # Output: 1
print(g.SoCungVao(4))  # Output: 1
