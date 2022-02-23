# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        is_exit=False
        for i in range(len(nums)):
            for j in range(len(nums)):
                target_num=nums[i]+nums[j]
                if target_num == target:
                    print(i,j)
                    is_exit=True
            if is_exit is True:
                break


sol = Solution()
nums=[2,7,11,15]
target=9
sol.twoSum(nums,target)
