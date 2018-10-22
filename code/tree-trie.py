#!/usr/bin/env python3
##-------------------------------------------------------------------
##  @copyright 2018 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: trie.py
## Author : Denny <https://www.dennyzhang.com/contact>
## Description :
## --
## Created : <2018-07-16>
## Updated: Time-stamp: <2018-07-16 22:44:26>
##-------------------------------------------------------------------
## Blog link: https://code.dennyzhang.com/add-and-search-word-data-structure-design
## Basic Ideas: Trie tree. Search with dfs or backtracking
##              TrieNode: children
##     search doesn't necessarily means startswith
##     If add you "word" and "words", then ask you whether "word" exists. You should say True
## Complexity: Time O(n), Space O(n), n how many nodes in the Trie Tree

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.mysearch(word, self.root)

    def mysearch(self, word, node):
        if len(word) == 0:
            # if node.is_word is False, we get a prefix, instead of a match.
            return node.is_word is True

        ch = word[0]
        if ch != '.':
            if ch not in node.children:
                return False
            return self.mysearch(word[1:], node.children[ch])
        else:
            for child in node.children.values():
                if self.mysearch(word[1:], child) is True:
                    return True
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
