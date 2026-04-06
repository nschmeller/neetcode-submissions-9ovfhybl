class PrefixNode:
    def __init__(self):
        self.chars = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = PrefixNode()


    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.chars:
                curr.chars[c] = PrefixNode()
            curr = curr.chars[c]
        curr.end = True


    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                if word[i] == '.':
                    for cand in curr.chars:
                        if dfs(i+1, curr.chars[cand]):
                            return True
                    return False
                elif word[i] not in curr.chars:
                    return False
                else:
                    curr = curr.chars[word[i]]
            return curr.end
        return dfs(0, self.root)
