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

    def height(self, root):
        '''
        Returns the height of the Tree.
        '''
        if root is None:
            return -1
        return max(self.height(root.left), self.height(root.right))+1

    def diameter(self, tree):
        '''
        Returns the diameter of the Tree.
        '''
        if tree is None:
            return -1

        # Find the Height of Left SubTree & Right SubTree
        lheight = self.height(tree.left)
        rheight = self.height(tree.right)

        # Find the Diameter of the Left SubTree & Right SubTree
        ldiameter = self.diameter(tree.left)
        rdiameter = self.diameter(tree.right)

        # The root must be counted twice to get the final diameter
        return max(lheight+rheight+2, max(ldiameter, rdiameter))


if __name__ == '__main__':
    s = Solution()
    print("Height : " + str(s.height(deserialize('[1,2,3,null,null,4,null,null,5]'))))
    print("Diameter : " + str(s.diameter(deserialize('[1,2,3,null,null,4,null,null,5]'))))
    drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    print("Height : " + str(s.height(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))))
    print("Diameter : " + str(s.diameter(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
    print("Height : " + str(s.height(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7,2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))))
    print("Diameter : " + str(s.diameter(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7,2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7,2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))

    print("Height : " + str(s.height(deserialize('[1,2,3,4,5,null,null,6,7,8,9,10,null,null,null,null,null,null,11,null,12,null,null]'))))
    print("Diameter : " + str(s.diameter(deserialize('[1,2,3,4,5,null,null,6,7,8,9,10,null,null,null,null,null,null,11,null,12,null,null]'))))
    drawtree(deserialize('[1,2,3,4,5,null,null,6,7,8,9,10,null,null,null,null,null,null,11,null,12,null,null]'))