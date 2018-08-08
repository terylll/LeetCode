class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        # Find the first down

        path = []
        res = []

        while (N > 0):
            path.append(N % 10)
            N /= 10


        # Two Pointer
        begin = None
        end = None
        for i in range(len(path) - 1):
            if (path[i] < path[i + 1]):
                # Found the first down
                begin = i
                end = i + 1
                break
        print(path, begin, end)

        # Find 
        if (begin and end):
            while(end < len(path) and path[end] == path[begin + 1]):
                end += 1
                
            for i in range(begin + 1, end):
                path[i] -= 1
        
        power = 1
        res = 0
        for i in path:
            res += i * power
            power *= 10
        return res

sol = Solution()
print(sol.monotoneIncreasingDigits(1232))


                
                

                
                
                