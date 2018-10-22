#!/usr/bin/env python3
##-------------------------------------------------------------------
##  @copyright 2018 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: bfs.py
## Author : Denny <https://www.dennyzhang.com/contact>
## Description :
## --
## Created : <2018-07-16>
## Updated: Time-stamp: <2018-07-16 22:43:26>
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
            level_elements = []
            for i in xrange(len(queue)):
                element = queue.popleft()
                level_elements.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            res.append(level_elements)
        return res
