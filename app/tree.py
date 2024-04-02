import random


class Node:
    def __init__(self, value, _id):
        self.value = value
        self.id = _id
        self.children = []


class Tree:
    def __init__(self):
        self.root = None
        self.nodes_amount = 0

    # def insert_node(self, value, node: Node):
    #     if node is None:
    #         self.nodes_amount += 1
    #         return Node(value, self.nodes_amount)
    #
    #     if random.randint(0, 1):
    #         node.children.append(self.insert_node(value, node.left))
    #     else:
    #         node.right = self.insert_node(value, node.right)
    #     return node

    # def insert(self, value):
    #     self.root = self.insert_node(value, self.root)

    def print_tree(self, node, indent=""):
        if node is not None:
            print(indent + str(node.value))
            self.print_tree(node.left, indent + "  ")
            self.print_tree(node.right, indent + "  ")

    def print_tree_ids(self, node, indent=""):
        if node is not None:
            print(indent + str(node.id))
            self.print_tree_ids(node.left, indent + "  ")
            self.print_tree_ids(node.right, indent + "  ")

    def print_tree_ids_to_file(self, node, output_file: str, indent=""):
        if node is not None:
            with open(output_file, 'a') as f:
                f.write(indent + str(node.id) + '\n')
            self.print_tree_ids_to_file(node.left, output_file, indent + "  ")
            self.print_tree_ids_to_file(node.right, output_file, indent + "  ")

    # def random_insertion(self, start: int, end: int, amount: int):
    #     values = [random.randint(start, end) for _ in range(amount)]
    #     for value in values:
    #         self.insert(value)

    def print_full_tree(self):
        self.print_tree(self.root)

    def export_tree(self, node):
        if node is None:
            return ""
        result = f"{node.value}: ["
        if node.left:
            result += f"{node.left.value}, "
        if node.right:
            result += f"{node.right.value}"
        result += "], "
        result += self.export_tree(node.left)
        result += self.export_tree(node.right)
        return result

    def export_tree_with_ids(self, node):
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
        result += self.export_tree_with_ids(node.left)
        result += self.export_tree_with_ids(node.right)
        return result

    def export_tree_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.export_tree(self.root))

    def export_tree_with_ids_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write('{\n' + f"'root_value': {self.root.value},\n" + self.export_tree_with_ids(self.root) + '}')

    def read_tree_from_dict(self, tree_dict):
        nodes = {}
        nodes[1] = Node(tree_dict['root_value'], 1)

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
