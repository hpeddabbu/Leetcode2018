class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        
        s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

        
        """
        dic = collections.defaultdict(list)
        for s in strs:
            """sorted(s)== eat==['e','a','t']"""
            dic["".join(sorted(s))].append(s)
        return list(dic.values())
        
        