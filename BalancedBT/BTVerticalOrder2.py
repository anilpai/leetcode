from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree


class Solution(object):

    def findMinMax(self, node, mini, maxi, hd):
        if node is None:
            return

        if hd < mini[0]:
            mini[0] = hd

        if hd > maxi[0]:
            maxi[0] = hd

        self.findMinMax(node.left, mini, maxi, hd-1)
        self.findMinMax(node.right, mini, maxi, hd+1)

    def printVertically(self, node, line_num, hd):
        if node is None:
            return

        if hd == line_num:
            print(node.val, end=',')

        self.printVertically(node.left, line_num, hd-1)
        self.printVertically(node.right, line_num, hd+1)

    def verticalOrder(self, root):
        mini = [0]
        maxi = [0]
        self.findMinMax(root, mini, maxi, 0)

        for line_num in range(mini[0], maxi[0]+1):
            print(self.printVertically(root, line_num, 0))

if __name__ == '__main__':
    s = Solution()
    print(s.verticalOrder(deserialize('[1,2,3,null,null,4,null,null,5]')))
    drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))