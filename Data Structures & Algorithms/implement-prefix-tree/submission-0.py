class PrefixNode:

    def __init__(self):
        self.chars = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.chars:
                curr.chars[word[i]] = PrefixNode()
            curr = curr.chars[word[i]]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] in curr.chars:
                curr = curr.chars[word[i]]
            else:
                return False
        return curr.end


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] in curr.chars:
                curr = curr.chars[prefix[i]]
            else:
                return False
        return True
