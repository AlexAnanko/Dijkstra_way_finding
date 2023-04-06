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

'---------GERMANY---------'

init_graph["Hannover"]["Hamburg"] = 132
init_graph["Hannover"]["Bremen"] = 98
init_graph["Hannover"]["Berlin"] = 248
init_graph["Hannover"]["Dresden"] = 313
init_graph["Hannover"]["Leipzig"] = 215
init_graph["Hannover"]["Nürnberg"] = 343
init_graph["Hannover"]["Stuttgart"] = 415
init_graph["Hannover"]["München"] = 489
init_graph["Hannover"]["Frankfurt am Main"] = 263
init_graph["Hannover"]["Bonn"] = 257
init_graph["Hannover"]["Köln"] = 250
init_graph["Hannover"]["Düsseldorf"] = 241
init_graph["Hannover"]["Dortmund"] = 184
init_graph["Hannover"]["Münster"] = 151
init_graph["Hannover"]["Bielefeld"] = 90
init_graph["Hannover"]["Catania"] = 1706
init_graph["Hannover"]["Osijek"] = 999
init_graph["Hannover"]["Paris"] = 650
init_graph["Hannover"]["Toulouse"] = 1153
init_graph["Hannover"]["Barcelona"] = 1369

init_graph["Hamburg"]["Bremen"] = 102
init_graph["Hamburg"]["Berlin"] = 254
init_graph["Hamburg"]["Dresden"] = 214
init_graph["Hamburg"]["Leipzig"] = 294
init_graph["Hamburg"]["Bielefeld"] = 209
init_graph["Hamburg"]["Münster"] = 108
init_graph["Hamburg"]["Dortmund"] = 286
init_graph["Hamburg"]["Düsseldorf"] = 339
init_graph["Hamburg"]["Köln"] = 358
init_graph["Hamburg"]["Bonn"] = 356
init_graph["Hamburg"]["Frankfurt am Main"] = 414
init_graph["Hamburg"]["Stuttgart"] = 534
init_graph["Hamburg"]["München"] = 612
init_graph["Hamburg"]["Nürnberg"] = 463
init_graph["Hamburg"]["Warszawa"] = 752
init_graph["Hamburg"]["Gdańsk"] = 561
init_graph["Hamburg"]["Milan"] = 901
init_graph["Hamburg"]["Genoa"] = 1019
init_graph["Hamburg"]["Venice"] = 918
init_graph["Hamburg"]["Florence"] = 1092
init_graph["Hamburg"]["Rome"] = 1310
init_graph["Hamburg"]["Napoli"] = 1449
init_graph["Hamburg"]["Bari"] = 1474
init_graph["Hamburg"]["Palermo"] = 1725
init_graph["Hamburg"]["Catania"] = 1830
init_graph["Hamburg"]["București"] = 1545
init_graph["Hamburg"]["Rijeka"] = 984
init_graph["Hamburg"]["Zadar"] = 1121
init_graph["Hamburg"]["Split"] = 1206
init_graph["Hamburg"]["Paris"] = 745
init_graph["Hamburg"]["Nice"] = 1119
init_graph["Hamburg"]["Vilnius"] = 1002
init_graph["Hamburg"]["Bilbao"] = 1487
init_graph["Hamburg"]["Barcelona"] = 1494
init_graph["Hamburg"]["Valencia"] = 1752
init_graph["Hamburg"]["Madrid"] = 1786
init_graph["Hamburg"]["Málaga"] = 2178
init_graph["Hamburg"]["Lisbon"] = 2199

init_graph["Bremen"]["Berlin"] = 316
init_graph["Bremen"]["Leipzig"] = 310
init_graph["Bremen"]["Dresden"] = 407
init_graph["Bremen"]["Nürnberg"] = 432
init_graph["Bremen"]["München"] = 583
init_graph["Bremen"]["Stuttgart"] = 479
init_graph["Bremen"]["Frankfurt am Main"] = 331
init_graph["Bremen"]["Bonn"] = 286
init_graph["Bremen"]["Köln"] = 270
init_graph["Bremen"]["Düsseldorf"] = 248
init_graph["Bremen"]["Dortmund"] = 197
init_graph["Bremen"]["Münster"] = 147
init_graph["Bremen"]["Bielefeld"] = 119
init_graph["Bremen"]["Zadar"] = 1106
init_graph["Bremen"]["Vilnius"] = 1094
init_graph["Bremen"]["Málaga"] = 2086

init_graph["Berlin"]["Dresden"] = 157
init_graph["Berlin"]["Leipzig"] = 143
init_graph["Berlin"]["Nürnberg"] = 429
init_graph["Berlin"]["München"] = 504
init_graph["Berlin"]["Stuttgart"] = 512
init_graph["Berlin"]["Frankfurt am Main"] = 430
init_graph["Berlin"]["Bonn"] = 478
init_graph["Berlin"]["Köln"] = 476
init_graph["Berlin"]["Düsseldorf"] = 474
init_graph["Berlin"]["Dortmund"] = 418
init_graph["Berlin"]["Münster"] = 398
init_graph["Berlin"]["Bielefeld"] = 336
init_graph["Berlin"]["Warszawa"] = 520
init_graph["Berlin"]["Kraków"] = 520
init_graph["Berlin"]["Milan"] = 843
init_graph["Berlin"]["Venice"] = 792
init_graph["Berlin"]["Bologna"] = 905
init_graph["Berlin"]["Rome"] = 1180
init_graph["Berlin"]["Napoli"] = 1301
init_graph["Berlin"]["Bari"] = 1294
init_graph["Berlin"]["Palermo"] = 1594
init_graph["Berlin"]["Catania"] = 1679
init_graph["Berlin"]["București"] = 1294
init_graph["Berlin"]["Cluj"] = 975
init_graph["Berlin"]["Rijeka"] = 817
init_graph["Berlin"]["Pula"] = 849
init_graph["Berlin"]["Zadar"] = 948
init_graph["Berlin"]["Split"] = 1022
init_graph["Berlin"]["Nantes"] = 1221
init_graph["Berlin"]["Paris"] = 878
init_graph["Berlin"]["Montpellier"] = 1216
init_graph["Berlin"]["Marseille"] = 1186
init_graph["Berlin"]["Nice"] = 1087
init_graph["Berlin"]["Vilnius"] = 818
init_graph["Berlin"]["Barcelona"] = 1504
init_graph["Berlin"]["Valencia"] = 1795
init_graph["Berlin"]["Madrid"] = 1851
init_graph["Berlin"]["Málaga"] = 2241
init_graph["Berlin"]["Seville"] = 2258
init_graph["Berlin"]["Lisbon"] = 2314

init_graph["Dresden"]["Leipzig"] = 55
init_graph["Dresden"]["Nürnberg"] = 259
init_graph["Dresden"]["München"] = 360
init_graph["Dresden"]["Stuttgart"] = 414
init_graph["Dresden"]["Frankfurt am Main"] = 373
init_graph["Dresden"]["Bonn"] = 467
init_graph["Dresden"]["Köln"] = 475
init_graph["Dresden"]["Düsseldorf"] = 487
init_graph["Dresden"]["Dortmund"] = 441
init_graph["Dresden"]["Münster"] = 436
init_graph["Dresden"]["Bielefeld"] = 376
init_graph["Dresden"]["Warszawa"] = 509
init_graph["Dresden"]["Gdańsk"] = 480

