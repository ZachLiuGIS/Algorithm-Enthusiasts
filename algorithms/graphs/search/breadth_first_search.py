def breadth_first_search(g, start):
    visited, queue = [], [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend([n for n in g[vertex] if n not in visited])
    return visited


if __name__ == '__main__':
    g = {"a": ["c"],
         "b": ["c", "e"],
         "c": ["a", "b", "d", "e"],
         "d": ["c"],
         "e": ["c", "b"]
         }

    print(breadth_first_search(g, "a"))
