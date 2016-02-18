def depth_first_search(g, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend([n for n in g[node] if n not in visited])
    return visited


def depth_first_search_recursive(g, start):
    if not hasattr(depth_first_search_recursive, 'visited'):
        depth_first_search_recursive.visited = []

    depth_first_search_recursive.visited.append(start)
    for v in (n for n in g[start] if n not in depth_first_search_recursive.visited):
        depth_first_search_recursive(g, v)
    return depth_first_search_recursive.visited


if __name__ == '__main__':
    g = {"a": ["c"],
         "b": ["c", "e"],
         "c": ["a", "b", "d", "e"],
         "d": ["c"],
         "e": ["c", "b"]
         }

    print(depth_first_search(g, "a"))
    print(depth_first_search_recursive(g, "a"))
