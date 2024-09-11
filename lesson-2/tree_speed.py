import collections

tree = [[1,2],[3],[4,5],[6],[7,8],[9,10],[11,12],[13,14],[],[15,16],[17],[],[18],[19,20],[],[],[],[],[],[],[]]

def grow_path(tree: list[list[int]], path: list[int]) -> list[int]:
    return tree[path[-1]]


def is_path_to_leaf(tree: list[list[int]], path: list[int]) -> bool:
    return len(tree[path[-1]]) == 0

def find_shortest_path(tree: list[list[int]]) -> list[int]:
    paths = collections.deque([[0, i] for i in tree[0]])

    while len(paths) > 0:
        path = paths.popleft()

        if is_path_to_leaf(tree, path): return path
        paths.extend([[*path, next_node] for next_node in grow_path(tree, path)])

shortest_path = find_shortest_path(tree)
print(shortest_path)