init_graph["Leipzig"]["Nürnberg"] = 230
init_graph["Leipzig"]["München"] = 360
init_graph["Leipzig"]["Stuttgart"] = 366
init_graph["Leipzig"]["Frankfurt am Main"] = 303
init_graph["Leipzig"]["Bonn"] = 375
init_graph["Leipzig"]["Köln"] = 378
init_graph["Leipzig"]["Düsseldorf"] = 390
init_graph["Leipzig"]["Dortmund"] = 341
init_graph["Leipzig"]["Münster"] = 335
init_graph["Leipzig"]["Bielefeld"] = 275
init_graph["Leipzig"]["Catania"] = 1568

init_graph["Nürnberg"]["München"] = 150
init_graph["Nürnberg"]["Stuttgart"] = 157
init_graph["Nürnberg"]["Frankfurt am Main"] = 190
init_graph["Nürnberg"]["Bonn"] = 318
init_graph["Nürnberg"]["Köln"] = 337
init_graph["Nürnberg"]["Düsseldorf"] = 364
init_graph["Nürnberg"]["Dortmund"] = 343
init_graph["Nürnberg"]["Münster"] = 371
init_graph["Nürnberg"]["Bielefeld"] = 337
init_graph["Nürnberg"]["Łódź"] = 638
init_graph["Nürnberg"]["Kraków"] = 629
init_graph["Nürnberg"]["Venice"] = 456
init_graph["Nürnberg"]["Bologna"] = 551
init_graph["Nürnberg"]["Napoli"] = 989
init_graph["Nürnberg"]["Bari"] = 1030
init_graph["Nürnberg"]["Palermo"] = 1263
init_graph["Nürnberg"]["Catania"] = 1370
init_graph["Nürnberg"]["București"] = 1266
init_graph["Nürnberg"]["Cluj"] = 983
init_graph["Nürnberg"]["Zadar"] = 678
init_graph["Nürnberg"]["Paris"] = 638
init_graph["Nürnberg"]["Toulouse"] = 983
init_graph["Nürnberg"]["Vilnius"] = 1127
init_graph["Nürnberg"]["Kaunas"] = 1062
init_graph["Nürnberg"]["Barcelona"] = 1133
init_graph["Nürnberg"]["Valencia"] = 1433
init_graph["Nürnberg"]["Málaga"] = 1887
init_graph["Nürnberg"]["Seville"] = 1916

init_graph["München"]["Stuttgart"] = 191
init_graph["München"]["Frankfurt am Main"] = 300
init_graph["München"]["Bonn"] = 433
init_graph["München"]["Köln"] = 456
init_graph["München"]["Düsseldorf"] = 486
init_graph["München"]["Dortmund"] = 478
init_graph["München"]["Münster"] = 510
init_graph["München"]["Bielefeld"] = 482
init_graph["München"]["Warszawa"] = 804
init_graph["München"]["Kraków"] = 635
init_graph["München"]["Wrocław"] = 505
init_graph["München"]["Gdańsk"] = 842
init_graph["München"]["Poznań"] = 604
init_graph["München"]["Milan"] = 348
init_graph["München"]["Turin"] = 453
init_graph["München"]["Genoa"] = 464
init_graph["München"]["Venice"] = 320
init_graph["München"]["Bologna"] = 405
init_graph["München"]["Florence"] = 486
init_graph["München"]["Rome"] = 698
init_graph["München"]["Napoli"] = 852
init_graph["München"]["Bari"] = 884
init_graph["München"]["Palermo"] = 1113
init_graph["München"]["Catania"] = 1246
init_graph["München"]["București"] = 1187
init_graph["München"]["Timișoara"] = 782
init_graph["München"]["Cluj"] = 916
init_graph["München"]["Zagreb"] = 423
init_graph["München"]["Osijek"] = 612
init_graph["München"]["Rijeka"] = 397
init_graph["München"]["Pula"] = 403
init_graph["München"]["Zadar"] = 535
init_graph["München"]["Split"] = 628
init_graph["München"]["Paris"] = 684
init_graph["München"]["Lyon"] = 575
init_graph["München"]["Toulouse"] = 934
init_graph["München"]["Marseille"] = 722
init_graph["München"]["Nice"] = 595
init_graph["München"]["Vilnius"] = 1191
init_graph["München"]["Kaunas"] = 1135
init_graph["München"]["Bilbao"] = 1248
init_graph["München"]["Zaragoza"] = 1223
init_graph["München"]["Barcelona"] = 1095
init_graph["München"]["Valencia"] = 1360
init_graph["München"]["Madrid"] = 1485
init_graph["München"]["Málaga"] = 1820
init_graph["München"]["Seville"] = 1860
init_graph["München"]["Lisbon"] = 1986

init_graph["Stuttgart"]["Frankfurt am Main"] = 153
init_graph["Stuttgart"]["Bonn"] = 264
init_graph["Stuttgart"]["Köln"] = 288
init_graph["Stuttgart"]["Düsseldorf"] = 322
init_graph["Stuttgart"]["Dortmund"] = 328
init_graph["Stuttgart"]["Münster"] = 385
init_graph["Stuttgart"]["Bielefeld"] = 364
init_graph["Stuttgart"]["Warszawa"] = 914
init_graph["Stuttgart"]["Kraków"] = 780
init_graph["Stuttgart"]["Milan"] = 368
init_graph["Stuttgart"]["Venice"] = 441
init_graph["Stuttgart"]["Rome"] = 808
init_graph["Stuttgart"]["Napoli"] = 968
init_graph["Stuttgart"]["Bari"] = 1043
init_graph["Stuttgart"]["Palermo"] = 1219
init_graph["Stuttgart"]["Catania"] = 1344
init_graph["Stuttgart"]["București"] = 1376
init_graph["Stuttgart"]["Timișoara"] = 972
init_graph["Stuttgart"]["Zagreb"] = 619
init_graph["Stuttgart"]["Rijeka"] = 568
init_graph["Stuttgart"]["Pula"] = 562
init_graph["Stuttgart"]["Zadar"] = 703
init_graph["Stuttgart"]["Split"] = 799
init_graph["Stuttgart"]["Nantes"] = 819
init_graph["Stuttgart"]["Paris"] = 500
init_graph["Stuttgart"]["Lyon"] = 468
init_graph["Stuttgart"]["Marseille"] = 676
init_graph["Stuttgart"]["Nice"] = 589
init_graph["Stuttgart"]["Bilbao"] = 1116
init_graph["Stuttgart"]["Barcelona"] = 988
init_graph["Stuttgart"]["Valencia"] = 1285
init_graph["Stuttgart"]["Seville"] = 1761
init_graph["Stuttgart"]["Lisbon"] = 1841

