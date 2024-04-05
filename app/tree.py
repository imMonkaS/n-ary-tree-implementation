import random
from typing import List


class Node:
    """
    Класс узла.
    У каждого узла свой Ид для возможности уникальной идентификации.
    """
    def __init__(self, value, _id):
        self.value = value
        self.id = _id
        # self.first_child = None
        self.siblings = []


class Tree:
    """
    Класс n-арного дерева
    """
    def __init__(self, _arity: int = 4):
        self.root = None
        self.arity = _arity
        self.nodes_amount = 0

    def _insert_node(self, value, node: Node):
        """
        Вставка узла. Используется вставка через случайный элемент, чтобы создаваемые рандомно деревья
        не были сбалансированными

        Args:
            value: то что лежит в узле
            node: узел
        """
        if node is None:
            self.nodes_amount += 1
            return Node(value, self.nodes_amount)

        if len(node.siblings) == 0:
            node.siblings.append(self._insert_node(value, None))
        else:
            if random.randint(0, 1) and self.arity > len(node.siblings):
                node.siblings.append(self._insert_node(value, None))
            else:
                child = random.randint(0, len(node.siblings) - 1)
                node.siblings[child] = self._insert_node(value, node.siblings[child])

        return node

    def insert(self, value):
        self.root = self._insert_node(value, self.root)

    def print_tree(self, node, indent=""):
        """
        Вывод в консоль
        """
        if node is not None:
            print(indent + str(node.value))
            for node in node.siblings:
                self.print_tree(node, indent + "  ")

    def print_tree_ids(self, node, indent=""):
        if node is not None:
            print(indent + str(node.id))
            for node in node.siblings:
                self.print_tree(node, indent + "  ")

    def print_tree_ids_to_file(self, node, output_file: str, indent=""):
        if node is not None:
            with open(output_file, 'a') as f:
                f.write(indent + str(node.id) + '\n')
            for node in node.siblings:
                self.print_tree(node, indent + "  ")

    def random_insertion(self, start: int, end: int, amount: int):
        """
        Вставка amount кол-ва узлов
        Args:
            start: нижний диапазон случ. знач.
            end: верхний диапазон случ. знач.
            amount: кол-во узлов, которые будут вставлены
        """
        values = [random.randint(start, end) for _ in range(amount)]
        for value in values:
            self.insert(value)

    def print_full_tree(self):
        self.print_tree(self.root)

    def _export_tree(self, node):
        if node is None:
            return ""
        result = ''
        if node.left or node.right:
            result += f"{node.id}: ["
            if node.left:
                result += f"({node.left.id}, {node.left.value})"
            if node.right and node.left:
                result += ", "
            if node.right:
                result += f"({node.right.id}, {node.right.value})"
            result += "],\n"
        result += self._export_tree(node.left)
        result += self._export_tree(node.right)
        return result

    def export_tree_to_file(self, filename):
        """
        Экспортировать дерево в файл для возможности его отрисовки
        и повторной работы.
        Args:
            filename: путь до файла, который будет создан
        """
        with open(filename, 'w') as f:
            f.write('{\n' + f"'root_value': {self.root.value},\n" + self._export_tree(self.root) + '}')

    def read_tree_from_dict(self, tree_dict):
        """
        Считать дерево из словаря (есть отдельная функция для преобразования файла в словарь.

        Args:
            tree_dict: словарь с деревом в формате:
                        'root_value': *val*
                        id_int: [(id_children_int, val_children)]
        """

        nodes = {1: Node(tree_dict['root_value'], 1)}

        for node_id, children in list(tree_dict.items())[1:]:
            node = nodes[node_id]
            if children:
                left_child, right_child = children[0], children[1] if len(children) > 1 else None
                if left_child:
                    left_id, left_value = left_child
                    if left_id not in nodes:
                        nodes[left_id] = Node(left_value, left_id)
                    node.left = nodes[left_id]
                if right_child:
                    right_id, right_value = right_child
                    if right_id not in nodes:
                        nodes[right_id] = Node(right_value, right_id)
                    node.right = nodes[right_id]
        self.root = nodes[1]
