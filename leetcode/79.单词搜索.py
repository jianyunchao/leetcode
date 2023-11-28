from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 从每一个点出发
        res = False
        for i, j in enumerate(board):
            for x, y in enumerate(j):
                res = self.dfs(i, x, 0, word, board)
                if res:
                    return True
        return res

    def dfs(self, row, col, index, w, board):
        # 结束条件
        print(row, col, index)
        if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0 or index >= len(w):
            return False
        print(board[row][col])
        if w[index] != board[row][col]:
            return False
        if index == len(w) - 1:
            return True
        board[row][col] = ''
        # 做选择
        res = self.dfs(row + 1, col, index + 1, w, board) or \
              self.dfs(row - 1, col, index + 1, w, board) or \
              self.dfs(row, col + 1, index + 1, w, board) or \
              self.dfs(row, col - 1, index + 1, w, board)
        board[row][col] = w[index]
        return res


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    s = Solution()
    print(s.exist(board, word))
