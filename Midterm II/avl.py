# Espacio para inciso 2.1
class AVLNode:

    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

    def __repr__(self):
        return f"({self.data})"


class AVLTree:

    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left_child) - self.get_height(node.right_child) if node else 0

    def right_rotate(self, y):
        x = y.left_child
        T2 = x.right_child

        x.right_child = y
        y.left_child = T2

        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))
        x.height = 1 + max(self.get_height(x.left_child), self.get_height(x.right_child))

        return x

    def left_rotate(self, x):
        y = x.right_child
        T2 = y.left_child

        y.left_child = x
        x.right_child = T2

        x.height = 1 + max(self.get_height(x.left_child), self.get_height(x.right_child))
        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))

        return y

    def insert(self, value: int):
        self.root = self._insert(self.root, value)

    def _insert(self, node: AVLNode, value: int) -> AVLNode:
        if not node:
            return AVLNode(value)

        if value < node.data:
            node.left_child = self._insert(node.left_child, value)
        elif value > node.data:
            node.right_child = self._insert(node.right_child, value)
        else:
            print("Value already exists in tree...")
            return node

        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        balance = self.get_balance(node)

        # Left Left
        if balance > 1 and value < node.left_child.data:
            return self.right_rotate(node)

        # Right Right
        if balance < -1 and value > node.right_child.data:
            return self.left_rotate(node)

        # Left Right
        if balance > 1 and value > node.left_child.data:
            node.left_child = self.left_rotate(node.left_child)
            return self.right_rotate(node)

        # Right Left
        if balance < -1 and value < node.right_child.data:
            node.right_child = self.right_rotate(node.right_child)
            return self.left_rotate(node)

        return node

    def search(self, key: int) -> bool:
        return self._search(self.root, key)

    def _search(self, node: AVLNode, key: int) -> bool:
        if node is None:
            return False
        if key == node.data:
            return True
        elif key < node.data:
            return self._search(node.left_child, key)
        else:
            return self._search(node.right_child, key)

    def delete(self, value: int):
        self.root = self._delete(self.root, value)

    def _delete(self, node: AVLNode, value: int) -> AVLNode:
        if not node:
            return node

        if value < node.data:
            node.left_child = self._delete(node.left_child, value)
        elif value > node.data:
            node.right_child = self._delete(node.right_child, value)
        else:
            if not node.left_child:
                return node.right_child
            elif not node.right_child:
                return node.left_child

            temp = self._get_min_value_node(node.right_child)
            node.data = temp.data
            node.right_child = self._delete(node.right_child, temp.data)

        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        balance = self.get_balance(node)

        # Balance tree
        if balance > 1 and self.get_balance(node.left_child) >= 0:
            return self.right_rotate(node)

        if balance > 1 and self.get_balance(node.left_child) < 0:
            node.left_child = self.left_rotate(node.left_child)
            return self.right_rotate(node)

        if balance < -1 and self.get_balance(node.right_child) <= 0:
            return self.left_rotate(node)

        if balance < -1 and self.get_balance(node.right_child) > 0:
            node.right_child = self.right_rotate(node.right_child)
            return self.left_rotate(node)

        return node

    def _get_min_value_node(self, node: AVLNode):
        current = node
        while current.left_child:
            current = current.left_child
        return current

    def print_pretty(self):
        if self.root:
            lines, *_ = self._build_tree_string(self.root)
            print("\n" + "\n".join(line.rstrip() for line in lines))
        else:
            print("\nEmpty tree...")

    def _build_tree_string(self, node: AVLNode):
        if node.right_child is None and node.left_child is None:
            line = str(node.data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right_child is None:
            lines, n, p, x = self._build_tree_string(node.left_child)
            s = str(node.data)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if node.left_child is None:
            lines, n, p, x = self._build_tree_string(node.right_child)
            s = str(node.data)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._build_tree_string(node.left_child)
        right, m, q, y = self._build_tree_string(node.right_child)
        s = str(node.data)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


