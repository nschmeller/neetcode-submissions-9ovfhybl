class Node:
    def __init__(self, val=0, end=False):
        self.val = val
        self.end = end
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        
        curr.end = True

    def search(self, word: str) -> bool:
        return self.helper(word, self.root)


    def helper(self, word, node):
        curr = node

        for i, c in enumerate(word):
            if c == ".":
                return any(self.helper(word[i+1:], curr.children[child]) for child in curr.children)
            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]

        return curr.end
