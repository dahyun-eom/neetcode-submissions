class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x != y:
                heapq.heappush_max(stones, x-y)
        if len(stones) ==1:
            return stones[0]
        else:
            return 0

    #####################################################
    # class Solution:
    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     stones = [-s for s in stones]
    #     heapq.heapify(stones)

    #     while len(stones) > 1:
    #         x = -heapq.heappop(stones)
    #         y = -heapq.heappop(stones)

    #         if x != y:
    #             heapq.heappush(stones, -(x - y))

    #     return -stones[0] if stones else 0
        
        