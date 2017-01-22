from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class Solution(object):
    def isBalanced(self, root):
        '''
        :param root:
        :return: True if balanced, False if not balanced.
        '''
        return self.balancedHeight(root) >= 0

    def balancedHeight(self, root):
        '''
        :param root:
        :return:
        '''
        if not root:
            return 0
        left = self.balancedHeight(root.left)
        right = self.balancedHeight(root.right)
        if left < 0 or right < 0:
            return -1
        if left - right > 1 or right - left > 1:
            return -1
        return max(left, right) + 1


if __name__ == '__main__':
    s = Solution()
    print(s.isBalanced(deserialize('[1,2,3,null,null,4,null,null,5]')))
    drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    print(s.isBalanced(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
    print(s.isBalanced(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7,2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7,2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
