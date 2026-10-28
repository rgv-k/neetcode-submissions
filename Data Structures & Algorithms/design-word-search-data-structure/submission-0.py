class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()

            node = node.children[ch]
        
        node.is_end = True

    def search(self, word: str) -> bool:
        def helper(node, index):
            if index == len(word):
                return node.is_end

            ch = word[index]
            if  ch != '.':
                if ch not in node.children:
                    return False
                
                return helper(node.children[ch], index + 1)

            for char in node.children:
                child_node = node.children[char]
                if helper(child_node, index + 1): return True

            return False


        return helper(self.root, 0)
class Node:
    def __init__(self):
        self.is_end = False
        self.children = {}