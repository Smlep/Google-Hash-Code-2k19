class Graph:

    def __init__(self, slides):
        self.order = len(slides)
        self.adj = []
        for i in range(self.order):
            self.adj.append([])
        self.weights = {}

        for i in range(self.order):
            for j in range(self.order):
                if i != j:
                    w = slides[i] - slides[j]
                    if w > 0:
                        self.adj[i].append(j)
                        self.weights[(i, j)] = w


    def longest(self):
        l = []
        for k in self.weights.keys():
            l.append((k, self.weights[k]))
        l.sort(key = lambda x: x[1])
        vertices = []
        for i in range(self.order - 1):
            if l == []:
                break
            select = l.pop()
            while treeze(vertices, select):
                select = l.pop()
            vertices.append(select)


    def treeze(l, t):
        ex = [0, 0]
        for e in l:
            for en in e:
                if t[0] == en:
                    ex[0] += 1
                if t[1] == en:
                    ex[1] += 1
        return max(ex) < 2

