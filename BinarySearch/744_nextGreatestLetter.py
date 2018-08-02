class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        n = len(letters)
        l = 0
        r = n

        while (l < r):
            mid = (l + r) / 2
            if (letters[mid] > target):
                r = mid
            else:
                # letters[mid] <= target
                l = mid + 1
        
        return letters[l % len(letters)]



sol = Solution()
print(sol.nextGreatestLetter(["c", "f", "j"], "g"))