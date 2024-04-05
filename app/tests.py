import datetime
from typing import Tuple

from tree import Tree
import time
from utils import draw_tree, dict_from_file, SOURCES_PATH


def create_random_test_data(
        arity: int,
        output_tree_file: str,
        start: int = 0,
        end: int = 100,
        nodes_amount: int = 10,
        image_file: str = None,
        show_ids: bool = False,
        fig_size: Tuple[int, int] = (12, 12)
):
    tree = Tree(arity)
    tree.random_insertion(start, end, nodes_amount)

    tree.export_tree_to_file(output_tree_file)
    if image_file is not None:
        draw_tree(
            dict_from_file(SOURCES_PATH + output_tree_file),
            show_ids=show_ids,
            make_image=image_file,
            fig_size=fig_size
        )


def ultimate_test(tree_file: str, output_file: str, time_file: str, print_to_cmd: bool = False):
    with open(output_file, 'w') as f:
        f.write('')

    tree = Tree()

    start_filling_time = time.perf_counter()
    tree.read_tree_from_dict(dict_from_file(tree_file))
    end_filling_time = time.perf_counter()

    # -----------TIME MEASURING-------------
    with open(time_file, 'a') as f:
        algo_time = time.perf_counter()
        tree.print_nodes_per_level_to_file(output_file)
        end_algo_time = time.perf_counter()
        total_algo_time = end_algo_time - algo_time

        total_filling_time = end_filling_time - start_filling_time
        f.write(f'{datetime.datetime.now()}: Выполнение считывания дерева заняло {total_filling_time*1000:.3f} мс или {total_filling_time:.6f} с\n')
        f.write(f'{datetime.datetime.now()}: Выполнение алгоритма заняло {total_algo_time*1000:.3f} мс или {total_algo_time:.6f} с\n\n')
    # -------------------------------------
    if print_to_cmd:
        with open(output_file, 'r') as f:
            print(f.read())
        print(f'Выполнение считывания дерева заняло {total_filling_time * 1000:.3f} мс или {total_filling_time:.6f} с')
        print(f'Выполнение алгоритма заняло {total_algo_time * 1000:.3f} мс или {total_algo_time:.6f} с')


def showcase():
    tree = Tree(6)
    tree.random_insertion(0, 100, 20)
    tree.export_tree_to_file(SOURCES_PATH + 'showcase/tree.txt')
    ultimate_test(
        SOURCES_PATH + 'showcase/tree.txt',
        SOURCES_PATH + 'showcase/output.txt',
        SOURCES_PATH + 'showcase/time.txt',
        True
    )
