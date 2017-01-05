from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class Solution(object):
    '''
    Convert Sorted Array into a Binary Search Tree (BST) with minimal height.
    '''

    def array2bst(self, a, min, max):

        if min > max:
            return None

        middle = int((min+max)/2)

        node = TreeNode(a[middle])
        node.left = self.array2bst(a, min, middle-1)
        node.right = self.array2bst(a, middle+1, max)

        return node


if __name__ == '__main__':
    s = Solution()
    a = [3, 4, 5, 6, 7, 8, 9, 10, 12, 13]
    r = s.array2bst(a, 0, len(a)-1)
    drawtree(r)
