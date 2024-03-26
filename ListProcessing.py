"""
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for j in range(len(nums)):
        if j+1 > len(nums):
            break

        if (nums[j] + nums[j+1]) == target:
            return j, j+1

        for k in range(len(nums)):
            if j == k:
                continue
            if (nums[j] + nums[k]) == target:
                return j, k

def twoSum1(nums, target):
    prevMap = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return

nums = [0,4,3,0]
target = 0
print("nums=", nums, "target=", target, "twoSum=",twoSum(nums, target))
print("nums=", nums, "target=", target, "twoSum1=",twoSum1(nums, target))

nums = [2,7,11,15]
target = 9
print("nums=", nums, "target=", target, "twoSum=",twoSum(nums, target))

nums = [3,2,4]
target = 6
print("nums=", nums, "target=", target, "twoSum=",twoSum(nums, target))

nums = [3,3]
target = 6
print("nums=", nums, "target=", target, "twoSum=",twoSum(nums, target))

nums = [2,5,7,11,15]
target = 9
print("nums=", nums, "target=", target, "twoSum=",twoSum(nums, target))

nums = [3,2,3]
target = 6
print("nums=", nums, "target=", target, "twoSum=",twoSum(nums, target))
