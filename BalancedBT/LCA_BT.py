from TreeSerialize.TreeSerialize import deserialize, drawtree


'''
Needs Python 3+
'''


class Solution_old(object):
    '''
    Lowest Common Ancestor (LCA) in a Binary Tree (BT)  : Takes additional space, not space optimized.
    '''

    def findPath(self, root, path, k):
        '''
        A Helper function to make sure that both nodes exist.
        '''
        if root is None:
            return False

        path.append(root.val)

        if root.val == k:
            return True

        # To check if K is found in left or right sub tree.

        if ((root.left is not None) and (self.findPath(root.left, path, k))) or ((root.right is not None) and (self.findPath(root.right, path, k))):
            return True

        # If not present in subtree with root, remove root from path and return False

        path.pop()
        return False

    def lca(self, root, n1, n2):

        # To store the paths to n1 and n2 from the root

        path1 = []
        path2 = []

        # Find path from root to n1 and n2 and if either is not present, return -1

        if (not self.findPath(root, path1, n1) or not self.findPath(root, path2, n2)):
            return -1

        # Compare the paths to get the first different value.

        i = 0

        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]


class Solution(object):
    '''
    Lowest Common Ancestor (LCA) in a Binary Tree (BT)
    '''

    def lca(self, root, p, q):
        if root is None:
            return None

        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)

        if (left and right) or (root in [p, q]):
            return root
        else:
            return left or right


if __name__ == '__main__':

    """ Both p & q must exist. If either of them is null, then the other node is the least common ancestor. """

    old_solution = False

    if old_solution:
        s = Solution_old()
        lca = s.lca(deserialize('[1,2,3,null,null,4,null,5,6]'), 5, 6)
        print(lca)
        drawtree(deserialize('[1,2,3,null,null,4,null,5,6]'))
        print(s.lca(deserialize('[2,1,3,0,7,9,11,12,null,21,20,null,null,38,48,null,null,null,null,17]'), 17, 12))
        drawtree(deserialize('[2,1,3,0,7,9,11,12,null,21,20,null,null,38,48,null,null,null,null,17]'))
        print(s.lca(deserialize('[2,1,3,0,7,9,11,12,null,21,20,null,null,18,28,null,null,null,null,17,22,31,43,0,47,49,51,52,null,61,40,null,null,48,58,null,null,null,null,47]'), 21, 58))
        drawtree(deserialize('[2,1,3,0,7,9,11,12,null,21,20,null,null,18,28,null,null,null,null,17,22,31,43,0,47,49,51,52,null,61,40,null,null,48,58,null,null,null,null,47]'))
    else:
        s1 = Solution()

        # Example 1
        # root = deserialize('[1,2,3,null,null,4,null,5,6]')
        # p = root.right.left.left
        # q = root.right.left.right
        # lca = s1.lca(root, p, q)
        # print(lca)
        # drawtree(deserialize('[1,2,3,null,null,4,null,5,6]'))

        # Example 2
        root = deserialize('[2,1,3,0,7,9,11,12,null,21,20,null,null,38,48,null,null,null,null,17]')
        p = root.left.left.left
        q = root.left.right.right.left
        lca = s1.lca(root, p, q)
        print(lca)
        drawtree(deserialize('[2,1,3,0,7,9,11,12,null,21,20,null,null,38,48,null,null,null,null,17]'))

