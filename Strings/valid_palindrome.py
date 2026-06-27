class Solution:
    def isPalindrome(self, s):
        filtered = ""

        for ch in s:
            if ch.isalnum():
                filtered += ch.lower()

        return filtered == filtered[::-1]


obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))
