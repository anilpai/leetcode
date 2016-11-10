from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree , TreeNode

'''
Needs Python 3+
'''


class Solution(object):
    '''
    Create a double tree of a given Tree.
    Insert the duplicate as the left child of the original node.
    '''

    def doubleTree(self, root):
        if root is None:
            return
        self.doubleTree(root.left)
        self.doubleTree(root.right)

        oldLeft = root.left
        root.left = TreeNode(root.val)
        root.left.left = oldLeft


if __name__ == '__main__':
    s = Solution()
    print(s.doubleTree(deserialize('[1,2,3,null,null,4,null,5,6]')))
    # drawtree(deserialize('[1,2,3,null,null,4,null,5,6]'))
    # drawtree(deserialize('[1,2,3,null,null,4,null,5,6]'))
    # print(s.isSymmetric(deserialize('[1,2,2,3,4,4,3]')))
    # drawtree(deserialize('[1,2,2,3,4,4,3]'))
    # print(s.isSymmetric(deserialize('[1,2,2,null,3,null,3]')))
    # drawtree(deserialize('[1,2,2,null,3,null,3]'))
