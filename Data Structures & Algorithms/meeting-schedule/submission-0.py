"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        import heapq
        
        n = len(intervals)
        if n == 0 or n == 1:
            return True

        heap = []
        intervals.sort(key = lambda x: x.start)
        heapq.heappush(heap, intervals[0].end)

        for i in range(1, n):
            start, end = intervals[i].start, intervals[i].end
            if heap[0] > start:
                return False
            heapq.heappop(heap)
            heapq.heappush(heap, end)
        
        return True

