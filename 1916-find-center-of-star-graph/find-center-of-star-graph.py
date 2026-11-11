class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        return list(set(edges[0]) & set(edges[1]))[0]