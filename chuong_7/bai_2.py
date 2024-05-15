class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    # Thêm cạnh vào đồ thị vô hướng
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    # DFS để duyệt đồ thị
    def DFS(self, v, visited):
        visited[v] = True
        for i in self.adj[v]:
            if not visited[i]:
                self.DFS(i, visited)

    # Tính số thành phần liên thông
    def SoThanhPhan(self):
        visited = [False] * self.V
        count = 0
        # Duyệt qua tất cả các đỉnh
        for i in range(self.V):
            if not visited[i]:
                # Nếu đỉnh chưa được duyệt, tăng số thành phần lên 1 và thực hiện DFS từ đỉnh này
                count += 1
                self.DFS(i, visited)
        return count

# Ví dụ sử dụng
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(3, 4)

print("Số thành phần liên thông của đồ thị:", g.SoThanhPhan())
