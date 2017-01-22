from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class Solution(object):
    def checkBST(self, root):
        '''
        Min-Max Solution.
        '''
        return self.checkedBST(root, None, None)

    def checkedBST(self, root, mini, maxi):
        if root is None:
            return True
        if (mini is not None and root.val <= mini) or (maxi is not None and root.val >= maxi):
            return False
        if (not self.checkedBST(root.left, mini, root.val)) or (not self.checkedBST(root.right, root.val, maxi)):
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.checkBST(deserialize('[20,10,30,5,15,null,null,3,7,null,17]')))
    drawtree(deserialize('[20,10,30,5,15,null,null,3,7,null,17]'))
    print(s.checkBST(deserialize('[1,2,3,null,null,4,null,null,5]')))
    drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    print(s.checkBST(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
    print(s.checkBST(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7,2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7,2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
