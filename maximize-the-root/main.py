# Run: `python ./maximize-the-root/main.py < ./maximize-the-root/input.txt`

def get_parent_children_map(vertices_count, vertices_parents):
    parent_child_map = {}

    for i in range(1, vertices_count):
        parent_index = vertices_parents[i - 1]
        if parent_index not in parent_child_map: 
            parent_child_map[parent_index] = []

        parent_child_map[parent_index].append(i + 1)

    return parent_child_map

def depth_sorted_vertices(parent_children_map):
    depth_vertices = []
    open_vertices = [1]

    depth = 0
    while len(open_vertices) > 0:
        depth_vertices.append(open_vertices.copy())

        open_vertices = [child for parent in open_vertices if parent in parent_children_map for child in parent_children_map.get(parent, [])]
        depth += 1

    return depth_vertices, depth

def maximize_root(vertices_count, vertices_values, vertices_parents):
    parent_children_map = get_parent_children_map(vertices_count, vertices_parents)
    depth_vertices, max_depth = depth_sorted_vertices(parent_children_map)

    # Analyze the vertices from the bottom up (excluding the root)
    for depth in range(max_depth - 1, 0, -1):
        vertices_of_depth = depth_vertices[depth]
        parents_children_values_map = {}

        # List all the children values for each parent
        for vertex in vertices_of_depth:
            parent_vertex = vertices_parents[vertex - 2]
            vertex_value = vertices_values[vertex - 1]

            if parent_vertex not in parents_children_values_map:
                parents_children_values_map[parent_vertex] = []

            parents_children_values_map[parent_vertex].append(vertex_value)

        for parent_vertex in parents_children_values_map:
            children_vertices_values = parents_children_values_map[parent_vertex]

            parent_vertex_value = vertices_values[parent_vertex - 1]
            min_children_value = min(children_vertices_values)

            # Average value if not the root
            if parent_vertex != 1: vertices_values[parent_vertex - 1] = (parent_vertex_value + min_children_value) // 2
            else: vertices_values[parent_vertex - 1] = parent_vertex_value + min_children_value

    return vertices_values[0]

########## TESTS ##########

import sys
solutions = []

cases_count = int(sys.stdin.readline())
for _ in range(cases_count):
    vertices_count = int(sys.stdin.readline())
    vertices_values = [int(s) for s in sys.stdin.readline().split(" ")]
    vertices_parents = [int(s) for s in sys.stdin.readline().split(" ")]

    print("Vertices count:", vertices_count)
    print("Vertices values:", vertices_values)
    print("Vertices parents:", vertices_parents)

    result = maximize_root(vertices_count, vertices_values, vertices_parents)
    solutions.append(result)

    print("Result:", result)
    print("-" * 20)

correct_solutions = [int(s.strip()) for s in open("./maximize-the-root/solution.txt", "r").readlines()]
for i, solution in enumerate(solutions):
    assert solution == correct_solutions[i], f"Expected {correct_solutions[i]} but got {solution}"