init_graph["Frankfurt am Main"]["Bonn"] = 131
init_graph["Frankfurt am Main"]["Köln"] = 153
init_graph["Frankfurt am Main"]["Düsseldorf"] = 183
init_graph["Frankfurt am Main"]["Dortmund"] = 178
init_graph["Frankfurt am Main"]["Münster"] = 218
init_graph["Frankfurt am Main"]["Bielefeld"] = 169
init_graph["Frankfurt am Main"]["Warszawa"] = 895
init_graph["Frankfurt am Main"]["Kraków"] = 800
init_graph["Frankfurt am Main"]["Katowice"] = 744
init_graph["Frankfurt am Main"]["Wrocław"] = 599
init_graph["Frankfurt am Main"]["Gdańsk"] = 827
init_graph["Frankfurt am Main"]["Poznań"] = 631
init_graph["Frankfurt am Main"]["Milan"] = 519
init_graph["Frankfurt am Main"]["Turin"] = 566
init_graph["Frankfurt am Main"]["Venice"] = 585
init_graph["Frankfurt am Main"]["Bologna"] = 652
init_graph["Frankfurt am Main"]["Florence"] = 727
init_graph["Frankfurt am Main"]["Rome"] = 960
init_graph["Frankfurt am Main"]["Napoli"] = 1115
init_graph["Frankfurt am Main"]["Bari"] = 1183
init_graph["Frankfurt am Main"]["Palermo"] = 1367
init_graph["Frankfurt am Main"]["Catania"] = 1493
init_graph["Frankfurt am Main"]["București"] = 1454
init_graph["Frankfurt am Main"]["Timișoara"] = 1058
init_graph["Frankfurt am Main"]["Cluj"] = 1160
init_graph["Frankfurt am Main"]["Zagreb"] = 726
init_graph["Frankfurt am Main"]["Rijeka"] = 700
init_graph["Frankfurt am Main"]["Pula"] = 700
init_graph["Frankfurt am Main"]["Zadar"] = 837
init_graph["Frankfurt am Main"]["Split"] = 941
init_graph["Frankfurt am Main"]["Nantes"] = 807
init_graph["Frankfurt am Main"]["Paris"] = 478
init_graph["Frankfurt am Main"]["Lyon"] = 563
init_graph["Frankfurt am Main"]["Toulouse"] = 899
init_graph["Frankfurt am Main"]["Marseille"] = 789
init_graph["Frankfurt am Main"]["Nice"] = 716
init_graph["Frankfurt am Main"]["Vilnius"] = 1233
init_graph["Frankfurt am Main"]["Kaunas"] = 1156
init_graph["Frankfurt am Main"]["Bilbao"] = 1155
init_graph["Frankfurt am Main"]["Barcelona"] = 1043
init_graph["Frankfurt am Main"]["Valencia"] = 1371
init_graph["Frankfurt am Main"]["Madrid"] = 1447
init_graph["Frankfurt am Main"]["Málaga"] = 1821
init_graph["Frankfurt am Main"]["Seville"] = 1837
init_graph["Frankfurt am Main"]["Lisbon"] = 1893

init_graph["Köln"]["Düsseldorf"] = 35
init_graph["Köln"]["Dortmund"] = 73
init_graph["Köln"]["Münster"] = 123
init_graph["Köln"]["Bielefeld"] = 163
init_graph["Köln"]["Warszawa"] = 977
init_graph["Köln"]["Łódź"] = 867
init_graph["Köln"]["Katowice"] = 854
init_graph["Köln"]["Gdańsk"] = 864
init_graph["Köln"]["Milan"] = 631
init_graph["Köln"]["Venice"] = 730
init_graph["Köln"]["Bologna"] = 788
init_graph["Köln"]["Rome"] = 1091
init_graph["Köln"]["Napoli"] = 1255
init_graph["Köln"]["Bari"] = 1330
init_graph["Köln"]["Palermo"] = 1498
init_graph["Köln"]["Catania"] = 1629
init_graph["Köln"]["Zagreb"] = 886
init_graph["Köln"]["Osijek"] = 1053
init_graph["Köln"]["Rijeka"] = 850
init_graph["Köln"]["Pula"] = 849
init_graph["Köln"]["Zadar"] = 971
init_graph["Köln"]["Split"] = 1082
init_graph["Köln"]["Marseille"] = 857
init_graph["Köln"]["Nice"] = 809
init_graph["Köln"]["Kaunas"] = 1215
init_graph["Köln"]["Barcelona"] = 1134
init_graph["Köln"]["Valencia"] = 1398
init_graph["Köln"]["Málaga"] = 1821
init_graph["Köln"]["Seville"] = 1822
init_graph["Köln"]["Lisbon"] = 1853

init_graph["Düsseldorf"]["Dortmund"] = 58
init_graph["Düsseldorf"]["Münster"] = 101
init_graph["Düsseldorf"]["Bielefeld"] = 151
init_graph["Düsseldorf"]["Warszawa"] = 982
init_graph["Düsseldorf"]["Kraków"] = 925
init_graph["Düsseldorf"]["Wrocław"] = 705
init_graph["Düsseldorf"]["Milan"] = 665
init_graph["Düsseldorf"]["Venice"] = 763
init_graph["Düsseldorf"]["Bologna"] = 822
init_graph["Düsseldorf"]["Rome"] = 1125
init_graph["Düsseldorf"]["Napoli"] = 1289
init_graph["Düsseldorf"]["Bari"] = 1363
init_graph["Düsseldorf"]["Palermo"] = 1532
init_graph["Düsseldorf"]["Catania"] = 1663
init_graph["Düsseldorf"]["București"] = 1621
init_graph["Düsseldorf"]["Zagreb"] = 916
init_graph["Düsseldorf"]["Osijek"] = 1090
init_graph["Düsseldorf"]["Rijeka"] = 882
init_graph["Düsseldorf"]["Pula"] = 881
init_graph["Düsseldorf"]["Zadar"] = 1019
init_graph["Düsseldorf"]["Split"] = 1114
init_graph["Düsseldorf"]["Nantes"] = 751
init_graph["Düsseldorf"]["Paris"] = 411
init_graph["Düsseldorf"]["Lyon"] = 623
init_graph["Düsseldorf"]["Toulouse"] = 936
init_graph["Düsseldorf"]["Marseille"] = 888
init_graph["Düsseldorf"]["Nice"] = 842
init_graph["Düsseldorf"]["Bilbao"] = 1147
init_graph["Düsseldorf"]["Barcelona"] = 1165
init_graph["Düsseldorf"]["Valencia"] = 1420
init_graph["Düsseldorf"]["Madrid"] = 1447
init_graph["Düsseldorf"]["Málaga"] = 1840
init_graph["Düsseldorf"]["Seville"] = 1839
init_graph["Düsseldorf"]["Lisbon"] = 1864

init_graph["Dortmund"]["Łódź"] = 831
init_graph["Dortmund"]["Kraków"] = 870
init_graph["Dortmund"]["Katowice"] = 811
init_graph["Dortmund"]["Wrocław"] = 646
init_graph["Dortmund"]["Gdańsk"] = 793
init_graph["Dortmund"]["Rome"] = 1132
init_graph["Dortmund"]["Catania"] = 1668
init_graph["Dortmund"]["București"] = 1579
init_graph["Dortmund"]["Timișoara"] = 1187
init_graph["Dortmund"]["Cluj"] = 1278
init_graph["Dortmund"]["Zagreb"] = 892
init_graph["Dortmund"]["Rijeka"] = 868
init_graph["Dortmund"]["Split"] = 1099
init_graph["Dortmund"]["Vilnius"] = 1226
init_graph["Dortmund"]["Málaga"] = 1900

