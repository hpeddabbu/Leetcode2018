class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J=list(J)
        S=list(S)
        sum =0
        for each in J:
            sum=sum + S.count(each)
            
        return sum