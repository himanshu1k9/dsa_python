// Hash Map using array

let list = [2,3,4];
let target = 6;

function two_sum(list, target) {
    let seen = [];
    for(let i = 0; i < list.length; i++) {
        let complement = target - list[i];
        if(complement in seen) {
            return [seen[complement], i];
        }
        seen[list[i]] = i;
    }
    return []
}

console.log(two_sum(list, target))

// two pointers only for soeted array
let nums = [1, 2, 3, 4, 6, 8, 10];
let target_sum1 = 10

function target_sum(num, target_sum) {
    let left = 0;
    let right = nums.length - 1;
    while(left < right) {
        let sum = num[left] + num[right];
        if(sum > target_sum) {
            right--;
        } else if(sum < target_sum) {
            left++;
        } else {
            return [left, right]
        }
    }
    return [];
}

console.log(target_sum(nums, target_sum1))

// # Valid Palindrom Leet code 125
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let cleaned = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();

    let left = 0;
    let right = cleaned.length - 1;

    while(left < right) {
        if(cleaned[left] == cleaned[right]) {
            left++;
            right--;
        } else {
            return false;
        }
    }
    return true;
};

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let arr = nums.sort((a, b) => a - b);
    let res = [];
    for(let i = 0; i < arr.length - 2; i++) {
        if(i > 0 && nums[i] === nums[i - 1]) continue;

        let left = i + 1;
        let right = arr.length - 1;

        while(left < right) {
            let sum = arr[i] + arr[left] + arr[right];
            if(sum === 0) {
                res.push([nums[i], nums[left], nums[right]]);

                while(left < right && nums[left] === nums[left + 1]) left++;
                while(left < right && nums[right] === nums[right - 1]) right--;

                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    return res;
};