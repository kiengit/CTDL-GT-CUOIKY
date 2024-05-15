# sử dụng stack
class Node:
    def __init__(self, info):
        self.Info = info
        self.Next = None

class dslk:
    def __init__(self):
        self.Head = None

    def Them(self, info):
        new_node = Node(info)
        if self.Head is None:
            self.Head = new_node
        else:
            current = self.Head
            while current.Next is not None:
                current = current.Next
            current.Next = new_node

    def InNguoc(self):
        print("Danh sách liên kết in ngược không đệ qui:")
        stack = []
        current = self.Head
        while current is not None:
            stack.append(current.Info)
            current = current.Next
        while stack:
            print(stack.pop(), end=" ")
        print()

# Tạo danh sách liên kết
ds = dslk()
ds.Them(1)
ds.Them(2)
ds.Them(3)
ds.Them(4)

# In danh sách liên kết theo chiều ngược sử dụng stack
ds.InNguoc()

# sử dụng đệ qui
class Node:
    def __init__(self, info):
        self.Info = info
        self.Next = None

class dslk:
    def __init__(self):
        self.Head = None

    def Them(self, info):
        new_node = Node(info)
        if self.Head is None:
            self.Head = new_node
        else:
            current = self.Head
            while current.Next is not None:
                current = current.Next
            current.Next = new_node

    def InNguoc(self):
        def in_nguoc_recursive(node):
            if node is None:
                return
            in_nguoc_recursive(node.Next)
            print(node.Info, end=" ")

        print("Danh sách liên kết in ngược bằng đệ qui:")
        in_nguoc_recursive(self.Head)
        print()

# Tạo danh sách liên kết
ds = dslk()
ds.Them(1)
ds.Them(2)
ds.Them(3)
ds.Them(4)

# In danh sách liên kết theo chiều ngược sử dụng đệ qui
ds.InNguoc()
