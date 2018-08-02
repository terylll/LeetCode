class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        
        l = 0
        r = len(letters) - 1

        while (l < r):
            mid = (l + r) / 2
            if (letters[mid] <= target):
                l = mid + 1
            else:
                r = mid
        
        if (l == len(letters) - 1):
            return letters[0]

        return letters[l] 

sol = Solution()
print(sol.nextGreatestLetter(["c", "f", "j"], "g"))