init_graph["Münster"]["Bielefeld"] = 63
init_graph["Münster"]["Katowice"] = 820
init_graph["Münster"]["Bari"] = 1407
init_graph["Münster"]["Palermo"] = 1444
init_graph["Münster"]["Catania"] = 1727
init_graph["Münster"]["Osijek"] = 612
init_graph["Münster"]["Pula"] = 925
init_graph["Münster"]["Zadar"] = 1057

'----------LITHUNIA---------'

init_graph["Vilnius"]["Kaunas"] = 92
init_graph["Vilnius"]["Klaipeda"] = 487
init_graph["Vilnius"]["Panevėžys"] = 130
init_graph["Vilnius"]["Alytus"] = 86
init_graph["Vilnius"]["Split"] = 1395

init_graph["Kaunas"]["Klaipeda"] = 197
init_graph["Kaunas"]["Panevėžys"] = 96
init_graph["Kaunas"]["Alytus"] = 56

init_graph["Klaipeda"]["Panevėžys"] = 201
init_graph["Klaipeda"]["Alytus"] = 235

init_graph["Alytus"]["Panevėžys"] = 153

'---------LATVIA--------'

init_graph["Riga"]["Liepāja"] = 195
init_graph["Riga"]["Daugavpils"] = 192
init_graph["Riga"]["Warszawa"] = 562
init_graph["Riga"]["Kraków"] = 810
init_graph["Riga"]["Gdańsk"] = 446
init_graph["Riga"]["Zürich"] = 1480
init_graph["Riga"]["Geneva"] = 1706
init_graph["Riga"]["Milan"] = 1592
init_graph["Riga"]["Venice"] = 1505
init_graph["Riga"]["Rome"] = 1876
init_graph["Riga"]["Napoli"] = 1924
init_graph["Riga"]["Catania"] = 2261
init_graph["Riga"]["București"] = 1396
init_graph["Riga"]["Brașov"] = 1260
init_graph["Riga"]["Rijeka"] = 1455
init_graph["Riga"]["Split"] = 1590
init_graph["Riga"]["Hannover"] = 1041
init_graph["Riga"]["Hamburg"] = 969
init_graph["Riga"]["Berlin"] = 841
init_graph["Riga"]["Stuttgart"] = 1345
init_graph["Riga"]["München"] = 1282
init_graph["Riga"]["Frankfurt am Main"] = 1271
init_graph["Riga"]["Bonn"] = 1310
init_graph["Riga"]["Köln"] = 1290
init_graph["Riga"]["Düsseldorf"] = 1295
init_graph["Riga"]["Bielefeld"] = 1146
init_graph["Riga"]["Paris"] = 1703
init_graph["Riga"]["Nice"] = 1888
init_graph["Riga"]["Vilnius"] = 265
init_graph["Riga"]["Klaipeda"] = 229
init_graph["Riga"]["Bilbao"] = 2421
init_graph["Riga"]["Barcelona"] = 2335
init_graph["Riga"]["Valencia"] = 2625
init_graph["Riga"]["Madrid"] = 2705
init_graph["Riga"]["Málaga"] = 3085
init_graph["Riga"]["Lisbon"] = 3150

init_graph["Liepāja"]["Daugavpils"] = 349

'----------ESTONIA--------'

init_graph["Tallin"]["Warszawa"] = 841
init_graph["Tallin"]["Zürich"] = 1712
init_graph["Tallin"]["Milan"] = 1831
init_graph["Tallin"]["Venice"] = 1764
init_graph["Tallin"]["Rome"] = 2126
init_graph["Tallin"]["Catania"] = 2540
init_graph["Tallin"]["Split"] = 1860
init_graph["Tallin"]["Berlin"] = 1045
init_graph["Tallin"]["Nürnberg"] = 1414
init_graph["Tallin"]["München"] = 1520
init_graph["Tallin"]["Frankfurt am Main"] = 1470
init_graph["Tallin"]["Paris"] = 1860
init_graph["Tallin"]["Nice"] = 2119
init_graph["Tallin"]["Vilnius"] = 532
init_graph["Tallin"]["Riga"] = 280
init_graph["Tallin"]["Barcelona"] = 2550
init_graph["Tallin"]["Málaga"] = 3280
init_graph["Tallin"]["Athens"] = 2390
init_graph["Tallin"]["Viena"] = 1362

init_graph["Tartu"]["Warszawa"] = 773
init_graph["Tartu"]["Zürich"] = 1718
init_graph["Tartu"]["Milan"] = 1864
init_graph["Tartu"]["Berlin"] = 1062
init_graph["Tartu"]["Frankfurt am Main"] = 1490
init_graph["Tartu"]["Paris"] = 1908
init_graph["Tartu"]["Nice"] = 2112
init_graph["Tartu"]["Vilnius"] = 420
init_graph["Tartu"]["Klaipeda"] = 450
init_graph["Tartu"]["Barcelona"] = 2550
init_graph["Tartu"]["Athens"] = 2279
init_graph["Tartu"]["Viena"] = 1320

'--------CZHECH-------'

init_graph["Praga"]["Brno"] = 184
init_graph["Praga"]["Ostrave"] = 277
init_graph["Praga"]["Warszawa"] = 520
init_graph["Praga"]["Kraków"] = 394
init_graph["Praga"]["Gdańsk"] = 551
init_graph["Praga"]["Zürich"] = 527
init_graph["Praga"]["Geneva"] = 750
init_graph["Praga"]["Milan"] = 646
init_graph["Praga"]["Turin"] = 750
init_graph["Praga"]["Venice"] = 536
init_graph["Praga"]["Bologna"] = 663
init_graph["Praga"]["Rome"] = 923
init_graph["Praga"]["Napoli"] = 1028
init_graph["Praga"]["Bari"] = 1014
init_graph["Praga"]["Catania"] = 1407
init_graph["Praga"]["București"] = 1080
init_graph["Praga"]["Sofia"] = 1072
init_graph["Praga"]["Varna"] = 1272
init_graph["Praga"]["Zadar"] = 670
init_graph["Praga"]["Split"] = 742
init_graph["Praga"]["München"] = 265
init_graph["Praga"]["Frankfurt am Main"] = 410
init_graph["Praga"]["Bonn"] = 524
init_graph["Praga"]["Köln"] = 536
init_graph["Praga"]["Düsseldorf"] = 553
init_graph["Praga"]["Nantes"] = 1213
init_graph["Praga"]["Paris"] = 875
init_graph["Praga"]["Lyon"] = 860
init_graph["Praga"]["Marseille"] = 1021
init_graph["Praga"]["Riga"] = 993
init_graph["Praga"]["Bilbao"] = 1520
init_graph["Praga"]["Barcelona"] = 1353
init_graph["Praga"]["Valencia"] = 1651
init_graph["Praga"]["Madrid"] = 1772
init_graph["Praga"]["Málaga"] = 2116
init_graph["Praga"]["Seville"] = 2150
init_graph["Praga"]["Lisbon"] = 2231

