from app.tree import Tree
from tests import *

# from utils import randomly_generate_tree_and_subtree_files


def main():
    tree = Tree()
    tree.random_insertion(0, 100, 100)

    tree.print_full_tree()
    print(tree.root)


if __name__ == '__main__':
    main()
