class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

        d =collections.defaultdict(list)
        
        d["".join(sorted(s))].append(sorted(t))
        if len(list(d.values()))==2:
            return true
        """
        return (collections.Counter(s))==(collections.Counter(t))
            
        