# Напишите класс BinaryTree, который реализует основные
# операции бинарного дерева: вставка (insert) и поиск (search)
from collections import deque

class Node:
    def __init__(self, value): # Конструктор класса. Он принимает значение value и создает новый узел.
        self.value = value     # Сохраняет значение в узле.
        self.left = None # Инициализирует левый дочерний узел как None (пустой)
        self.right = None # Инициализирует правый дочерний узел как None (пустой).
        self.height = 1  # Высота узла (используется для AVL-дерева)


class BinaryTree:

    def __init__(self): #Конструктор класса.
        self.root = None # Инициализирует корень дерева как None (пустое дерево).

    def insert(self, value): # Вставляет новый узел со значением value в дерево
        if self.root is None: # Если дерево пустое (нет корня), создает новый узел и делает его корнем.
            self.root = Node(value)
        else: # Если дерево не пустое, вызывает вспомогательный рекурсивный метод _insert для вставки узла, начиная с корня
            self._insert(self.root, value)


    def _insert(self, current_node, value): # Вспомогательный рекурсивный метод для вставки узла. Важно: Это логика бинарного дерева поиска.
        if value < current_node.value: #  Если значение меньше, чем значение текущего узла:
            if current_node.left is None: # : Если у текущего узла нет левого дочернего узла, создает новый узел и делает его левым дочерним узлом.
                current_node.left = Node(value)
            else: # Если у текущего узла уже есть левый дочерний узел, рекурсивно вызывает _insert для вставки в левое поддерево.
                self._insert(current_node.left, value)
        else: # Если значение больше или равно (обычно больше, чтобы избежать дубликатов в левом поддереве) значению текущего узла:
            if current_node.right is None: # Если у текущего узла нет правого дочернего узла, создает новый узел и делает его правым дочерним узлом.
                current_node.right = Node(value)
            else: #  Если у текущего узла уже есть правый дочерний узел, рекурсивно вызывает _insert для вставки в правое поддерево.
                self._insert(current_node.right, value)

    def bfs(self):
        if self.root is None:
            return # Если дерево пустое, ничего не делаем

        queue = deque([self.root]) # Используем очередь для BFS

        while queue:
            node = queue.popleft()          # Извлекаем узел из начала очереди
            print(node.value, end = " ")    # Выводим значение узла

            if node.left:
                queue.append(node.left)     # Добавляем левого потомка в очередь
            if node .right:
                queue.append(node.right)    # Добавляем правого потомка в очередь

# Напишите три функции для обхода бинарного дерева в глубину
# (Depth-First Search, DFS): прямой обход (preorder), симметричный  обход (inorder) и обратный обход (postorder)
# прямой обход (preorder)
    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
# симметричный  обход (inorder)
    def inorder(self, node):  # Выполняет обход дерева в порядке “inorder” (левый, корень, правый).
        # Этот обход возвращает значения в отсортированном порядке для бинарного дерева поиска.
        if node:  # Проверяет, не является ли текущий узел None. Если узел существует:
            self.inorder(node.left)  # Рекурсивно вызывает inorder для левого поддерева.
            print(node.value, end=' ')  # выводит значение текущего узла. end=' ' добавляет
            # пробел после значения, чтобы значения выводились в одной строке.
            self.inorder(node.right)  # Рекурсивно вызывает inorder для правого поддерева.
# обратный обход (postorder)
    def postorder(self, node):#-------------симметричный обход в обратном порядке
        if node :
            self.postorder(node.left) # проходит левое поддерево
            self.postorder(node.right) # проходит правое поддерево
            print(node.value, end=" ") # проходит сам узел

# Напишите класс AVLTree, который наследует класс BinaryTree
#  и добавляет операции балансировки при вставке элементов.
# Реализуйте методы для поворотов (left_rotate, right_rotate)
#  и балансировки (rebalance)
class AVLTree(BinaryTree):# cоздаем дерево AVL
    def __init__(self):
        super().__init__()

    def get_height(self, node):
        if not node:
            return 0
        return node.height # Возвращает высоту узла

    def get_balance(self, node): # Возвращает фактор балансировки узла
        if node is None: # если у нас нет корня
            return 0 # возвращаем 0
        return self.get_height(node.right) - self.get_height(node.left) # возвращаем разницу высот между правым и левым


    def left_rotate(self, m): # меняем местами. Выполняем левый поворот
        y = m.right
        T2 = y.left
        y.left = m
        m.right = T2
        m.height = 1 + max(self.get_height(m.left), self.get_height(m.right)) # меняем высоты
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right)) # меняем высоты
        return y

    def right_rotate(self, m):
        y = m.left
        T3 = y.right
        y.right = m
        m.left = T3
        m.height = 1 + max(self.get_height(m.left), self.get_height(m.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def _rebalance(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance_factor = self.get_balance(node)

       # Левый дисбаланс
        if balance_factor < -1 and self.get_balance(node.left) <= 0:
                return self.right_rotate(node)  # Left Left Case

        if balance_factor > 1 and self.get_balance(node.left) > 0:
            node.left = self.left_rotate(node.left)  # Left Right Case
            return self.right_rotate(node)

        # Правый дисбаланс
        if balance_factor > 1 and self.get_balance(node.right) >= 0:
            return self.left_rotate(node)  # Right Right Case

        if balance_factor > 1 and self.get_balance(node.right) < 0:
            node.right = self.right_rotate(node.right)  # Right Left Case
            return self.left_rotate(node)

        return node  # Поддерево сбалансировано

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        return self._rebalance(node)


# Пример использования
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("Обход по порядку:")
print('bfs', tree.bfs())

print('прямой обход (preorder)', tree.preorder(tree.root))
print(' ')
print('симметричный  обход (inorder)', tree.inorder(tree.root))
print(' ')
print('обратный обход (postorder)', tree.postorder(tree.root))

# Пример использования:
avl_tree = AVLTree()
avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(30)
avl_tree.insert(40)
avl_tree.insert(50)
avl_tree.insert(25)

print("Inorder обход AVL-дерева:")
avl_tree.inorder(avl_tree.root)
print()

print("Высота дерева:", avl_tree.get_height(avl_tree.root))