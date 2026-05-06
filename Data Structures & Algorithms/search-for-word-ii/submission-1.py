class Node:
    def __init__(self, val=None, word=None):
        self.val = val
        self.word = word
        self.children = {}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node(c)
                curr = curr.children[c]
            curr.word = word

        COMPASS = (
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        )

        res = []

        def backtrack(i, j, node):
            c = board[i][j]
            child = node.children.get(c)
            if child is None:
                return
            if child.word is not None:
                res.append(child.word)
                child.word = None

            board[i][j] = "#"
            for di, dj in COMPASS:
                if 0 <= i+di < len(board) and 0 <= j+dj < len(board[0]) and board[i+di][j+dj] != "#":
                    backtrack(i+di, j+dj, child)
            board[i][j] = c


        for i in range(len(board)):
            for j in range(len(board[i])):
                backtrack(i, j, root)

        return res
