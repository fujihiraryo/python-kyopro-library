class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, i):
        j = i
        while self.parent[j] != j:
            j = self.parent[j]
        return j

    def unite(self, i, j):
        i0, j0 = self.find(i), self.find(j)
        if i0 > j0:
            i0, j0 = j0, i0
        self.parent[j0] = i0
