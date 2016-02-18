def n_level_from_source(g, start, level):
    visited, queue = [], [start]
    level_dict = {}
    return_nodes = []
    if level == 0:
        return [start]
    level_dict[start] = 0
    visited.append(start)
    while queue:
        node = queue.pop(0)
        if level_dict[node] == level:
            break

        for vertex in (n for n in g[node] if n not in visited):
            visited.append(vertex)
            level_dict[vertex] = level_dict[node] + 1
            if level_dict[vertex] == level:
                return_nodes.append(vertex)
            queue.append(vertex)
    return return_nodes

if __name__ == '__main__':
    g = {"a": ["c"],
         "b": ["c", "e"],
         "c": ["a", "b", "d", "e"],
         "d": ["c"],
         "e": ["c", "b"]
         }
    print(n_level_from_source(g, "a", 0))
    print(n_level_from_source(g, "a", 1))
    print(n_level_from_source(g, "a", 2))
