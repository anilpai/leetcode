from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree , TreeNode

'''
Needs Python 3+
'''


class Solution(object):
    '''
    Longest Consecutive Sequence .
    '''

    def longestConsecutive(self, root):

        if not root:
            return 0

        self.result = 0
        self.helper(root, 1)

        return self.result

    def helper(self, root, curLen):
        self.result = curLen if curLen > self.result else self.result
        if root.left:
            if root.left.val == root.val + 1:
                self.helper(root.left, curLen + 1)
            else:
                self.helper(root.left, 1)
        if root.right:
            if root.right.val == root.val + 1:
                self.helper(root.right, curLen + 1)
            else:
                self.helper(root.right, 1)

if __name__ == '__main__':
    s = Solution()
    root = deserialize('[1,2,3,null,null,4,null,5,6]')
    print(s.longestConsecutive(root))
    drawtree(deserialize('[1,2,3,null,null,4,null,5,6]'))
    root = deserialize('[2,null,3,2,null,1,null]')
    print(s.longestConsecutive(root))
    drawtree(deserialize('[2,null,3,2,null,1,null]'))

    # s.longestConsecutive(deserialize('[1,2,2,3,4,4,3]'))
    # drawtree(deserialize('[1,2,2,3,4,4,3]'))
    # s.longestConsecutive(deserialize('[1,2,2,null,3,null,3]'))
    # drawtree(deserialize('[1,2,2,null,3,null,3]'))
