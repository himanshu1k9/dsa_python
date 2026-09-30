# Find minimum
nums = [3, 8, 2, 9, 4, 7]

def find_min(num):
    minEle = num[0]
    for ele in num:
        if ele < minEle:
            minEle = ele
    return minEle

print(find_min(nums))

# Two sum
nums = [3, 2, 4]
target = 6

def two_sum(num, target):
    result = []
    for  i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                result.append(i)
                result.append(j)
    return result

print(two_sum(nums, target))

# Optimisation [ Hash map ] in python dictionary do these
def two_sum_optimized(nums, target):
    seen = {}
    for i in range(len(nums)):
        if target - nums[i] in seen:
            return [seen[target - nums[i]] , i]
        seen[nums[i]] = i
    return []

print(two_sum_optimized(nums, target))