class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        flag = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                flag = self.bt(board, i, j, word, 0)
                print("Flag = %s" % flag)
                if (flag == True):
                    return flag;

        return flag
    
    def bt(self, board, x, y, word, start):
        if (start == len(word)):
            # print("Found.")
            return True
        
        if (x < 0 or x == len(board) or y < 0 or y == len(board[0])):
            return False
        
        if (board[x][y] != word[start]):
            return False
        
        print("board(%d, %d) = %c, start = %c" % (x, y, board[x][y], word[start]))
        temp = board[x][y]
        board[x][y] = None
        flag = self.bt(board, x - 1, y, word, start + 1) or self.bt(board, x + 1, y, word, start + 1) or self.bt(board, x, y - 1, word, start + 1) or self.bt(board, x, y + 1, word, start + 1)
        board[x][y] = temp
        return flag

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]]

sol = Solution()
print(sol.exist(board, "ABCCED"))