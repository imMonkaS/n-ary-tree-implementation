import matplotlib.pyplot as plt
import networkx as nx

from typing import Tuple, Dict, List, Union, Optional

import time

SOURCES_PATH = 'app/sources/'


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

    pos = nx.drawing.nx_agraph.graphviz_layout(graph, prog='dot')
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
