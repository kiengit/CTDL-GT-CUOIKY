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

    def DaoNguoc(self):
        print("Danh sách liên kết sau khi đảo ngược:")
        stack = []
        current = self.Head
        while current is not None:
            stack.append(current)
            current = current.Next

        new_head = None
        while stack:
            node = stack.pop()
            if new_head is None:
                new_head = node
                current = new_head
            else:
                current.Next = node
                current = current.Next
        current.Next = None
        self.Head = new_head

    def In(self):
        current = self.Head
        while current is not None:
            print(current.Info, end=" ")
            current = current.Next
        print()

# Tạo danh sách liên kết
ds = dslk()
ds.Them(1)
ds.Them(2)
ds.Them(3)
ds.Them(4)

# In danh sách liên kết trước khi đảo ngược
print("Danh sách liên kết trước khi đảo ngược:")
ds.In()

# Đảo ngược danh sách liên kết
ds.DaoNguoc()

# In danh sách liên kết sau khi đảo ngược
ds.In()
