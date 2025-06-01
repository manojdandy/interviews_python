from typing import List
def twoSum(nums:List[int],target:int)-> List[int]:
    l = 0
    r = len(nums) - 1

    while l < r:
        currSum = nums[l] + nums[r]
        if currSum > target:
            r -= 1
        elif currSum < target:
            l += 1
        else:
            return [l+1,r+1]
    return []

if __name__ == "__main__":
    print(twoSum([3,2,4],6))