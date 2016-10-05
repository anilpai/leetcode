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

        curr = root
        s = []
        done = None

        while not done:
            if curr is not None:
                s.append(curr)
                curr = curr.left
            else:
                if len(s) > 0:
                    curr = s.pop()
                    print(curr.val)
                    curr = curr.right
                else:
                    done = True

    def preOrder(self, root):
        pass

    def postOrder(self, root):
        pass


if __name__ == '__main__':
    s = Solution()
    print(" # In Order #")
    s.inOrder(deserialize('[1,2,3,null,null,4,null,null,5]'))