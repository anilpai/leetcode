from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree


class Solution(object):
    def hasPathSum(self, root, sum, k):
        if root is None:
            return False

        sum += root.val

        if sum > k:
            return False
        elif sum == k and not root.left and not root.right:
            return True
        else:
            return self.hasPathSum(root.left, sum, k) or self.hasPathSum(root.right, sum, k)


if __name__ == '__main__':
    s = Solution()
    print(s.hasPathSum(deserialize('[1,2,3,null,null,4,null,6,5]'), 0, 13))
    drawtree(deserialize('[1,2,3,null,null,4,null,6,5]'))
    print(s.hasPathSum(deserialize('[1,2,3,null,null,4,null,6,5]'), 0, 15))
    drawtree(deserialize('[1,2,3,null,null,4,null,6,5]'))
    print(s.hasPathSum(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'), 0, 11))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
    print(s.hasPathSum(deserialize(
        '[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7,2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'), 0, 25))
    drawtree(deserialize(
        '[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7,2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
