import sys
class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        self.helper(S, 0, res)
        return res

    
    def helper(self, S, start, res):
        if (len(res) > 2 and start >= len(S)):
            return True
        
        for i in range(start, len(S)):
            if (S[start] == '0' and i > idx):
                break;

            num = long(S[start: i + 1])
            if (num > sys.maxint):
                print(num)
                break;
            
            size = len(res)
            if (size >= 2 and num > res[-1] + res[-2]):
                break
            
            if (size <= 1 or num == res[-1] + res[-2]):
                res.append(int(num))
                # branch pruning. if one branch has found fib seq, return true to upper call
                if (self.helper(S, i + 1, res) is True):
                    return True
                res.pop(-1)
        
        return False

sol = Solution()
print(sol.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))