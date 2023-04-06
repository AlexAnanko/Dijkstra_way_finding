import sys

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        '''
        Этот метод обеспечивает симметричность графика.
        Другими словами, если существует путь от узла A к B со значением V,
        должен быть путь от узла B к узлу A со значением V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        "Возвращает узлы графа"
        return self.nodes

    def get_outgoing_edges(self, node):
        "Возвращает соседей узла"
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Возвращает значение ребра между двумя узлами."
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    # Мы будем использовать этот словарь, чтобы сэкономить на посещении каждого узла и обновлять его по мере продвижения по графику
    shortest_path = {}

    # Мы будем использовать этот dict, чтобы сохранить кратчайший известный путь к найденному узлу
    previous_nodes = {}

    # Мы будем использовать max_value для инициализации значения "бесконечности" непосещенных узлов
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # Однако мы инициализируем значение начального узла 0
    shortest_path[start_node] = 0

    # Алгоритм выполняется до тех пор, пока мы не посетим все узлы
    while unvisited_nodes:
        # Приведенный ниже блок кода находит узел с наименьшей оценкой
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # Приведенный ниже блок кода извлекает соседей текущего узла и обновляет их расстояния
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # После посещения его соседей мы отмечаем узел как "посещенный"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path

nodes = ["Białystok", "Warszawa", "Łódź", "Lublin", "Kraków", "Katowice", "Wrocław", "Szczecin", "Bydgoszcz", "Gdańsk",
         "Częstochowa", "Poznań", "Hannover", "Hamburg", "Bremen", "Berlin", "Leipzig", "Dresden", "Nürnberg",
         "Stuttgart", "München", "Frankfurt am Main", "Bonn", "Köln", "Düsseldorf", "Dortmund", "Münster", "Bielefeld",
         "Vilnius", "Kaunas", "Klaipeda", "Panevėžys", "Alytus", "Riga", "Liepāja", "Daugavpils", "Tallin", "Tartu",
         "Praga", "Brno", "Ostrave", "Bratislava", "Košice", "Graz", "Viena", "Zagreb", "Osijek", "Rijeka", "Pula",
         "Zadar", "Split", "București", "Brașov", "Timișoara", "Cluj", "Athens", "Thessaloniki", "Sofia", "Varna",
         "Plovdiv", "Zürich", "Bern", "Geneva", "Milan", "Turin", "Genoa", "Venice", "Bologna", "Florence", "Rome",
         "Napoli", "Bari", "Palermo", "Catania", "Nantes", "Paris", "Lyon", "Toulouse", "Montpellier", "Marseille",
         "Nice", "Bilbao", "Zaragoza", "Barcelona", "Valencia", "Madrid", "Murcia", "Málaga", "Seville", "Budapest",
         "Kishinev", "Ljubljana", "Skopje", "Tirana", "Sarajevo", "Belgrade", "Lisbon", "Minsk"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["Białystok"]["Warszawa"] = 105
init_graph["Białystok"]["Łódź"] = 295
init_graph["Białystok"]["Lublin"] = 214
init_graph["Białystok"]["Kraków"] = 408
init_graph["Białystok"]["Katowice"] = 428
init_graph["Białystok"]["Wrocław"] = 476
init_graph["Białystok"]["Szczecin"] = 573
init_graph["Białystok"]["Bydgoszcz"] = 345
init_graph["Białystok"]["Gdańsk"] = 326
init_graph["Białystok"]["Częstochowa"] = 380
init_graph["Białystok"]["Poznań"] = 345

init_graph["Warszawa"]["Łódź"] = 119
init_graph["Warszawa"]["Lublin"] = 153
init_graph["Warszawa"]["Kraków"] = 252
init_graph["Warszawa"]["Katowice"] = 259
init_graph["Warszawa"]["Wrocław"] = 305
init_graph["Warszawa"]["Szczecin"] = 454
init_graph["Warszawa"]["Bydgoszcz"] = 226
init_graph["Warszawa"]["Gdańsk"] = 282
init_graph["Warszawa"]["Częstochowa"] = 207
init_graph["Warszawa"]["Poznań"] = 279
init_graph["Warszawa"]["Milan"] = 1145
init_graph["Warszawa"]["Turin"] = 1253
init_graph["Warszawa"]["Venice"] = 975
init_graph["Warszawa"]["Bologna"] = 1109
init_graph["Warszawa"]["Rome"] = 1309
init_graph["Warszawa"]["Napoli"] = 1359
init_graph["Warszawa"]["Bari"] = 1275
init_graph["Warszawa"]["Catania"] = 1698
init_graph["Warszawa"]["București"] = 926
init_graph["Warszawa"]["Cluj"] = 630
init_graph["Warszawa"]["Zagreb"] = 799
init_graph["Warszawa"]["Zadar"] = 989
init_graph["Warszawa"]["Paris"] = 1368
init_graph["Warszawa"]["Nice"] = 1391
init_graph["Warszawa"]["Vilnius"] = 393
init_graph["Warszawa"]["Kaunas"] = 359
init_graph["Warszawa"]["Bilbao"] = 2026
init_graph["Warszawa"]["Barcelona"] = 1866
init_graph["Warszawa"]["Valencia"] = 2166
init_graph["Warszawa"]["Madrid"] = 2280
init_graph["Warszawa"]["Málaga"] = 2633
init_graph["Warszawa"]["Seville"] = 2654
init_graph["Warszawa"]["Lisbon"] = 2748

init_graph["Łódź"]["Lublin"] = 225
init_graph["Łódź"]["Kraków"] = 192
init_graph["Łódź"]["Katowice"] = 169
init_graph["Łódź"]["Wrocław"] = 183
init_graph["Łódź"]["Szczecin"] = 382
init_graph["Łódź"]["Bydgoszcz"] = 182
init_graph["Łódź"]["Gdańsk"] = 293
init_graph["Łódź"]["Częstochowa"] = 108
init_graph["Łódź"]["Poznań"] = 187
init_graph["Łódź"]["Milan"] = 1022
init_graph["Łódź"]["Turin"] = 1135
init_graph["Łódź"]["Genoa"] = 1127
init_graph["Łódź"]["Venice"] = 870
init_graph["Łódź"]["Bologna"] = 1000
init_graph["Łódź"]["Florence"] = 1072
init_graph["Łódź"]["Rome"] = 1212
init_graph["Łódź"]["Bari"] = 1275
init_graph["Łódź"]["Catania"] = 1621

init_graph["Lublin"]["Kraków"] = 227
init_graph["Lublin"]["Katowice"] = 273
init_graph["Lublin"]["Wrocław"] = 386
init_graph["Lublin"]["Szczecin"] = 596
init_graph["Lublin"]["Bydgoszcz"] = 374
init_graph["Lublin"]["Gdańsk"] = 434
init_graph["Lublin"]["Częstochowa"] = 246
init_graph["Lublin"]["Poznań"] = 408
init_graph["Lublin"]["Milan"] = 1183
init_graph["Lublin"]["Split"] = 981

init_graph["Kraków"]["Katowice"] = 46
init_graph["Kraków"]["Wrocław"] = 236
init_graph["Kraków"]["Szczecin"] = 527
init_graph["Kraków"]["Bydgoszcz"] = 366
init_graph["Kraków"]["Gdańsk"] = 486
init_graph["Kraków"]["Częstochowa"] = 102
init_graph["Kraków"]["Poznań"] = 335
init_graph["Kraków"]["Milan"] = 952
init_graph["Kraków"]["Turin"] = 1063
init_graph["Kraków"]["Bologna"] = 888
init_graph["Kraków"]["Rome"] = 1069
init_graph["Kraków"]["Napoli"] = 1113
init_graph["Kraków"]["Bari"] = 1022
init_graph["Kraków"]["Palermo"] = 1424
init_graph["Kraków"]["Catania"] = 1451
init_graph["Kraków"]["Zadar"] = 744
init_graph["Kraków"]["Split"] = 774
init_graph["Kraków"]["Paris"] = 1265
init_graph["Kraków"]["Lyon"] = 1211
init_graph["Kraków"]["Toulouse"] = 1568
init_graph["Kraków"]["Marseille"] = 1330
init_graph["Kraków"]["Nice"] = 1190
init_graph["Kraków"]["Barcelona"] = 1681
init_graph["Kraków"]["Valencia"] = 1974
init_graph["Kraków"]["Madrid"] = 2117
init_graph["Kraków"]["Málaga"] = 2438
init_graph["Kraków"]["Seville"] = 2479
init_graph["Kraków"]["Lisbon"] = 2597

init_graph["Katowice"]["Wrocław"] = 161
init_graph["Katowice"]["Szczecin"] = 467
init_graph["Katowice"]["Bydgoszcz"] = 326
init_graph["Katowice"]["Gdańsk"] = 456
init_graph["Katowice"]["Częstochowa"] = 62
init_graph["Katowice"]["Poznań"] = 279
init_graph["Katowice"]["Milan"] = 907
init_graph["Katowice"]["Venice"] = 732
init_graph["Katowice"]["Bologna"] = 864
init_graph["Katowice"]["Rome"] = 1058
init_graph["Katowice"]["Napoli"] = 1111
init_graph["Katowice"]["Catania"] = 1457
init_graph["Katowice"]["Pula"] = 714
init_graph["Katowice"]["Split"] = 776
init_graph["Katowice"]["Barcelona"] = 1660
init_graph["Katowice"]["Málaga"] = 2400
init_graph["Katowice"]["Seville"] = 2447

init_graph["Wrocław"]["Szczecin"] = 309
init_graph["Wrocław"]["Bydgoszcz"] = 234
init_graph["Wrocław"]["Gdańsk"] = 376
init_graph["Wrocław"]["Częstochowa"] = 150
init_graph["Wrocław"]["Poznań"] = 147
init_graph["Wrocław"]["Milan"] = 947
init_graph["Wrocław"]["Turin"] = 957
init_graph["Wrocław"]["Venice"] = 715
init_graph["Wrocław"]["Bologna"] = 843
init_graph["Wrocław"]["Rome"] = 1078
init_graph["Wrocław"]["Napoli"] = 1159
init_graph["Wrocław"]["Bari"] = 1109
init_graph["Wrocław"]["Palermo"] = 1467
init_graph["Wrocław"]["Zadar"] = 787
init_graph["Wrocław"]["Split"] = 843
init_graph["Wrocław"]["Paris"] = 1068
init_graph["Wrocław"]["Barcelona"] = 1560
init_graph["Wrocław"]["Málaga"] = 2331
init_graph["Wrocław"]["Lisbon"] = 2438

init_graph["Szczecin"]["Bydgoszcz"] = 232
init_graph["Szczecin"]["Gdańsk"] = 278
init_graph["Szczecin"]["Częstochowa"] = 428
init_graph["Szczecin"]["Poznań"] = 196
init_graph["Wrocław"]["Milan"] = 947
init_graph["Wrocław"]["Turin"] = 957
init_graph["Wrocław"]["Venice"] = 715
init_graph["Wrocław"]["Bologna"] = 843
init_graph["Wrocław"]["Rome"] = 1078
init_graph["Wrocław"]["Napoli"] = 1159
init_graph["Wrocław"]["Bari"] = 1109
init_graph["Wrocław"]["Palermo"] = 1467
init_graph["Wrocław"]["Zadar"] = 787
init_graph["Wrocław"]["Split"] = 843
init_graph["Wrocław"]["Paris"] = 1068
init_graph["Wrocław"]["Barcelona"] = 1560
init_graph["Wrocław"]["Málaga"] = 2331
init_graph["Wrocław"]["Lisbon"] = 2438

init_graph["Bydgoszcz"]["Gdańsk"] = 143
init_graph["Bydgoszcz"]["Częstochowa"] = 269
init_graph["Bydgoszcz"]["Poznań"] = 108

init_graph["Gdańsk"]["Częstochowa"] = 397
init_graph["Gdańsk"]["Poznań"] = 245
init_graph["Gdańsk"]["Milan"] = 1152
init_graph["Gdańsk"]["Rome"] = 1472
init_graph["Gdańsk"]["Napoli"] = 1533
init_graph["Gdańsk"]["Catania"] = 1895
init_graph["Gdańsk"]["Zadar"] = 1165
init_graph["Gdańsk"]["Split"] = 1216
init_graph["Gdańsk"]["Paris"] = 1267
init_graph["Gdańsk"]["Barcelona"] = 1885
init_graph["Gdańsk"]["Valencia"] = 2178
init_graph["Gdańsk"]["Málaga"] = 2629

init_graph["Poznań"]["Częstochowa"] = 234
init_graph["Poznań"]["Milan"] = 952
init_graph["Poznań"]["Venice"] = 842
init_graph["Poznań"]["Rome"] = 1215
init_graph["Poznań"]["Bari"] = 1255
init_graph["Poznań"]["Pula"] = 863
init_graph["Poznań"]["Zadar"] = 931
init_graph["Poznań"]["Split"] = 988
init_graph["Poznań"]["Paris"] = 1092
init_graph["Poznań"]["Málaga"] = 2413