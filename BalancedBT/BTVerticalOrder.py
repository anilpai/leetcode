from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree

'''
Needs Python 3+
'''
from collections import defaultdict


class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


class Solution(object):
    def verticalOrder(self, root):
        cols = defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]

if __name__ == '__main__':
    s = Solution()
    print(s.verticalOrder(deserialize('[1,2,3,null,null,4,null,null,5]')))
    drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    print(s.verticalOrder(deserialize('[1,2,3,4,5,6,7,null,null,null,null,null,8,null,9]')))
    drawtree(deserialize('[1,2,3,4,5,6,7,null,null,null,null,null,8,null,9]'))
    print(s.verticalOrder(deserialize('[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]')))
    drawtree(deserialize('[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]'))
