class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        1. Push char into the stack. If matched, poped.
        2. Key Observation:
            The substring between leftover indexes are all valid parenthesis that were poped in the last step. Therefore, we have
            the length of the valid parenthesis.
        3. Take max length by iterate over the leftover stacks.
        """
        
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if (len(stack) > 0 and s[stack[-1]] == '('):
                    stack.pop(-1)
                else:
                    stack.append(i)
        if (len(stack) == 0):
            return len(s)
        else:
            stack.append(len(s))
            stack = [-1] + stack
            max_len = 0
            for i in range(1, len(stack)):
                max_len = max(max_len, stack[i] - stack[i - 1] - 1)
            return max_len

sol = Solution()
print(sol.longestValidParentheses("())"))
