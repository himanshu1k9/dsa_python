# Two Pointers

# Only for sorted array LeetCode Problem #167
nums = [1, 2, 3, 4, 6, 8, 10]
target = 10

def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum > target:
            right -= 1
        elif sum < target:
            left += 1
        else:
            return [left, right]
    return []

print(two_sum_sorted(nums, target))

# submitted leet code
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            if current_sum > target:
                right -= 1

            elif current_sum < target:
                left += 1

            else:
                return [left + 1, right + 1]

        return []

# String palindrom check
str = 'hello'
def check_palindrome(str):
    left = 0
    right = len(str) - 1
    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

print(check_palindrome(str))

import re

def is_palindrome(str):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', str).lower()
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] == cleaned[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

str = "A man, a plan, a canal: Panama"
print(is_palindrome(str))

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                
                    left += 1
                    right -= 1
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res