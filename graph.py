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

    def dft(self, start, p, score=0):
        calls = []
        p.append(start)
        for e in self.adj[start]:
            if e not in p:
                calls.append(self.dft(e, p.copy(), score + self.weights[(start, e)]))
        if not calls:
            return p, score
        return max(calls, key=lambda x: x[1])

    def longest(self):
        scores = []
        for i in range(self.order):
            scores.append(self.dft(i, []))
        return max(scores, key=lambda x: x[1])
