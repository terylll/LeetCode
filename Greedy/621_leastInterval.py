class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        freq = [0 for i in range(26)]
        for i in tasks:
            freq[ord(i) - ord('A')] += 1
        
        freq.sort(reverse=True)

        length = len(tasks)

        count = 0
        p = 0
        res = 0
        while count < len(tasks):
            intervals = (freq[p] - 1) * (n + 1) + 1
            res += intervals
            print("Intervals: %d" % intervals)
            while count < len(tasks):
                freq[p] -= 1
                intervals -= 1
                count += 1
                if (freq[p] == 0):
                    p += 1
                print(p, intervals, count, freq)
        return res



sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B"], 2))
        