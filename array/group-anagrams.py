from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for item in strs:
            key = ''.join(sorted(item))
            result[key].append(item)
            
        return list(result.values())