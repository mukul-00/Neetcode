class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Brue Forece solution
        # s1 = s[::-1]
        # if(s == s1):
        #     return True
        # return False

        # better solution
        # newStr = ""
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]

        # optimal solution (for interview)
        l, r = 0, len(s) - 1

        while l < r:
            # to ignore spaces, special char and other symbols
            while l < r and not self.alphaNum(s[l]):
                l = l + 1
            while r > l and not self.alphaNum(s[r]):
                r = r - 1
                
            if s[l].lower() != s[r].lower():
                return False
            
            l = l + 1
            r = r - 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
    

if __name__ == "__main__":
    sol = Solution()

    s = "A man, a plan, a canal: Panama"
    result = sol.isPalindrome(s)

    print(result)