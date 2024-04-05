from tests import *


def main():
    showcase()


    # pairs = [(4, 10000), (4, 1000000), (5, 100), (6, 60),
    #          (100, 200), (10000, 10000), (1000000, 1000000), (1000000, 2000000), (1000000, 5000000)]
    #
    # for arity, nodes_amount in pairs:
    #     # create_random_test_data(arity, SOURCES_PATH + f'report/{arity}_{nodes_amount}/tree.txt', nodes_amount=nodes_amount)
    #     ultimate_test(
    #         SOURCES_PATH + f'report/{arity}_{nodes_amount}/tree.txt',
    #         SOURCES_PATH + f'report/{arity}_{nodes_amount}/output.txt',
    #         SOURCES_PATH + f'report/{arity}_{nodes_amount}/time.txt'
    #     )

    # arity, nodes_amount = 100, 200
    # draw_tree(
    #     dict_from_file(SOURCES_PATH + f'report/{arity}_{nodes_amount}/tree.txt'),
    #     make_image=SOURCES_PATH + f'report/{arity}_{nodes_amount}/tree.png',
    #     fig_size=(50, 20)
    # )


if __name__ == '__main__':
    main()
