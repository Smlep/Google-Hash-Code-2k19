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

    def treeze(self, l, t):
        ex = [0, 0]
        for e in l:
            for en in e:
                if t[0] == en:
                    ex[0] += 1
                if t[1] == en:
                    ex[1] += 1
        return max(ex) > 1 or (t[1], t[0]) in l


    def construct(self, conn, vertices):
        l = [-1] * self.order
        for s, e in vertices:
            if l[s] == -1:
                l[s] = e
            else:
                l[e] = s
        path = []
        i = 0
        while i in l:
            i += 1
        M = [i]
        l.append(i)
        while len(M) < self.order:
            if l[i] == -1:
                a = 0
                while a in l:
                    a += 1
                l[i] = a
            path.append(i)
            i = l[i]
            M.append(i)
        return path



    def longest(self):
        l = []
        for k in self.weights.keys():
            l.append((k, self.weights[k]))
        l.sort(key=lambda x: x[1])
        vertices = []

        for i in range(self.order - 1):
            if not l:
                break
            select = l.pop()[0]
            while self.treeze(vertices, select):
                if not l:
                    break
                select = l.pop()[0]
            vertices.append(select)
        conn = [0] * self.order
        for e in vertices:
            conn[e[0]] += 1
            conn[e[1]] += 1
        res = self.construct(conn, vertices)
        return res
