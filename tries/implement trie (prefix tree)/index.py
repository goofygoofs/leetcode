'''
A trie (pronounced as "try") or prefix root is a root data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith
'''

'''
will be a dictionary of at most 26 keys on the first level of each char of the alphabet
{
    a:
    b:
    c:
    ...
}
insert will go through each char, check if the char in dictionary, if is, then go keep going through until all char added
also we need to add a bool somewhere to check if word is entire word True
remember to go into the root.trie when iterating
prefix doesn't matter if isWord or not
time - O(n) where n is number characters of longest word for insert
    search O(n) for iterating through each char
space - O(n) to build dictionaries for insert
    search is O(1) no space is needed
'''

class Trie:

    def __init__(self):
        self.trie = {}
        self.isWord = False
        

    def insert(self, word: str) -> None:
        root = self.trie
        for i, char in enumerate(word):
            if char not in root:
                root[char] = Trie()
            root = root[char]
            # at last index of word, it is now a complete word
            if i == len(word) - 1:
                root.isWord = True
            else:
                root = root.trie
                
    def search(self, word: str) -> bool:
        root = self.trie
        for i, char in enumerate(word):
            if char not in root:
                return False
            root = root[char]
            # if at last index and is a complete word, then return 
            if i == len(word) - 1:
                return root.isWord
            else:
                root = root.trie        

    def startsWith(self, prefix: str) -> bool:
        root = self.trie
        for i, char in enumerate(prefix):
            if char not in root:
                return False
            root = root[char].trie
            # if i == len(prefix) - 1:
            #     return not root.isWord
            # else:
            #     root = root.trie
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)