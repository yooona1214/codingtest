# 최소 환승 2021
from collections import defaultdict, deque

# 노선 딕셔너리
routes = {
    1: [1, 2, 3, 4, 5],
    2: [3, 7, 9],
    3: [5, 6, 7, 8, 10]
}

# 노드 딕셔너리
graph = defaultdict(list)
for route, nodes in routes.items():
    for node in nodes:
        graph[node].append(route)
# print(graph) # defaultdict(<class 'list'>, {1: [1], 2: [1], 3: [1, 2], 4: [1], 5: [1, 3], 7: [2, 3], 9: [2], 6: [3], 8: [3], 10: [3]})


def find_path_with_routes(start, end):
    # Track nodes with (previous node, route taken to reach this node)
    parents = {start: (None, None)}
    queue = deque([start])

    # Track visited nodes to avoid revisiting them
    visited = {start}

    while queue:
        current = queue.popleft()

        if current == end:
            break  # Stop when we reach the end node

        current_routes = graph[current]
        for route in current_routes:
            for next_node in routes[route]:
                if next_node not in visited:
                    visited.add(next_node)
                    parents[next_node] = (current, route)
                    queue.append(next_node)

    # Reconstruct the path from end to start
    path = []
    current = end
    while current is not None:
        path.append(current)
        current, _ = parents[current]

    path.reverse()  # Reverse the path to start -> end

    # Convert path to route:nodes format
    route_nodes = defaultdict(list)
    last_route = None
    for node in path:
        _, route = parents[node]
        if route != last_route:
            last_route = route
        if route is not None:  # Skip the start node which has no associated route
            route_nodes[f"Route {route}"].append(node)

    return dict(route_nodes)


# Find the path with routes from 1 to 10
find_path_with_routes(1, 10)
# Result {'Route 1': [5], 'Route 3': [10]}