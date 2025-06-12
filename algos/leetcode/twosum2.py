from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       elements = {}
       indexes=[]
       for i,n in enumerate(nums):
            elements[n] = i


       for i, n in enumerate(nums):
            if target-n in elements and elements[target-n] !=i:
                indexes.append(i)
                indexes.append(elements[target-n])

       return indexes