init_graph["Brno"]["Ostrave"] = 140
init_graph["Brno"]["Milan"] = 695
init_graph["Brno"]["Varna"] = 1086

init_graph["Ostrave"]["Warszawa"] = 319
init_graph["Ostrave"]["Varna"] = 1033

'-------SLOVAKIA-------'

init_graph["Bratislava"]["Košice"] = 312
init_graph["Bratislava"]["Milan"] = 680
init_graph["Bratislava"]["Rome"] = 790
init_graph["Bratislava"]["Sofia"] = 777
init_graph["Bratislava"]["Zagreb"] = 284
init_graph["Bratislava"]["Kaunas"] = 879
init_graph["Bratislava"]["Barcelona"] = 1413
init_graph["Bratislava"]["Athens"] = 1260
init_graph["Bratislava"]["Thessaloniki"] = 965

init_graph["Košice"]["Warszawa"] = 391
init_graph["Košice"]["Praga"] = 519
init_graph["Košice"]["Düsseldorf"] = 1072
init_graph["Košice"]["Viena"] = 363

'--------AUSTRIA-------'

init_graph["Graz"]["Viena"] = 151
init_graph["Graz"]["Zürich"] = 522
init_graph["Graz"]["Hamburg"] = 825
init_graph["Graz"]["Berlin"] = 632
init_graph["Graz"]["Stuttgart"] = 507
init_graph["Graz"]["München"] = 313
init_graph["Graz"]["Frankfurt am Main"] = 609
init_graph["Graz"]["Düsseldorf"] = 786
init_graph["Graz"]["Nantes"] = 1343

init_graph["Viena"]["Warszawa"] = 563
init_graph["Viena"]["Kraków"] = 332
init_graph["Viena"]["Zürich"] = 602
init_graph["Viena"]["Geneva"] = 810
init_graph["Viena"]["Milan"] = 625
init_graph["Viena"]["Venice"] = 433
init_graph["Viena"]["Bologna"] = 565
init_graph["Viena"]["Florence"] = 632
init_graph["Viena"]["Rome"] = 766
init_graph["Viena"]["Napoli"] = 836
init_graph["Viena"]["Bari"] = 788
init_graph["Viena"]["Palermo"] = 1145
init_graph["Viena"]["Catania"] = 1196
init_graph["Viena"]["București"] = 857
init_graph["Viena"]["Cluj"] = 571
init_graph["Viena"]["Sofia"] = 823
init_graph["Viena"]["Varna"] = 1045
init_graph["Viena"]["Praga"] = 278
init_graph["Viena"]["Zagreb"] = 268
init_graph["Viena"]["Pula"] = 413
init_graph["Viena"]["Zadar"] = 463
init_graph["Viena"]["Split"] = 519
init_graph["Viena"]["Hannover"] = 661
init_graph["Viena"]["Hamburg"] = 768
init_graph["Viena"]["Bremen"] = 758
init_graph["Viena"]["Berlin"] = 521
init_graph["Viena"]["Leipzig"] = 469
init_graph["Viena"]["Nürnberg"] = 412
init_graph["Viena"]["Stuttgart"] = 533
init_graph["Viena"]["München"] = 355
init_graph["Viena"]["Frankfurt am Main"] = 598
init_graph["Viena"]["Bonn"] = 743
init_graph["Viena"]["Köln"] = 746
init_graph["Viena"]["Düsseldorf"] = 767
init_graph["Viena"]["Dortmund"] = 727
init_graph["Viena"]["Nantes"] = 1343
init_graph["Viena"]["Paris"] = 1033
init_graph["Viena"]["Lyon"] = 915
init_graph["Viena"]["Marseille"] = 1012
init_graph["Viena"]["Nice"] = 876
init_graph["Viena"]["Vilnius"] = 943
init_graph["Viena"]["Klaipeda"] = 895
init_graph["Viena"]["Riga"] = 1103
init_graph["Viena"]["Liepāja"] = 974
init_graph["Viena"]["Daugavpils"] = 1099
init_graph["Viena"]["Bilbao"] = 1593
init_graph["Viena"]["Zaragoza"] = 1545
init_graph["Viena"]["Barcelona"] = 1351
init_graph["Viena"]["Valencia"] = 1652
init_graph["Viena"]["Madrid"] = 1809
init_graph["Viena"]["Málaga"] = 2120
init_graph["Viena"]["Seville"] = 2174
init_graph["Viena"]["Lisbon"] = 2308
init_graph["Viena"]["Athens"] = 1283
init_graph["Viena"]["Thessaloniki"] = 1002

'-------CROATIA-------'

init_graph["Zagreb"]["Osijek"] = 213
init_graph["Zagreb"]["Rijeka"] = 132
init_graph["Zagreb"]["Pula"] = 191
init_graph["Zagreb"]["Zadar"] = 197
init_graph["Zagreb"]["Split"] = 259

init_graph["Osijek"]["Rijeka"] = 333
init_graph["Osijek"]["Pula"] = 388
init_graph["Osijek"]["Zadar"] = 316
init_graph["Osijek"]["Split"] = 289

init_graph["Rijeka"]["Pula"] = 68
init_graph["Rijeka"]["Zadar"] = 150
init_graph["Rijeka"]["Split"] = 257

init_graph["Pula"]["Zadar"] = 138
init_graph["Pula"]["Split"] = 256

init_graph["Zadar"]["Split"] = 118

init_graph["Split"]["Vilnius"] = 1395

'-------ROMANIA-------'

init_graph["București"]["Brașov"] = 142
init_graph["București"]["Timișoara"] = 410
init_graph["București"]["Cluj"] = 309
init_graph["București"]["Zadar"] = 855
init_graph["București"]["Split"] = 790
init_graph["București"]["Lisbon"] = 2975

init_graph["Brașov"]["Timișoara"] = 338
init_graph["Brașov"]["Cluj"] = 211

init_graph["Timișoara"]["Cluj"] = 214

'-------GREECE-------'

