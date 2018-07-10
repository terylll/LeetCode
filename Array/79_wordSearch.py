"""
Link: https://leetcode.com/problems/word-search/description/
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = self.search(board, i, j, word)
                if (res):
                    return True
        
        return False



    def search(self, board, i, j, word):

        # Base Case
        if (len(word) == 0):
            return True

        if ( i < 0 or i >= len(board) or j < 0 or j >= len(board[0])):
            return False

        # print("i = %d, j = %d, c = %c, word = %s" % (i, j, board[i][j], word))
        if (board[i][j] == word[0]):
            board[i][j] = ""
            word = word[1:]
        else:
            return False

        return self.search(board, i + 1, j, word) or self.search(board, i, j+1, word) or self.search(board, i-1, j, word) or self.search(board, i, j-1, word)


# board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
board = [
    'a', 'a'
]

sol = Solution()
print(sol.exist(board, "aaa"))