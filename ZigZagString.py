class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        len_Str = len(s)
        outList = [len_Str]
        col = 1
        numberOfEmptyCols = numRows - 2
        ctr = 0
        sCtr = 0
        for row in range(1 , numRows+1): #numRows = 3
            if col % numberOfEmptyCols == 0:
                pass
            else:
                outList[ctr] = s[sCtr]
                ctr = ctr + 1
