"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        import heapq
        n = len(intervals)
        if n == 0 or n == 1:
            return n
        
        heap = []
        count = 1
        intervals.sort(key = lambda x: x.start)
        heapq.heappush(heap, intervals[0].end)

        for i in range(1, n):
            start = intervals[i].start
            end = intervals[i].end
            if heap[0] > start:
                count += 1
            else:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        
        return count