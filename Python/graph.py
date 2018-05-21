# adj list: {vertex: [(other vertex, weight), ...]}
from pythonds.graphs import PriorityQueue


class Graph():
    def __init__(self, vertices, adj_list):
        self.vertices = vertices
        self.adj = adj_list

    def __str__(self):
        output = "vertices = " + str(self.vertices) + "\n"
        output += "edges = \n"
        for key, value in self.adj.items():
            output += "       " + str(key) + " : " + str(value) + "\n"
        return output

    def number_of_vertices(self):
        return len(self.vertices)

    def contains(self, vertex):
        return vertex in self.vertices

    def dfs(self, start, connected=set()):
        if not self.contains(start):
            return set()
        connected.add(start)
        for y in self.adj[start]:
            if y[0] not in connected:
                connected = connected.union(self.dfs(y[0]), connected)
        return connected

    def bfs(self, start):
        connected = set()
        queue = [start]
        while not queue == []:
            y = queue.pop(0)
            connected.add(y)
            for x in self.adj[y]:
                if x[0] not in connected:
                    queue.append(x[0])
        return connected

    def connected_components(self):
        unvisited = set(self.vertices)
        components = []
        while unvisited != set():
            x = unvisited.pop()
            comp = self.bfs(x)
            components.append(comp)
            unvisited = unvisited.difference(comp)
        return components

    def Dijkstra(self, start):
        # initialize the heap with infinity dist
        pq = PriorityQueue()
        entries = dict([(str(v), float('inf')) for v in self.vertices])
        entries[str(start)] = 0
        pq.buildHeap([(float('inf'), v) for v in self.vertices])
        pq.decreaseKey(start, 0)
        # do the dijkstra step
        while not pq.isEmpty():
            cur = pq.delMin()
            for x in self.adj[cur]:
                dist = entries[str(cur)] + x[1]
                old = entries[str(x[0])]
                if old > dist:
                    entries[str(x[0])] = dist
                    pq.decreaseKey(x[0], dist)
        return entries

    def prims(self, start):
        pq = PriorityQueue()
        entries = dict([(str(v), float('inf')) for v in self.vertices])
        entries[str(start)] = 0
        pq.buildHeap([(float('inf'), v) for v in self.vertices])
        pq.decreaseKey(start, 0)

        new_vertices = []
        new_edges = dict([(x, []) for x in self.vertices])

        last =  dict([(str(x), None) for x in self.vertices])

        while not pq.isEmpty():
            current = pq.delMin()
            new_vertices.append(current)

            clast = last[str(current)]

            if clast:
                new_edges[clast].append(current)


            for v in self.adj[current]:
                dist = v[1]
                old = entries[str(v[0])]
                if old > dist:
                    entries[str(v[0])] = dist
                    last[str(v[0])] = current
                    pq.decreaseKey(v[0], dist)

        return Graph(new_vertices, new_edges)

    def approx_Travelling_Salesman(self):
        mst = self.prims(self.vertices[0])
        stack = [mst.vertices[0]]
        res = []
        while stack != []:
            current = stack.pop()
            res.append(current)
            for x in mst.adj[current][::-1]:
                stack.append(x)
        return res + [self.vertices[0]]



# For connected component and Dijkstra
vertices1 = [1, 2, 3, 4, 5, 6, 7]
adj_List1 = {1: [(2, 2), (3, 4), (4, 1)],
            2: [(1, 2), (3, 1), (5, 2)],
            3: [(1, 4), (2, 1), (7, 1)],
            4: [(1, 1), (7, 2)],
            5: [(2, 2)],
            6: [],
            7: [(4, 2), (3, 1)]}

graph = Graph(vertices1, adj_List1)
print(graph.connected_components())
print(graph.Dijkstra(1))
print(graph)


# For travelling Salesman: graph satisfies triangle inequality

vertices2 = [1, 2, 3, 4, 5]

adj_List2 = {
    1: [(2, 2), (3, 3), (4, 1), (5, 3)],
    2: [(1, 2), (3, 2), (4, 3), (5, 3)],
    3: [(1, 3), (2, 2), (4, 4), (5, 2)],
    4: [(1, 1), (2, 3), (3, 4), (5, 3)],
    5: [(1, 2), (2, 3), (3, 2), (4, 3)]
}

graph2 = Graph(vertices2, adj_List2)
print(graph2)
print(graph2.prims(1))
print(graph2.approx_Travelling_Salesman())
