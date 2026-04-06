class Solution:
    class Trie:
        class Node:
            def __init__(self):
                self.children = {}
                self.word = ""


        def __init__(self):
            self.root = self.Node()
        

        def insert(self, word):
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = self.Node()
                curr = curr.children[c]
            curr.word = word


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        COMPASS = (
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1),
        )
        trie = self.Trie()
        for word in words:
            trie.insert(word)
        root = trie.root

        visited = [[False for _ in board[0]] for _ in board]
        present = set()

        def backtrack(i, j, node):
            if node.word:
                present.add(node.word)

            visited[i][j] = True
            for di, dj in COMPASS:
                if i+di >= 0 and i+di < len(board) and j+dj >= 0 and j+dj < len(board[0]) and not visited[i+di][j+dj] and board[i+di][j+dj] in node.children:
                    backtrack(i+di, j+dj, node.children[board[i+di][j+dj]])
            visited[i][j] = False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in root.children:
                    backtrack(i, j, root.children[board[i][j]])
        
        return list(present)
