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
        if parent and parent.val > node.val:  # Обмін значеннями         
            parent.val, node.val = node.val, parent.val
            self._up_heap(parent)

    def _find_parent(self, node):
        for n in self.nodes:
            if n.left == node or n.right == node:
                return n
        return None

# Початкові налаштування
INITIAL_COLOR = "#1296F0"
COLOR_DELTA = 30

def lighten_color(color, delta):
    # Перетворення шістнадцяткового кольору в RGB
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)

    # Збільшення яскравості
    r = min(255, r + delta)
    g = min(255, g + delta)
    b = min(255, b + delta)

    # Повернення нового шістнадцяткового кольору
    return f'#{r:02x}{g:02x}{b:02x}'

def dfs(tree):
    stack = [tree.root]
    colors = {}
    output = []  
    color = INITIAL_COLOR  
    
    while stack:
        current_node = stack.pop()
        if current_node is None:
            continue
        
        if current_node not in colors: 
            colors[current_node] = color
            
            output.append(current_node.val)
        
        color = lighten_color(color, COLOR_DELTA)  
        
        stack.append(current_node.right)
        stack.append(current_node.left)
    
    print("DFS Order:", " -> ".join(map(str, output)))  
    return colors

def bfs(tree):
    queue = [tree.root]
    colors = {}
    output = []  
    color = INITIAL_COLOR  
    
    while queue:
        current_node = queue.pop(0)
        if current_node is None:
            continue
        
        if current_node not in colors: 
            colors[current_node] = color
            
            output.append(current_node.val)
        
        color = lighten_color(color, COLOR_DELTA) 
        
        queue.append(current_node.left)
        queue.append(current_node.right)
    
    print("BFS Order:", " -> ".join(map(str, output))) 
    return colors

def visualize_tree_with_colors(tree, colors):
    for node, color in colors.items():
        node.color = color 
    
    draw_tree(tree.root) 

heap = BinaryHeap()
heap.insert(3)
heap.insert(1)
heap.insert(7)
heap.insert(6)
heap.insert(5)
heap.insert(8)
heap.insert(4)

dfs_colors = dfs(heap)
bfs_colors = bfs(heap)

visualize_tree_with_colors(heap, dfs_colors)  
visualize_tree_with_colors(heap, bfs_colors) 
