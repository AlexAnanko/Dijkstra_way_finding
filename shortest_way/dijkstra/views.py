import requests
from django.shortcuts import render
import random
from .graphs import Graph, nodes, init_graph, dijkstra_algorithm
from .models import News
from .conditions import conditions_code
from django.conf import settings

OWM = settings.OWM

def index(request):
    news = News.objects.order_by('-id')[:5]

    cities = ['Berlin', 'Hong Kong', 'Paris', 'London', 'Moscow', 'Madrid', 'New York']
    temperature = []
    weather_condition = []

    for city in cities:

        res = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM}&units=metric')

        data = res.json()

        temp = data["main"]["temp"]
        weather_conditions = data["weather"][0]["description"]
        if weather_conditions in conditions_code:
            condition = conditions_code[weather_conditions]
            weather_condition.append(condition)

        temperature.append(round(temp))

    return render(request, 'index.html', {'news': news, 'temperature': temperature, 'cities': cities,
                                          'weather_condition': weather_condition})

def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

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

    gate = []
    flight = []
    seat = []
    time = []
    day = []

    day_item1 = random.randint(1, 32)
    day.append(day_item1)
    day.append(day_item1 + 1)
    month = random.randint(5, 13)

    for i in range(0, 6):
        gate_item = chr(random.randint(ord('A'), ord('Y'))) + str(random.randint(1, 31))
        gate.append(gate_item)

    for i in range(0, 6):
        flight_item = chr(random.randint(ord('A'), ord('Z'))) + str(random.randint(100, 1000))
        flight.append(flight_item)

    for i in range(0, 6):
        seat_item = str(random.randint(1, 61)) + chr(random.randint(ord('A'), ord('F')))
        seat.append(seat_item)

    for i in range(0, 6):
        time_item = str(random.randint(0, 2)) + str(random.randint(0, 10)) + ':' \
               + str(random.randint(1, 6)) + str(random.randint(0, 10))
        time.append(time_item)

    return render(request, 'route.html', {'way': way, 'route': route, 'day': day, 'month': month, 'gate': gate,
                                          'flight': flight, 'seat': seat, 'time': time})