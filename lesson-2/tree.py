tree = [[1,2],[3],[4,5],[6],[7,8],[9,10],[11,12],[13,14],[],[15,16],[17],[],[18],[19,20],[],[],[],[],[],[],[]]

def grow_path(tree: list[list[int]], path: list[int]) -> list[int]:
    return tree[path[-1]]


def is_path_to_leaf(tree: list[list[int]], path: list[int]) -> bool:
    return len(tree[path[-1]]) == 0

def find_shortest_path(tree: list[list[int]]) -> list[int]:
    paths = [[0, i] for i in tree[0]]

    while True:
        new_paths = []
        for path in paths:
            if is_path_to_leaf(tree, path): return path
            next_nodes = grow_path(tree, path)

            for next_node in next_nodes:
                new_paths.append([*path, next_node])
        paths = new_paths

shortest_path = find_shortest_path(tree)
print(shortest_path)