class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        ln = len(prefix) 
        for s in strs:
            while s[0:ln] != prefix[0:ln]:
                ln -= 1
        return prefix[0:ln]
        