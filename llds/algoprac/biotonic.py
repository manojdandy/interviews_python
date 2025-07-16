def biotonic(nums:list) -> int:
    left = 0
    n = len(nums)
    right = n-1
    while left <= right:
        mid = left + (right - left)//2
        if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == n-1 or nums[mid] > nums[mid+1]):
            return nums[mid]
        elif mid == 0 or nums[mid] > nums[mid-1]:
            left = mid + 1
        else:
            right = mid - 1
    return -1



if __name__ == '__main__':
    print(biotonic([1, 2, 4, 5, 7, 8, 3])) #8