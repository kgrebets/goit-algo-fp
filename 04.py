from task_04_example import Node, draw_tree

class BinaryHeap:
    def __init__(self):
        self.root = None
        self.nodes = []

    def insert(self, key):
        new_node = Node(key)
        self.nodes.append(new_node)
        if not self.root:
            self.root = new_node
        else:
            self._insert_into_heap(self.root, new_node)

    def _insert_into_heap(self, current, new_node):
        if current.left is None:
            current.left = new_node
        elif current.right is None:
            current.right = new_node
        else:
            if len(self.nodes) % 2 == 0:
                self._insert_into_heap(current.left, new_node)
            else:
                self._insert_into_heap(current.right, new_node)
        
        self._up_heap(new_node)

    def _up_heap(self, node):
        if node == self.root:
            return
        parent = self._find_parent(node)
        if parent and parent.val > node.val:   # Обмін значеннями         
            parent.val, node.val = node.val, parent.val
            self._up_heap(parent)

    def _find_parent(self, node):
        for n in self.nodes:
            if n.left == node or n.right == node:
                return n
        return None


heap = BinaryHeap()
heap.insert(3)
heap.insert(1)
heap.insert(7)
heap.insert(6)
heap.insert(5)
heap.insert(8)
heap.insert(4)

draw_tree(heap.root)
