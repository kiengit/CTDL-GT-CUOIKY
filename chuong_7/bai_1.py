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

    # Kiểm tra đồ thị liên thông
    def LienThong(self):
        visited = [False] * self.V
        # Tìm một nút mà DFS có thể truy cập được từ đó
        for i in range(self.V):
            if len(self.adj[i]) > 0:
                start_node = i
                break
        # Thực hiện DFS từ nút bắt đầu
        self.DFS(start_node, visited)
        # Nếu mọi nút trong đồ thị đều được duyệt, tức là đồ thị liên thông
        return all(visited)

# Ví dụ sử dụng
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(3, 4)

if g.LienThong():
    print("Đồ thị là đồ thị liên thông")
else:
    print("Đồ thị không phải là đồ thị liên thông")
