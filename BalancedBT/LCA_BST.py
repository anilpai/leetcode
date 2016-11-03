from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree


'''
Needs Python 3+
'''


class Solution(object):
    '''
    Lowest Common Ancestor (LCA) in a Binary Search Tree (BST)
    '''

    def lca(self, root, n1, n2):

        if root is None:
            return None

        # If n1 & n2 is lesser then lca lies to the left.
        if (n1 < root.val) and (n2 < root.val):
            return self.lca(root.left, n1, n2)

        # If n1 & n2 is greater then lca lies to the right.
        if (n1 > root.val) and (n2 > root.val):
            return self.lca(root.right, n1, n2)

        return root


if __name__ == '__main__':
    s = Solution()
    lca = s.lca(deserialize('[8,4,12,null,null,10,null,null,11]'), 4, 10)
    print(lca.val)
    drawtree(deserialize('[8,4,12,null,null,10,null,null,11]'))
