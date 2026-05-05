class Node:
    def __init__(self, val=0, end=False):
        self.val = val
        self.children = {}
        self.end = end


class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        return True
        