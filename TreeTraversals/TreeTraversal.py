from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree


'''
Needs Python 3+
'''


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class Solution(object):
    def inOrder(self, root):
        '''
        :param root:
        :return:
        '''
        if root is not None:
            self.inOrder(root.left)
            print(root.val)
            self.inOrder(root.right)

    def preOrder(self, root):
        '''

        :param root:
        :return:
        '''
        if root is not None:
            print(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        '''

        :param root:
        :return:
        '''
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.val)


if __name__ == '__main__':
    s = Solution()
    print(" # Pre Order #")
    s.preOrder(deserialize('[1,2,3,null,null,4,null,null,5]'))
    print(" # In Order #")
    s.inOrder(deserialize('[1,2,3,null,null,4,null,null,5]'))
    print(" # Post Order #")
    s.postOrder(deserialize('[1,2,3,null,null,4,null,null,5]'))
    drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))