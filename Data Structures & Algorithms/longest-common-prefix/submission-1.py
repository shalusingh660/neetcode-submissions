class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first = strs[0]
        for i in range(len(first)):
            for word in strs:
                if(len(word)<=i or word[i]!=first[i]):
                    return first[:i]
        return first       



        