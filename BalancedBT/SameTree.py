from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree , TreeNode

'''
Needs Python 3+
'''


class Solution(object):
    '''
    To check if both trees are structurally same.
    '''

    def sameTree(self, a, b):

        if a is None and b is None:
            return True

        elif a is not None and b is not None:
            return a.val == b.val and self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right)


if __name__ == '__main__':
    s = Solution()
    print(s.sameTree(deserialize('[1,2,3,null,null,4,null,5,6]'), deserialize('[1,2,3,null,null,4,null,5,6]')))
    drawtree(deserialize('[1,2,3,null,null,4,null,5,6]'))
    print(s.sameTree(deserialize('[1,2,7,null,null,4,null,5,6]'), deserialize('[1,2,3,null,null,4,null,5,6]')))

