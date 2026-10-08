def dijkstra(graph, source, destination):
    n = len(graph)

    distance = [float('inf')] * n
    visited = [False] * n
    previous = [-1] * n

    distance[source] = 0

    for _ in range(n):
     
        min_dist = float('inf')
        u = -1

        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                u = i

        if u == -1:
            break

        visited[u] = True
 
        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                new_distance = distance[u] + graph[u][v]

                if new_distance < distance[v]:
                    distance[v] = new_distance
                    previous[v] = u
 
    path = []
    current = destination

    while current != -1:
        path.append(current)
        current = previous[current]

    path.reverse()

    if distance[destination] == float('inf'):
        print("No path exists.")
    else:
        print("Shortest Path:", end=" ")
        for vertex in path:
            print(vertex, end=" ")
        print()
        print("Shortest Distance:", distance[destination])

 
n = int(input("Enter number of cities: "))
 
print("Enter the adjacency matrix:")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
 
source = int(input("Enter source city: "))
destination = int(input("Enter destination city: "))
 
dijkstra(graph, source, destination)