init_graph["Athens"]["Thessaloniki"] = 304
init_graph["Athens"]["Warszawa"] = 1600
init_graph["Athens"]["Kraków"] = 1389
init_graph["Athens"]["Katowice"] = 1425
init_graph["Athens"]["Wrocław"] = 1565
init_graph["Athens"]["Zürich"] = 1633
init_graph["Athens"]["Geneva"] = 1712
init_graph["Athens"]["Milan"] = 1480
init_graph["Athens"]["Venice"] = 1272
init_graph["Athens"]["Bologna"] = 1229
init_graph["Athens"]["Florence"] = 1247
init_graph["Athens"]["Rome"] = 1054
init_graph["Athens"]["Napoli"] = 893
init_graph["Athens"]["Bari"] = 702
init_graph["Athens"]["Palermo"] = 949
init_graph["Athens"]["Catania"] = 782
init_graph["Athens"]["București"] = 760
init_graph["Athens"]["Sofia"] = 531
init_graph["Athens"]["Praga"] = 1555
init_graph["Athens"]["Zagreb"] = 1084
init_graph["Athens"]["Split"] = 895
init_graph["Athens"]["Hannover"] = 1947
init_graph["Athens"]["Hamburg"] = 2039
init_graph["Athens"]["Berlin"] = 1799
init_graph["Athens"]["Nürnberg"] = 1641
init_graph["Athens"]["Stuttgart"] = 1691
init_graph["Athens"]["München"] = 1519
init_graph["Athens"]["Frankfurt am Main"] = 1817
init_graph["Athens"]["Bonn"] = 1954
init_graph["Athens"]["Köln"] = 1968
init_graph["Athens"]["Düsseldorf"] = 2005
init_graph["Athens"]["Nantes"] = 2315
init_graph["Athens"]["Paris"] = 2107
init_graph["Athens"]["Lyon"] = 1797
init_graph["Athens"]["Toulouse"] = 1996
init_graph["Athens"]["Montpellier"] = 1798
init_graph["Athens"]["Marseille"] = 1673
init_graph["Athens"]["Nice"] = 1543
init_graph["Athens"]["Vilnius"] = 1861
init_graph["Athens"]["Riga"] = 2111
init_graph["Athens"]["Bilbao"] = 2330
init_graph["Athens"]["Barcelona"] = 1898
init_graph["Athens"]["Valencia"] = 2118
init_graph["Athens"]["Madrid"] = 2389
init_graph["Athens"]["Málaga"] = 2502
init_graph["Athens"]["Seville"] = 2625
init_graph["Athens"]["Lisbon"] = 2872

init_graph["Thessaloniki"]["Warszawa"] = 1304
init_graph["Thessaloniki"]["Kraków"] = 1091
init_graph["Thessaloniki"]["Zürich"] = 1380
init_graph["Thessaloniki"]["Geneva"] = 1496
init_graph["Thessaloniki"]["Milan"] = 1246
init_graph["Thessaloniki"]["Venice"] = 1024
init_graph["Thessaloniki"]["Bologna"] = 1049
init_graph["Thessaloniki"]["Rome"] = 889
init_graph["Thessaloniki"]["Napoli"] = 736
init_graph["Thessaloniki"]["București"] = 505
init_graph["Thessaloniki"]["Praga"] = 1261
init_graph["Thessaloniki"]["Zagreb"] = 806
init_graph["Thessaloniki"]["Hannover"] = 1657
init_graph["Thessaloniki"]["Hamburg"] = 1746
init_graph["Thessaloniki"]["Berlin"] = 1519
init_graph["Thessaloniki"]["Nürnberg"] = 1361
init_graph["Thessaloniki"]["Stuttgart"] = 1422
init_graph["Thessaloniki"]["München"] = 1238
init_graph["Thessaloniki"]["Frankfurt am Main"] = 1612
init_graph["Thessaloniki"]["Bonn"] = 1679
init_graph["Thessaloniki"]["Köln"] = 1683
init_graph["Thessaloniki"]["Düsseldorf"] = 1784
init_graph["Thessaloniki"]["Dortmund"] = 1697
init_graph["Thessaloniki"]["Paris"] = 1859
init_graph["Thessaloniki"]["Riga"] = 1823
init_graph["Thessaloniki"]["Barcelona"] = 1745

'-------BULGARIA-------'

init_graph["Sofia"]["Varna"] = 378
init_graph["Sofia"]["Plovdiv"] = 133
init_graph["Sofia"]["Warszawa"] = 1069
init_graph["Sofia"]["Wrocław"] = 1058
init_graph["Sofia"]["Milan"] = 1141
init_graph["Sofia"]["Venice"] = 935
init_graph["Sofia"]["Bologna"] = 986
init_graph["Sofia"]["Rome"] = 895
init_graph["Sofia"]["Napoli"] = 787
init_graph["Sofia"]["Bari"] = 568
init_graph["Sofia"]["Catania"] = 916
init_graph["Sofia"]["București"] = 290
init_graph["Sofia"]["Zagreb"] = 678
init_graph["Sofia"]["Zadar"] = 669
init_graph["Sofia"]["Hamburg"] = 1561
init_graph["Sofia"]["Berlin"] = 1306
init_graph["Sofia"]["Nürnberg"] = 1210
init_graph["Sofia"]["München"] = 1103
init_graph["Sofia"]["Frankfurt am Main"] = 1436
init_graph["Sofia"]["Bonn"] = 1531
init_graph["Sofia"]["Köln"] = 1532
init_graph["Sofia"]["Paris"] = 1760
init_graph["Sofia"]["Nice"] = 1317
init_graph["Sofia"]["Barcelona"] = 1764
init_graph["Sofia"]["Valencia"] = 2025
init_graph["Sofia"]["Madrid"] = 2250
init_graph["Sofia"]["Málaga"] = 2460
init_graph["Sofia"]["Lisbon"] = 2762

init_graph["Varna"]["Plovdiv"] = 285
init_graph["Varna"]["Kraków"] = 976
init_graph["Varna"]["Katowice"] = 1036
init_graph["Varna"]["Hamburg"] = 1738
init_graph["Varna"]["Berlin"] = 1491
init_graph["Varna"]["Nürnberg"] = 1455
init_graph["Varna"]["Stuttgart"] = 1561
init_graph["Varna"]["Frankfurt am Main"] = 1733
init_graph["Varna"]["Bonn"] = 1779
init_graph["Varna"]["Köln"] = 1775
init_graph["Varna"]["Düsseldorf"] = 1814
init_graph["Varna"]["Dortmund"] = 1770
init_graph["Varna"]["Nantes"] = 2329
init_graph["Varna"]["Vilnius"] = 1290

init_graph["Plovdiv"]["Dortmund"] = 1648

'-------SWITZERLAND-------'

init_graph["Zürich"]["Bern"] = 95
init_graph["Zürich"]["Geneva"] = 224
init_graph["Zürich"]["Warszawa"] = 1038
init_graph["Zürich"]["Kraków"] = 877
init_graph["Zürich"]["Wrocław"] = 734
init_graph["Zürich"]["Gdańsk"] = 1043
init_graph["Zürich"]["Milan"] = 217
init_graph["Zürich"]["Venice"] = 361
init_graph["Zürich"]["Bologna"] = 385
init_graph["Zürich"]["Florence"] = 454
init_graph["Zürich"]["Rome"] = 684
init_graph["Zürich"]["Napoli"] = 856
init_graph["Zürich"]["Bari"] = 958
init_graph["Zürich"]["Palermo"] = 1086
init_graph["Zürich"]["Catania"] = 1222
init_graph["Zürich"]["București"] = 1393
init_graph["Zürich"]["Sofia"] = 1276
init_graph["Zürich"]["Varna"] = 1571
init_graph["Zürich"]["Zagreb"] = 602
init_graph["Zürich"]["Pula"] = 497
init_graph["Zürich"]["Split"] = 739
init_graph["Zürich"]["Hannover"] = 563
init_graph["Zürich"]["Hamburg"] = 695
init_graph["Zürich"]["Berlin"] = 669
init_graph["Zürich"]["Dresden"] = 564
init_graph["Zürich"]["Nürnberg"] = 297
init_graph["Zürich"]["Stuttgart"] = 163
init_graph["Zürich"]["München"] = 242
init_graph["Zürich"]["Frankfurt am Main"] = 306
init_graph["Zürich"]["Bonn"] = 389
init_graph["Zürich"]["Köln"] = 413
init_graph["Zürich"]["Düsseldorf"] = 447
init_graph["Zürich"]["Nantes"] = 761
init_graph["Zürich"]["Paris"] = 476
init_graph["Zürich"]["Marseille"] = 516
init_graph["Zürich"]["Nice"] = 425
init_graph["Zürich"]["Vilnius"] = 1417
init_graph["Zürich"]["Bilbao"] = 1005
init_graph["Zürich"]["Barcelona"] = 835
init_graph["Zürich"]["Valencia"] = 1137
init_graph["Zürich"]["Madrid"] = 1247
init_graph["Zürich"]["Málaga"] = 1592
init_graph["Zürich"]["Seville"] = 1627
init_graph["Zürich"]["Lisbon"] = 1725

