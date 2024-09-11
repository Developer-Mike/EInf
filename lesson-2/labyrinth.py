labyrinth = [[1,2],[0,5],[0,3],[2,4],[3,7],[1,6],[5,7,10],[4,6,8],[7,9],[8,12],[6,11],[10,13],[9,15],[11,14,16],[13,19],[12,20],[13,17],[16,18],[17,19],[14,18,20],[15,19]]
goal = 20

def grow_path(labyrinth: list[list[int]], path: list[int]) -> list[int]:
    return labyrinth[path[-1]]

def is_path_to_goal(path: list[int], goal: int) -> bool:
    return path[-1] == goal

def find_shortest_path(labyrinth: list[list[int]]) -> list[int]:
    paths = [[0, i] for i in labyrinth[0]]

    while True:
        new_paths = []
        for path in paths:
            if is_path_to_goal(path, goal): return path
            next_nodes = grow_path(labyrinth, path)

            for next_node in next_nodes:
                new_paths.append([*path, next_node])
        paths = new_paths

shortest_path = find_shortest_path(labyrinth)
print(shortest_path)