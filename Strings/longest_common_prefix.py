class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

        return prefix


words = ["flower", "flow", "flight"]

obj = Solution()
print(obj.longestCommonPrefix(words))
