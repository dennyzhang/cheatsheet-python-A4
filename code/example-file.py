#!/usr/bin/env python3
##-------------------------------------------------------------------
##  @copyright 2018 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: example-file.py
## Author : Denny <https://www.dennyzhang.com/contact>
## Description :
## --
## Created : <2018-07-16>
## Updated: Time-stamp: <2020-02-03 11:06:47>
##-------------------------------------------------------------------
## Blog link: https://code.dennyzhang.com/binary-tree-level-order-traversal
## Baisc Idea: BFS
## Complexity: Time O(n), Space O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None: return []
        res = []
        queue = collections.deque()
        queue.append(root)
        while len(queue) != 0:
            nexts = []
            for i in xrange(len(queue)):
                element = queue.popleft()
                nexts.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            res.append(nexts)
        return res
