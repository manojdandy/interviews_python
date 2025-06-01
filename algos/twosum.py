from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items = {}
        indexes = []
        for i,num in enumerate(nums):
            print(f"index : {i} , item : {num}")
            items[num] = i
        for i,num in enumerate(nums):
            search_item = (target - num)
            if search_item in items.keys() and i != items[search_item]:
                indexes.append(i)
                indexes.append(items[search_item])
                break
        return indexes
            


if __name__ == "__main__":
    print("two sum")
    solution = Solution()
    print(solution.twoSum([2,7,11,15],9))
    print(solution.twoSum([3,2,4],6))