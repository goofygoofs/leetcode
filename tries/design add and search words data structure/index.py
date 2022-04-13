'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.
'''

'''
the issue here is the period dot. that means we have to iterate through every char for every period which is (26 * # of periods)
otherwise it's the same as the Trie
at most 3 dots so it's not so bad it's only 26*3 so it's constant
actually not constant because 1,000,000 chars * 26 * 26 * 26 will be 17.5 billion operations

so we need dfs and if it's "." character, we dfs through the children.values() # which are Tries
pass in index and current Trie as parameters to dfs
also dfs (i + 1, child)
we are passing i, not index

O(n * 26^3) time
O(n) space for dictionary
'''


class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie()
            cur = cur.children[char]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def helper(index: int, root: Trie):
            cur = root
            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    for child in cur.children.values(): # child is a Trie
                        if helper(i + 1, child):
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            return cur.isWord
        
        return helper(0, self.root)





# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)