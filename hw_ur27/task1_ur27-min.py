"""
Розширити структуру, яку побудували на уроці, можливістю вставки дерева в наявне дерево та видалення піддерева з дерева, що існує.
"""

from hw_ur27.AVL_Node import AVL_Node

class AVLTree:
    def __init__(self): # Додавання дерева, коріння пусте
        self.root = None

    def insert(self, value): # Додавання листя
        self.root = self._insert(self.root, value)

    def _insert(self, current_node: AVL_Node, value):
        if not current_node: return AVL_Node(value)

        elif value <= current_node.value: # Якщо значення листка менше від кореня, то додаємо до лівої сторони
            if current_node.left_node is None:
                current_node.left_node = AVL_Node(value)
            else: # Якщо ліва сторона зайнята, через рекурсію додаємо листочок до гілки
                current_node.left_node = self._insert(current_node.left_node, value)

        elif value >= current_node.value: # Якщо значення листка більше від кореня, то додаємо до правої сторони
            if current_node.right_node is None:
                current_node.right_node = AVL_Node(value)
            else: # Якщо права сторона зайнята, через рекурсію додаємо листочок до гілки
                current_node.right_node = self._insert(current_node.right_node, value)

        current_node.height = 1 + max(self.height(current_node.left_node), self.height(current_node.right_node))
        balance = self.balance(current_node)

        if balance < -1 and value > current_node.right_node.value:
            return self.rotate_left(current_node)

        if balance > 1 and value < current_node.left_node.value:
            return  self.rotate_right(current_node)

        if balance > 1 and value > current_node.right_node.value:
            current_node.left_node = self.rotate_left(current_node.left_node)

        if balance < -1 and value < current_node.left_node.value:
            current_node.right_node = self.rotate_right(current_node.right_node)

        return current_node


    def rotate_right(self, root):
        root_left = root.left_node
        root_right = root.right_node

        root_left.right_node = root
        root.left_node = root_right

        root.height = 1 + max(self.height(root.left_node), self.height(root.right_node))
        root_left.height = 1 + max(self.height(root_left.left_node), self.height(root_left.right_node))

        return root_left


    def rotate_left(self, root):
        root_right = root.right_node
        root_left = root.left_node

        root_right.left_node = root
        root.right_node = root_left

        root.height = 1 + max(self.height(root.left_node), self.height(root.right_node))
        root_right.height = 1 + max(self.height(root_right.left_node), self.height(root_right.right_node))

        return root_right


    def del_subtree(self, search_value):
        self.root = self._del_subtree(self.root, search_value)

    def _del_subtree(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left_node = self._del_subtree(node.left_node, value)
        elif value > node.value:
            node.right_node = self._del_subtree(node.right_node, value)
        else:
            return None

        node.height = 1 + max(self.height(node.left_node), self.height(node.right_node))
        return self.balance(node)


    def insert_tree(self, subtree):
        def _insert_tree( root, sub_root):
            if sub_root:
                root = self._insert(root, sub_root.value)
                root = _insert_tree(root, sub_root.left_node)
                root = _insert_tree(root, sub_root.right_node)
            return root

        self.root = _insert_tree(self.root, subtree.root)



    @staticmethod
    def height(root: AVL_Node): # Повертає висоту дерева
        return root.height if root else 0

    def balance(self, root: AVL_Node):
        if root:
            left_height = self.height(root.left_node)
            right_height = self.height(root.right_node)
            return left_height - right_height
        else:
            return 0

    def display(self): # Відображення дерева
        lines, *_ = self.root.display_aux()
        for line in lines:
            print(line)


if __name__ == "__main__":
    tree = AVLTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(6)
    tree.insert(2)
    tree.insert(12)
    tree.insert(18)
    tree.insert(20)
    tree.insert(21)
    tree.insert(2)
    tree.insert(1)
    tree.insert(0)
    tree.insert(-1)
    tree.insert(-2)
    tree.insert(-3)
    tree.display()
    subtree = AVLTree()
    subtree.insert(4)
    subtree.insert(9)
    subtree.insert(3)
    subtree.display()
    tree.insert_tree(subtree)
    tree.display()