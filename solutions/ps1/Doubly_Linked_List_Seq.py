class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)
        node.next = self.head
        if self.head:
            self.head.prev = node
        else:   # means it's empty before
            self.tail = node
        self.head = node

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        else:   # means it's empty before
            self.head = node
        self.tail = node

    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        if self.head:
            x = self.head.item
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        if self.tail:
            x = self.tail.item
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        L2.head = x1
        L2.tail = x2
        if x1.prev:
            x1.prev.next = x2.next
            x1.prev = None
        if x2.next:
            x2.next.prev = x1.prev
            x2.next = None
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        # splice L2 after x
        if L2.head: # means it's not empty
            if x.next:
                x.next.prev = L2.tail
                L2.tail.next = x.next
            else:
                self.tail = L2.tail
            x.next = L2.head
            L2.head.prev = x
            L2.head = None
            L2.tail = None
