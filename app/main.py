from app.tree import Tree
from tests import *

from utils import SOURCES_PATH, dict_from_file, draw_tree


def main():
    # tree = Tree()
    # # tree.random_insertion(0, 100, 20)
    #
    # # tree.print_full_tree()
    # # tree.export_tree_to_file(SOURCES_PATH + 'tree.txt')
    # # print(tree.root)
    # tree.read_tree_from_dict(dict_from_file(SOURCES_PATH + 'tree.txt'))
    # tree.print_full_tree()
    # draw_tree(
    #     dict_from_file(SOURCES_PATH + 'tree.txt'),
    #     make_image=SOURCES_PATH + 'tree.png'
    # )
    tree = Tree(5)
    # tree.random_insertion(0, 100, 100)
    # tree.export_tree_to_file(SOURCES_PATH + 'tree5_100.txt')
    tree.read_tree_from_dict(dict_from_file(SOURCES_PATH + 'tree5_100.txt'))
    draw_tree(
        dict_from_file(SOURCES_PATH + 'tree5_100.txt'),
        make_image=SOURCES_PATH + 'tree5_100.png',
        fig_size=(20, 15)
    )
    tree.print_nodes_per_level()
    tree.print_nodes_per_level_to_file(SOURCES_PATH + 'tree5_100_output.txt')


    # tree2


if __name__ == '__main__':
    main()
