from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree


class Solution(object):
    def printPaths(self, root, s):
        if root is None:
            return
        s.append(root)
        if root.left is None and root.right is None:
            self.printPath(s)
        else:
            self.printPaths(root.left, s)
            self.printPaths(root.right, s)
        s.pop()

    def printPath(self, s):
        s_value = [i.val for i in s]
        print(s_value)
        print(sum(s_value))


if __name__ == '__main__':
    s = Solution()
    s.printPaths(deserialize('[1,2,3,null,null,4,null,6,5]'), [])
    drawtree(deserialize('[1,2,3,null,null,4,null,6,5]'))
    s.printPaths(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'), [])
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
    s.printPaths(deserialize(
        '[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7,2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'), [])
    drawtree(deserialize(
        '[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7,2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
