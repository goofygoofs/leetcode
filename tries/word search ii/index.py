'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''

'''
loop through all nodes
    if that first letter is equal to any of those in word,:
        we add options left right up down to go, but not previously traversed
        go through and if entire word, then add it to set

remember to remove banned position when backtracking

time O(m*n*c) m,n,c are row, length and # of characters in a word
space is O(c) # of char for trie

'''
from typing import List, Set, Tuple


class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rowCount = len(board)
        if rowCount == 0 or len(words) == 0:
            return []
        colCount = len(board[0])

        root = Trie()
    
        for word in words:
            self.createTrie(word, root)

        output = set()


        for i in range(rowCount):
            for j in range(colCount):
                char = board[i][j]
                if char in root.children:
                    start = (i, j)
                    banned = {start}
                    self.find(board, root.children[char], start, banned, output)

        return output

    def find(self, board: List[List[str]], root: Trie, start: Tuple[int], banned: Set[int], output: Set[str]) -> None:
        i, j = start[0], start[1]
        left, right, up, down = j-1, j+1, i-1, i+1
        rowCount = len(board)
        colCount = len(board[0])
        if root.isWord:
            output.add(root.word)

        if left >= 0:
            pos = (i, left)
            char = board[i][left]
            if pos not in banned and char in root.children:
                banned.add(pos)
                self.find(board, root.children[char], pos, banned, output)
                banned.remove(pos)
        if right < colCount:
            pos = (i, right)
            char = board[i][right]
            if pos not in banned and char in root.children:
                banned.add(pos)
                self.find(board, root.children[char], pos, banned, output)
                banned.remove(pos)
        if up >= 0:
            pos = (up, j)
            char = board[up][j]
            if pos not in banned and char in root.children:
                banned.add(pos)
                self.find(board, root.children[char], pos, banned, output)
                banned.remove(pos)
        if down < rowCount:
            pos = (down, j)
            char = board[down][j]
            if pos not in banned and char in root.children:
                banned.add(pos)
                self.find(board, root.children[char], pos, banned, output)   
                banned.remove(pos)

    def createTrie(self, word: str, root: Trie):
        for char in word:
            if char not in root.children:
                root.children[char] = Trie()
            root = root.children[char]
        root.isWord = True
        root.word = word
