from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree , TreeNode

'''
Needs Python 3+
'''


class Solution(object):
    '''
    Level order traversal of the tree (Breadth First Search)
    '''

    def printLevelOrder(self, root):

        if root is None:
            return

        q = []

        q.append(root)

        while len(q) > 0:

            # print the first value in q and pop the same.
            print(q[0].val, end=' ')
            node = q.pop(0)

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)


if __name__ == '__main__':
    s = Solution()
    s.printLevelOrder(deserialize('[1,2,3,null,null,4,null,5,6]'))
    drawtree(deserialize('[1,2,3,null,null,4,null,5,6]'))
    s.printLevelOrder(deserialize('[1,2,2,3,4,4,3]'))
    drawtree(deserialize('[1,2,2,3,4,4,3]'))
    s.printLevelOrder(deserialize('[1,2,2,null,3,null,3]'))
    drawtree(deserialize('[1,2,2,null,3,null,3]'))
