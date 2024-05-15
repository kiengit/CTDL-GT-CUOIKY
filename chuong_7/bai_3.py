class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    # Thêm cạnh vào đồ thị vô hướng
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    # Kiểm tra xem đồ thị có chu trình không
    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True
        # Duyệt qua tất cả các đỉnh kề của đỉnh hiện tại
        for i in self.adj[v]:
            # Nếu đỉnh kề chưa được duyệt, tiến hành duyệt đệ quy
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            # Nếu đỉnh kề đã được duyệt trước đó và không phải là đỉnh cha của đỉnh hiện tại, có chu trình
            elif parent != i:
                return True
        return False

    # Phương thức kiểm tra có chu trình trong đồ thị hay không
    def ChuTrinh(self):
        visited = [False] * self.V
        # Duyệt qua tất cả các đỉnh của đồ thị
        for i in range(self.V):
            if not visited[i]:
                # Nếu đỉnh chưa được duyệt, kiểm tra xem từ đỉnh này có chu trình không
                if self.is_cyclic_util(i, visited, -1):
                    return True
        return False

# Ví dụ sử dụng
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)

if g.ChuTrinh():
    print("Đồ thị có chu trình")
else:
    print("Đồ thị không có chu trình")