init_graph["Geneva"]["Warszawa"] = 1263
init_graph["Geneva"]["Venice"] = 487
init_graph["Geneva"]["Florence"] = 484
init_graph["Geneva"]["Rome"] = 696
init_graph["Geneva"]["Napoli"] = 884
init_graph["Geneva"]["Palermo"] = 1058
init_graph["Geneva"]["Catania"] = 1218
init_graph["Geneva"]["București"] = 1568
init_graph["Geneva"]["Sofia"] = 1422
init_graph["Geneva"]["Split"] = 852
init_graph["Geneva"]["Hamburg"] = 863
init_graph["Geneva"]["Berlin"] = 877
init_graph["Geneva"]["München"] = 464
init_graph["Geneva"]["Frankfurt am Main"] = 462
init_graph["Geneva"]["Düsseldorf"] = 561
init_graph["Geneva"]["Nantes"] = 597
init_graph["Geneva"]["Paris"] = 411
init_graph["Geneva"]["Toulouse"] = 471
init_graph["Geneva"]["Nice"] = 294
init_graph["Geneva"]["Bilbao"] = 786
init_graph["Geneva"]["Barcelona"] = 636
init_graph["Geneva"]["Valencia"] = 919
init_graph["Geneva"]["Madrid"] = 1022
init_graph["Geneva"]["Málaga"] = 1371
init_graph["Geneva"]["Seville"] = 1402
init_graph["Geneva"]["Lisbon"] = 1501

'-------ITALY-------'

init_graph["Milan"]["Turin"] = 131
init_graph["Milan"]["Genoa"] = 119
init_graph["Milan"]["Venice"] = 245
init_graph["Milan"]["Bologna"] = 200
init_graph["Milan"]["Florence"] = 250
init_graph["Milan"]["Rome"] = 477
init_graph["Milan"]["Napoli"] = 658
init_graph["Milan"]["Bari"] = 785
init_graph["Milan"]["Palermo"] = 887
init_graph["Milan"]["Catania"] = 1014
init_graph["Milan"]["București"] = 1333
init_graph["Milan"]["Timișoara"] = 943
init_graph["Milan"]["Cluj"] = 1125
init_graph["Milan"]["Zagreb"] = 535
init_graph["Milan"]["Rijeka"] = 421
init_graph["Milan"]["Zadar"] = 510
init_graph["Milan"]["Split"] = 603
init_graph["Milan"]["Nantes"] = 846
init_graph["Milan"]["Paris"] = 640
init_graph["Milan"]["Lyon"] = 359
init_graph["Milan"]["Toulouse"] = 651
init_graph["Milan"]["Marseille"] = 387
init_graph["Milan"]["Nice"] = 254
init_graph["Milan"]["Vilnius"] = 1535
init_graph["Milan"]["Bilbao"] = 992
init_graph["Milan"]["Zaragoza"] = 923
init_graph["Milan"]["Barcelona"] = 725
init_graph["Milan"]["Valencia"] = 1029
init_graph["Milan"]["Madrid"] = 1189
init_graph["Milan"]["Murcia"] = 1191
init_graph["Milan"]["Málaga"] = 1495
init_graph["Milan"]["Seville"] = 1548
init_graph["Milan"]["Lisbon"] = 1683

init_graph["Turin"]["Genoa"] = 124
init_graph["Turin"]["Venice"] = 367
init_graph["Turin"]["Bologna"] = 295
init_graph["Turin"]["Florence"] = 318
init_graph["Turin"]["Rome"] = 524
init_graph["Turin"]["Napoli"] = 712
init_graph["Turin"]["Bari"] = 864
init_graph["Turin"]["Palermo"] = 906
init_graph["Turin"]["Catania"] = 1044
init_graph["Turin"]["București"] = 1452
init_graph["Turin"]["Zadar"] = 616
init_graph["Turin"]["Paris"] = 583
init_graph["Turin"]["Vilnius"] = 1642
init_graph["Turin"]["Barcelona"] = 606
init_graph["Turin"]["Valencia"] = 912
init_graph["Turin"]["Madrid"] = 1063
init_graph["Turin"]["Málaga"] = 1375
init_graph["Turin"]["Seville"] = 1425

init_graph["Genoa"]["Venice"] = 290
init_graph["Genoa"]["Bologna"] = 195
init_graph["Genoa"]["Florence"] = 198
init_graph["Genoa"]["Rome"] = 401
init_graph["Genoa"]["Napoli"] = 589
init_graph["Genoa"]["Bari"] = 744
init_graph["Genoa"]["Palermo"] = 791
init_graph["Genoa"]["Catania"] = 927
init_graph["Genoa"]["București"] = 1368
init_graph["Genoa"]["Paris"] = 706
init_graph["Genoa"]["Toulouse"] = 604
init_graph["Genoa"]["Barcelona"] = 646

init_graph["Venice"]["Bologna"] = 131
init_graph["Venice"]["Florence"] = 204
init_graph["Venice"]["Rome"] = 394
init_graph["Venice"]["Napoli"] = 534
init_graph["Venice"]["Bari"] = 605
init_graph["Venice"]["Palermo"] = 817
init_graph["Venice"]["Catania"] = 913
init_graph["Venice"]["București"] = 1087
init_graph["Venice"]["Timișoara"] = 699
init_graph["Venice"]["Cluj"] = 881
init_graph["Venice"]["Nantes"] = 1084
init_graph["Venice"]["Paris"] = 846
init_graph["Venice"]["Lyon"] = 584
init_graph["Venice"]["Toulouse"] = 891
init_graph["Venice"]["Marseille"] = 602
init_graph["Venice"]["Nice"] = 452
init_graph["Venice"]["Vilnius"] = 1373
init_graph["Venice"]["Bilbao"] = 1235
init_graph["Venice"]["Zaragoza"] = 1153
init_graph["Venice"]["Barcelona"] = 935
init_graph["Venice"]["Valencia"] = 1238
init_graph["Venice"]["Madrid"] = 1416
init_graph["Venice"]["Málaga"] = 1701
init_graph["Venice"]["Seville"] = 1763
init_graph["Venice"]["Lisbon"] = 1918

