import requests
from django.shortcuts import render, HttpResponse
import random
from .graphs import Graph, nodes, init_graph, dijkstra_algorithm
from .models import News
from .conditions import conditions_code
from django.conf import settings

OWM = settings.OWM

def index(request):
    """

    This view get a request openwather api to get temperature in the cities.
    And take all objects of News model and sent 5 last news it to template.

    :param request: get a request openwather api to get temperature in the cities.
    :return: all objects of News model and temperature
    """
    news = News.objects.order_by('-id')[:5]

    cities = ['Berlin', 'Hong Kong', 'Paris', 'London', 'Moscow', 'Madrid', 'New York']
    temperature = []
    weather_condition = []

    # Get request to the openweather api to get information about temperature
    for city in cities:
        try:
            res = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM}&units=metric')

            data = res.json()

            temp = data["main"]["temp"]
            weather_conditions = data["weather"][0]["description"]
            # Set emojis of weather conditions
            if weather_conditions in conditions_code:
                condition = conditions_code[weather_conditions]
                weather_condition.append(condition)

            temperature.append(round(temp))
        except Exception as e:
            print("Something wrong with the network, try again later.")

    return render(request, 'index.html', {'news': news, 'temperature': temperature, 'cities': cities,
                                          'weather_condition': weather_condition})

def news_list(request):
    """
    Take all News model objects and send to the template like list
    :param request: take all News model objects
    :return: all News model objects
    """
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

def route(request):
    """
    Take start node and target node from form and then send it into func
    :param request: take start node and target node
    :return: request data
    """

    point_from = request.POST.get('point_from')
    point_to = request.POST.get('point_to')

    if not point_to or point_from == '':
        return render(request, 'error.html')

    start_node = point_from
    target_node = point_to

    # Take start node and send to the dijkstra_algorithm func
    graph = Graph(nodes, init_graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start_node)

    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Set start node
    path.append(start_node)

    # Create string way separated by "->"
    new_path = " -> ".join(reversed(path))
    way = new_path.split('->')

    route = shortest_path[target_node]

    gate = []
    flight = []
    seat = []
    time = []
    day = []

    # Generate data for tickets
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


