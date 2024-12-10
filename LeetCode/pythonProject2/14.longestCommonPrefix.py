class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        l = ""
        size = len(strs)
        for i in range(size):
            halfWord = len(strs[i]) // 2  # for prefix
            nextHalfWord = len(strs[i + 1]) // 2  # for prefix
            for j in range(halfWord):
                if i != size - 1 and (strs[i][j] in strs[nextHalfWord]):
                    l += strs[i][j]
                    if i == size - 2:
                        strs.append("NULL")
                        size = len(strs)
        print(l)


strs = list(input())
obj = Solution()
obj.longestCommonPrefix(strs)
