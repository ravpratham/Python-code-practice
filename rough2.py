class Solution(object):
    def __init__(self,s):
        self.s = s

    def lengthOfLongestSubstring(self, s):
        self.s = s
        l = []
        for i in self.s:
            if i not in l:
                l.append(i)
        answer = len(l)
        return answer
s = input()
solution1 = Solution(s)
print(solution1.lengthOfLongestSubstring(s))