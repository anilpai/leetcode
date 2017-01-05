class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = []
        self.words_count = 0
        self.is_word = False

    def get_child(self, char):
        for child in self.children:
            if child.char == char:
                return child
        return None


class Trie(object):
    def __init__(self):
        # token root char
        self.root = TrieNode("*")

    def add(self, word):
        curr = self.root
        for c in word:
            next_node = curr.get_child(c)
            if next_node is None:
                next_node = TrieNode(c)
                curr.children.append(next_node)
            next_node.words_count += 1
            curr = next_node
        curr.is_word = True

    def find(self, prefix):
        curr = self.root
        for c in prefix:
            next_node = curr.get_child(c)
            if next_node is None:
                return 0
            curr = next_node

        return curr.words_count


if __name__ == '__main__':
    t = Trie()
    t.add('and')
    t.add('andy')
    print(t.find('an'))