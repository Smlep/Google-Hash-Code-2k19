

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
                        self.weights[(i,j)] = w

    def longest(self):
        scores = []
        for i in range(self.order):
            scores.append(dft(self, i))
        return max(calls, key=lambda x: return x[1])

    def dft(self, start, P = [], score = 0):
        calls = []
        for e in self.adj[start]:
            if e not in P:
                calls.append(dft(self, e, (P + [e]).copy(), score + self.weigths[(start, e)]))
        if calls == []:
            return (P, score)
        return max(calls, key=lambda x: return x[1])
