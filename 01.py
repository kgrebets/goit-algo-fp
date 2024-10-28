class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def show_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head

        middle = self.get_middle(self.head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort_recursive(self.head)
        right = self._merge_sort_recursive(next_to_middle)

        self.head = self.merge_sorted_lists(left, right)

    def _merge_sort_recursive(self, node):
        if node is None or node.next is None:
            return node

        middle = self.get_middle(node)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort_recursive(node)
        right = self._merge_sort_recursive(next_to_middle)

        return self.merge_sorted_lists(left, right)

    def get_middle(self, head):
        if head is None:
            return head
        a = head
        b = head
        while b.next and b.next.next:
            a = a.next
            b = b.next.next
        return a

    @staticmethod
    def merge_sorted_lists(l1, l2):
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next


list = LinkedList()
list.append(3)
list.append(1)
list.append(4)
list.append(2)

print("Оригінальний список:")
list.show_list()

list.reverse()
print("\nРеверсований список:")
list.show_list()

list.merge_sort()
print("\nВідсортований список:")
list.show_list()

list_a = LinkedList()
list_a.append(1)
list_a.append(3)
list_a.append(5)

list_b = LinkedList()
list_b.append(2)
list_b.append(4)
list_b.append(6)

merged_list = LinkedList()
merged_list.head = LinkedList.merge_sorted_lists(list_a.head, list_b.head)
print("\nОб'єднаний відсортований список:")
merged_list.show_list()
