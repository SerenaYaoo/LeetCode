class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        
        """
        # first sort by starting position
        intervals.sort(key=lambda x:x[0])
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged





