from django.shortcuts import render
import random
from graph import Graph, nodes, init_graph, dijkstra_algorithm

def index(request):
    return render(request, "index.html")

def route(request):
    point_from = request.POST.get('point_from')
    point_to = request.POST.get('point_to')

    start_node = point_from
    target_node = point_to

    graph = Graph(nodes, init_graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start_node)

    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Добавляем начальный узел вручную
    path.append(start_node)

    new_path = " -> ".join(reversed(path))
    way = new_path.split('->')

    route = shortest_path[target_node]

    day = random.randint(1, 32)
    month = random.randint(5, 13)
    gate = chr(random.randint(ord('A'), ord('Y'))) + str(random.randint(1, 31))
    flight = chr(random.randint(ord('A'), ord('Z'))) + str(random.randint(100, 1000))
    seat = str(random.randint(1, 61)) + chr(random.randint(ord('A'), ord('F')))
    time = str(random.randint(0, 23)) + ':' + str(random.randint(5, 56))

    return render(request, 'route.html', {'way': way, 'route': route, 'day': day, 'month': month, 'gate': gate,
                                          'flight': flight, 'seat': seat, 'time': time})