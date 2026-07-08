class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        counter = Counter(nums)

        h = []

        for num, freq in counter.items():   
            heapq.heappush(h, (-freq, num))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(h)[1])

        return result