init_graph["Bologna"]["Florence"] = 81
init_graph["Bologna"]["Rome"] = 304
init_graph["Bologna"]["Napoli"] = 470
init_graph["Bologna"]["Bari"] = 586
init_graph["Bologna"]["Palermo"] = 721
init_graph["Bologna"]["Catania"] = 839
init_graph["Bologna"]["București"] = 1169
init_graph["Bologna"]["Timișoara"] = 794
init_graph["Bologna"]["Cluj"] = 991
init_graph["Bologna"]["Zagreb"] = 394
init_graph["Bologna"]["Osijek"] = 588
init_graph["Bologna"]["Paris"] = 839
init_graph["Bologna"]["Lyon"] = 529
init_graph["Bologna"]["Toulouse"] = 802
init_graph["Bologna"]["Marseille"] = 496
init_graph["Bologna"]["Nice"] = 452
init_graph["Bologna"]["Barcelona"] = 822
init_graph["Bologna"]["Valencia"] = 1121
init_graph["Bologna"]["Madrid"] = 1313
init_graph["Bologna"]["Málaga"] = 1583
init_graph["Bologna"]["Seville"] = 1653
init_graph["Bologna"]["Lisbon"] = 1815

init_graph["Florence"]["Rome"] = 276
init_graph["Florence"]["Napoli"] = 409
init_graph["Florence"]["Bari"] = 548
init_graph["Florence"]["Palermo"] = 653
init_graph["Florence"]["Catania"] = 770
init_graph["Florence"]["Nantes"] = 1068
init_graph["Florence"]["Paris"] = 885
init_graph["Florence"]["Lyon"] = 553
init_graph["Florence"]["Toulouse"] = 794
init_graph["Florence"]["Marseille"] = 477
init_graph["Florence"]["Bilbao"] = 1143
init_graph["Florence"]["Barcelona"] = 796
init_graph["Florence"]["Madrid"] = 1288
init_graph["Florence"]["Seville"] = 1617
init_graph["Florence"]["Lisbon"] = 1790

init_graph["Rome"]["Napoli"] = 189
init_graph["Rome"]["Bari"] = 374
init_graph["Rome"]["Palermo"] = 427
init_graph["Rome"]["Catania"] = 538
init_graph["Rome"]["București"] = 1137
init_graph["Rome"]["Timișoara"] = 830
init_graph["Rome"]["Cluj"] = 1040
init_graph["Rome"]["Zagreb"] = 535
init_graph["Rome"]["Osijek"] = 535
init_graph["Rome"]["Zadar"] = 338
init_graph["Rome"]["Split"] = 360
init_graph["Rome"]["Nantes"] = 1258
init_graph["Rome"]["Paris"] = 1106
init_graph["Rome"]["Lyon"] = 748
init_graph["Rome"]["Toulouse"] = 927
init_graph["Rome"]["Montpellier"] = 729
init_graph["Rome"]["Marseille"] = 603
init_graph["Rome"]["Nice"] = 473
init_graph["Rome"]["Vilnius"] = 1704
init_graph["Rome"]["Bilbao"] = 1270
init_graph["Rome"]["Barcelona"] = 859
init_graph["Rome"]["Valencia"] = 1117
init_graph["Rome"]["Madrid"] = 1364
init_graph["Rome"]["Málaga"] = 1546
init_graph["Rome"]["Seville"] = 1657
init_graph["Rome"]["Lisbon"] = 1864

init_graph["Napoli"]["Bari"] = 220
init_graph["Napoli"]["Palermo"] = 313
init_graph["Napoli"]["Catania"] = 386
init_graph["Napoli"]["București"] = 1047
init_graph["Napoli"]["Cluj"] = 1003
init_graph["Napoli"]["Zagreb"] = 563
init_graph["Napoli"]["Rijeka"] = 487
init_graph["Napoli"]["Pula"] = 451
init_graph["Napoli"]["Split"] = 344
init_graph["Napoli"]["Nantes"] = 1445
init_graph["Napoli"]["Paris"] = 1291
init_graph["Napoli"]["Lyon"] = 937
init_graph["Napoli"]["Toulouse"] = 1103
init_graph["Napoli"]["Marseille"] = 782
init_graph["Napoli"]["Nice"] = 659
init_graph["Napoli"]["Bilbao"] = 1441
init_graph["Napoli"]["Barcelona"] = 1015
init_graph["Napoli"]["Valencia"] = 1257
init_graph["Napoli"]["Madrid"] = 1513
init_graph["Napoli"]["Málaga"] = 1678
init_graph["Napoli"]["Seville"] = 1784
init_graph["Napoli"]["Lisbon"] = 2007

init_graph["Bari"]["Palermo"] = 450
init_graph["Bari"]["Catania"] = 432
init_graph["Bari"]["București"] = 837
init_graph["Bari"]["Timișoara"] = 632
init_graph["Bari"]["Cluj"] = 832
init_graph["Bari"]["Paris"] = 1425
init_graph["Bari"]["Lyon"] = 1098
init_graph["Bari"]["Toulouse"] = 1301
init_graph["Bari"]["Marseille"] = 976
init_graph["Bari"]["Barcelona"] = 1227
init_graph["Bari"]["Valencia"] = 1478
init_graph["Bari"]["Madrid"] = 1730
init_graph["Bari"]["Seville"] = 2006

init_graph["Palermo"]["Catania"] = 167
init_graph["Palermo"]["București"] = 1286
init_graph["Palermo"]["Nantes"] = 1559
init_graph["Palermo"]["Paris"] = 1487
init_graph["Palermo"]["Lyon"] = 1084
init_graph["Palermo"]["Toulouse"] = 1155
init_graph["Palermo"]["Marseille"] = 864
init_graph["Palermo"]["Nice"] = 784
init_graph["Palermo"]["Barcelona"] = 1023
init_graph["Palermo"]["Valencia"] = 1182
init_graph["Palermo"]["Madrid"] = 1465
init_graph["Palermo"]["Lisbon"] = 1954

init_graph["Catania"]["București"] = 1206
init_graph["Catania"]["Cluj"] = 1254
init_graph["Catania"]["Nantes"] = 1738
init_graph["Catania"]["Paris"] = 1628
init_graph["Catania"]["Lyon"] = 1252
init_graph["Catania"]["Toulouse"] = 1344
init_graph["Catania"]["Marseille"] = 1045
init_graph["Catania"]["Nice"] = 955
init_graph["Catania"]["Vilnius"] = 2062
init_graph["Catania"]["Kaunas"] = 2051
init_graph["Catania"]["Bilbao"] = 1650
init_graph["Catania"]["Zaragoza"] = 1452
init_graph["Catania"]["Barcelona"] = 1190
init_graph["Catania"]["Valencia"] = 1368
init_graph["Catania"]["Madrid"] = 1652
init_graph["Catania"]["Murcia"] = 1424
init_graph["Catania"]["Málaga"] = 1727
init_graph["Catania"]["Seville"] = 1856
init_graph["Catania"]["Lisbon"] = 2120
