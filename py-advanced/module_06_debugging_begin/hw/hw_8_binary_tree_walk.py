"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход путь до файла с логами
    и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, хранящиеся в бинарном дереве уникальны
"""
import itertools
import logging
import random
import re
from collections import deque
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                    f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                    f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(1, 10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)

    node_right = get_tree(max_depth - 1, level=level + 1)

    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


def restore_tree(path_to_log_file: str):
    child_list = []
    parent_list = []
    with open(path_to_log_file, 'r') as log_file:
        for line in log_file:
            if line[:4] == 'INFO':
                try:
                    find_num = re.search(r'\[[0-9]*\]', line).group(0)
                except AttributeError:
                    find_num = re.search(r'\[[0-9]*\]', line)
                parent_list.append(find_num)
            elif line[:4] == 'DEBU':
                if 'left' in line.split('.')[0]:
                    side = 'left'
                elif 'right' in line.split('.')[0]:
                    side = 'right'
                try:
                    res = [re.search(r'\[[0-9]*\]', line).group(0), side,
                           re.search(r'\[[0-9]*\]', line.split('.')[1]).group(0)]
                except AttributeError:
                    res = [re.search(r'\[[0-9]*\]', line), side,
                           re.search(r'\[[0-9]*\]', line.split('.')[1])]
                child_list.append(res[2])
            else:
                print('Not log matchings')
    for p in parent_list:
        for c in child_list:
            if not p == c:
                parent_list.remove(c)
    print('root is', parent_list)


if __name__ == "__main__":
    logging.basicConfig(
            level=logging.DEBUG,
            format="%(levelname)s:%(message)s",
            filename="hw_8_walk_log_4.txt",
    )

    # root = get_tree(7)
    # print(root)
    # walk(root)
    restore_tree('hw_8_walk_log_1.txt')
