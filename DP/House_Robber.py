'''

N houses to rob and security system will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non - negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

'''


'''

Rob2 : This time, all houses at this place are arranged in a circle.

'''


'''
Rob3 :  "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.
'''


import random
from TreeSerialize.TreeSerialize import serialize, deserialize, drawtree, TreeNode

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # f(0) = nums[0]
        # f(1) = max(num[0], num[1])
        # f(k) = max( f(k-2) + nums[k], f(k-1) )

        last, now = 0, 0

        for i in nums:
            last, now = now, max(last + i, now)

        return now

    def rob2(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob(nums[1:]), self.rob(nums[:-1]))

    def rob3(self, root):
        '''
        :type root: TreeNode
        :return: int
        '''
        def robHelper(root):
            if not root:
                return (0,0)
            left, right = robHelper(root.left), robHelper(root.right)
            return root.val + left[1] + right[1], max(left)+max(right)
        return max(robHelper(root))


if __name__=='__main__':
    s = Solution()
    ll = random.sample(range(100), 20)
    print ll
    print s.rob(ll)
    print s.rob2(ll)
    print s.rob3(deserialize('[3,2,3,null,3,null,1]'))
    print s.rob3(deserialize('[3,4,5,1,3,null,1]'))