
class Solution(object):
    def flatten(self, l, a):
        for i in l:
            if isinstance(i, list):
                self.flatten(i, a)
            else:
                a.append(i)
        return a

    def merge(self, a, b):
        i = j = k = 0
        t =[]
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                t.append(a[i])
                i+=1
            else:
                t.append(b[j])
                j+=1

        while i < len(a):
            t.append(a[i])
            i+=1

        while j < len(b):
            t.append(b[j])
            j+=1

        return t

    def pushToZero(self, arr, n):
        count = 0
        for i in range(0, n):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1
        while count < n:
            arr[count] = 0
            count += 1
        return arr

    def printIntegerVertically(self, i):
        r = i % 10
        if r == 0:
            return
        else:
            self.printIntegerVertically(int(i/10))
        print(r)

    def reverseTheInteger(self, i):
        r = 0
        while i != 0:
            r *= 10
            r += i%10
            i = int(i/10)
        return r

    def maxSubArraySum(self, a):
        max_so_far = a[0]
        curr_max = a[0]

        currStartIndex = 0
        maxStartIndex = 0
        maxEndIndex = 0

        for i in range(1, len(a)):
            curr_max = max(a[i], curr_max+a[i])
            if curr_max > max_so_far:
                max_so_far = curr_max
                maxStartIndex = currStartIndex
                maxEndIndex = i

            if curr_max < 0:
                currStartIndex = i+1

        print("Max SubArray starts at "+str(maxStartIndex)+ " and ends at "+ str(maxEndIndex)+" and the sum is "+str(max_so_far))

    def findMissingNumbers(self, nums):
        for n in nums:
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        return [i + 1 for i, n in enumerate(nums) if n > 0]

    def subset_sum(self, numbers, target, partial=[]):

        s = sum(partial)

        if s == target:
            print("(%s)=%s" % (partial, target))
        if s >= target:
            return

        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i + 1:]
            self.subset_sum(remaining, target, partial + [n])

    def two_sum(self, nums, target):
        nums_hash = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_hash:
                return [nums_hash[target - nums[i]], i]
            nums_hash[nums[i]] = i

    def subarraySum_EqualsK_Count(self, nums, k):
        d, count, sum = {0: 1}, 0, 0
        for n in nums:
            sum += n
            if sum-k in d:
                count+= d[sum-k]
            d[sum] = d.get(sum, 0)+1
        return count

    def subarraySum_EqualsK(self, nums, k):
        d, count, sum = {0: 1}, 0, 0
        for n in nums:
            sum += n
            if sum-k in d:
                return True
            d[sum] = d.get(sum, 0)+1
        return False

    def checkSubarraySum_MultipleOfK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {0: -1}
        t = 0
        for i in range(len(nums)):
            t += nums[i]
            temp = t % k if k else t
            if temp in d and i - d[temp] > 1:
                return True
            if temp not in d:
                d[temp] = i
        return False


if __name__=='__main__':
    s = Solution()
    # To push all the zeroes to the right.
    arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    n = len(arr)
    print(s.pushToZero(arr, n))

    # To flatten a list of lists
    print(s.flatten([[[1, [1,1, [3, [4,5,]]]], 2, 3], [4, 5],6], []))

    # To merge two lists
    a = [1, 7, 9, 10, 14, 17, 20, 22]
    b = [2, 3, 4, 6, 8, 11, 15, 21]

    print(s.merge(a, b))

    # To print an integer vertically
    s.printIntegerVertically(1234)

    # To reverse an integer
    print(s.reverseTheInteger(12345))

    s.maxSubArraySum([-2, -3, 4, -1, -2, 1, 5, -3])
    s.maxSubArraySum([-3, -2, -1, -5])

    a = [4, 3, 2, 7, 8, 2, 3, 1]
    print(s.findMissingNumbers(a))

    s.subset_sum([1, 2, 3, 9, 8, 4, 5, 7, 10], 13)

    a = [2, 7, 11, 15]
    target = 9
    print(s.two_sum(a, target))

    arr = [23, 2, 4, 6, 7]
    target = 6
    print(s.subarraySum_EqualsK_Count(arr, target))

    arr = [23, 2, 6, 4, 7]
    target = 6
    print(s.subarraySum_EqualsK_Count(arr, target))

    arr = [23, 2, 4, 6, 7]
    target = 7
    print(s.subarraySum_EqualsK(arr, target))

    arr = [23, 2, 6, 4, 7]
    target = 6
    print(s.subarraySum_EqualsK(arr, target))

    arr = [23, 2, 4, 6, 7]
    target = 6
    print(s.checkSubarraySum_MultipleOfK(arr, target))

    arr = [23, 2, 6, 4, 7]
    target = 6
    print(s.checkSubarraySum_MultipleOfK(arr, target))