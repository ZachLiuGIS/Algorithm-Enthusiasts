def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start]

    parent = {}
    queue = [start]
    visited = [start]

    while queue:
        node = queue.pop(0)
        if node == end:
            return backtrace(parent, start, end)
        for adjacent in (n for n in graph[node] if n not in visited):
            visited.append(adjacent)
            parent[adjacent] = node  # <<<<< record its parent
            queue.append(adjacent)


if __name__ == '__main__':
    g = {"a": ["c"],
         "b": ["c", "e"],
         "c": ["a", "b", "d", "e"],
         "d": ["c"],
         "e": ["c", "b"]
         }

    print(bfs_shortest_path(g, 'a', 'a'))
    print(bfs_shortest_path(g, 'a', 'c'))
    print(bfs_shortest_path(g, 'a', 'e'))
    print(bfs_shortest_path(g, 'a', 'd'))
