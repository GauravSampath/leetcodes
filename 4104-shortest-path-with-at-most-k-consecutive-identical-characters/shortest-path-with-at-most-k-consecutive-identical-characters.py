class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, labels[v], w))
        dist = {}
        dist[(0, 1, labels[0])] = 0
        heap = [(0, 0, 1, labels[0])]
        while heap:
            d, u, cons, last = heapq.heappop(heap)
            if u == n - 1:
                return d
            for v, c, w in g[u]:
                newd = d + w
                newcons = cons + 1
                if c != last:
                    newcons = 1
                if newcons > k:
                    continue
                if newd < dist.get((v, newcons, c), float('inf')):
                    dist[(v, newcons, c)] = newd
                    heapq.heappush(heap, (newd, v, newcons, c))
        return -1