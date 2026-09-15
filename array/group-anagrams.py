from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen = defaultdict(list)
        result = []

        for item in strs:
            curr = ''.join(sorted(item))
            if curr in seen:
                seen[curr].append(item)
            else:
                seen[curr] = [item]
        return list(seen.values())
        

        