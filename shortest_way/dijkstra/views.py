import requests
from django.shortcuts import render, HttpResponse
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
        try:
            res = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM}&units=metric')

            data = res.json()

            temp = data["main"]["temp"]
            weather_conditions = data["weather"][0]["description"]
            if weather_conditions in conditions_code:
                condition = conditions_code[weather_conditions]
                weather_condition.append(condition)

            temperature.append(round(temp))
        except Exception as e:
            print("Something wrong with the network, try again later.")

    return render(request, 'index.html', {'news': news, 'temperature': temperature, 'cities': cities,
                                          'weather_condition': weather_condition})

def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

def route(request):
    point_from = request.POST.get('point_from')
    point_to = request.POST.get('point_to')

    if not point_to or point_from == '':
        return render(request, 'error.html')

    start_node = point_from
    target_node = point_to

    graph = Graph(nodes, init_graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start_node)

    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Set start node
    path.append(start_node)

    new_path = " -> ".join(reversed(path))
    way = new_path.split('->')

    route = shortest_path[target_node]

    gate = []
    flight = []
    seat = []
    time = []
    day = []

    day_item1 = random.randint(1, 31)
    day.append(day_item1)
    day.append(day_item1 + 1)
    month = random.randint(5, 12)

    for i in range(0, 6):
        gate_item = chr(random.randint(ord('A'), ord('Y'))) + str(random.randint(1, 31))
        gate.append(gate_item)

    for i in range(0, 6):
        flight_item = chr(random.randint(ord('A'), ord('Z'))) + str(random.randint(100, 1000))
        flight.append(flight_item)

    for i in range(0, 6):
        seat_item = str(random.randint(1, 60)) + chr(random.randint(ord('A'), ord('F')))
        seat.append(seat_item)

    for i in range(0, 6):
        time_item = str(random.randint(0, 2)) + str(random.randint(0, 9)) + ':' \
               + str(random.randint(1, 5)) + str(random.randint(0, 9))
        time.append(time_item)


    return render(request, 'route.html', {'way': way, 'route': route, 'day': day, 'month': month, 'gate': gate,
                                          'flight': flight, 'seat': seat, 'time': time})


