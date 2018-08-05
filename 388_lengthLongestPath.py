class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        """
        Define (s, p) as the relative path 's' in depth 'p'

        Time: O(n)
        Space: O(n)
        """

        stack = [("", 0)]
        stack_len = 0
        max_len = 0

        for path in input.split('\n'):
            path_strip = path.lstrip('\t')
            depth = len(path) - len(path_strip)
            
            while(len(stack) != 0 and stack[-1][1] >= depth):
                temp = stack.pop()
                stack_len -= len(temp[0])
            
            stack.append((path_strip, depth))
            stack_len += len(path_strip)

            if ('.' in path_strip and path_strip.index('.') != len(path_strip) - 1 and stack_len + len(stack) - 1 > max_len):
                # Add '\' to length
                max_len = stack_len + len(stack) - 1

            # print("Stack: %s, length: %d, max_len: %d" % ([i[0] for i in stack], stack_len, max_len))

        return max_len

    def lengthLongestPath2(self, input):
        
        for path in input.split('\n'):

            

sol = Solution()
sol.lengthLongestPath("a\n\tb\n\t\tc.txt\n\taaaa.txt")
