from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree

'''
Needs Python 3+
'''


class Solution(object):
    '''
    To check for Symmetric Tree.
    '''

    def isSymmetric(self, root):
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)


if __name__ == '__main__':
    s = Solution()
    print(s.isSymmetric(deserialize('[1,2,3,null,null,4,null,5,6]')))
    drawtree(deserialize('[1,2,3,null,null,4,null,5,6]'))
    print(s.isSymmetric(deserialize('[1,2,2,3,4,4,3]')))
    drawtree(deserialize('[1,2,2,3,4,4,3]'))
    print(s.isSymmetric(deserialize('[1,2,2,null,3,null,3]')))
    drawtree(deserialize('[1,2,2,null,3,null,3]'))
