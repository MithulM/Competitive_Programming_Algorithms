from sys import maxsize


class Ford_Folkerson:
    def __init__(self, size: int, s: int, t: int):
        self.size = size
        self.source = s
        self.sink = t

        self.capacity = [[0] * size for _ in range(size)]
        self.seen = [False] * size

    def addEdge(self, i: int, j: int, c: int) -> None:
        self.capacity[i][j] = c

    def run(self):
        total = 0
        sent = -1
        while sent != 0:
            self.seen = [False] * self.size
            sent = self.dfs(self.source, maxsize * 2 + 1)
            total += sent
        return total

    def dfs(self, i: int, amount: int):
        if i == self.sink:
            return amount
        self.seen[i] = True
        for j in range(self.size):
            if self.capacity[i][j] and not self.seen[j]:
                sent = self.dfs(j, min(amount, self.capacity[i][j]))
                if sent > 0:
                    self.capacity[i][j] -= sent
                    self.capacity[j][i] += sent
                    return sent
        return 0
