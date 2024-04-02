import matplotlib.pyplot as plt
import networkx as nx

from typing import Tuple, Dict, List, Union, Optional

import time

SOURCES_PATH = 'app/sources/'


def adjust_positions(pos, graph):
    for node in graph.nodes():
        if len(list(graph.successors(node))) == 1:  # if the node has only one child
            child = list(graph.successors(node))[0]
            pos[child] = (pos[node][0] + (0.1 if child < node else -0.1), pos[child][1])
    return pos


def draw_tree(
        tree: Dict[int, List[Tuple[int, Union[int, str]]]],
        show_tree: bool = False,
        fig_size: Tuple[int, int] = (12, 12),
        show_ids: bool = False,
        make_image: Optional[str] = None,
        color: str = 'cyan'
):
    graph = nx.DiGraph()

    id_to_value = {}
    id_to_value[1] = f'1: {tree["root_value"]}' if show_ids else tree["root_value"]
    for node_id, children in list(tree.items())[1:]:
        for child in children:
            if child[0] not in id_to_value.keys():
                id_to_value[child[0]] = f'{child[0]}: {child[1]}' if show_ids else child[1]
            graph.add_edge(node_id, child[0])

    pos = adjust_positions(nx.drawing.nx_agraph.graphviz_layout(graph, prog='dot'), graph)
    # pos = nx.drawing.nx_agraph.graphviz_layout(graph, prog='dot')
    plt.figure(figsize=fig_size)
    nx.draw(graph, pos, with_labels=True, node_color=color, arrows=False, labels=id_to_value)
    if make_image is not None:
        plt.savefig(make_image)
    if show_tree:
        plt.show()


def dict_from_file(filename: str) -> Dict:
    try:
        with open(filename, 'r') as f:
            try:
                tree_dict = eval(f.read())
            except Exception as e:
                raise e
    except Exception as e:
        raise e
    return tree_dict


# def randomly_generate_tree_and_subtree_files(
#         tree_nodes_amount: int,
#         subtree_nodes_amount: int,
#         tree_output_name: str,
#         subtree_output_name: str,
#         tree_image_name: str = None,
#         subtree_image_name: str = None,
#         start: int = 0,
#         end: int = 100,
#         show_ids: bool = True
# ):
#     bt = BinaryTree()
#     subtree = BinaryTree()
#
#     bt.random_insertion(start, end, tree_nodes_amount)
#     subtree.random_insertion(start, end, subtree_nodes_amount)
#
#     bt.export_tree_with_ids_to_file(tree_output_name)
#     subtree.export_tree_with_ids_to_file(subtree_output_name)
#
#     if tree_image_name is not None:
#         draw_tree(
#             dict_from_file(tree_output_name),
#             fig_size=(10, 10),
#             make_image=tree_image_name,
#             show_ids=show_ids
#         )
#     if subtree_image_name is not None:
#         draw_tree(
#             dict_from_file(subtree_output_name),
#             fig_size=(8, 8),
#             make_image=subtree_image_name,
#             show_ids=show_ids
#         )
