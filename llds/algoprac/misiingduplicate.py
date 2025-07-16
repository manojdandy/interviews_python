#nput: arr[] = {3, 1, 3}
#Output: 3, 2
def swap(arr:list,i:int,j:int):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def missing_dup(nums:list[int]) -> tuple[int,int]:
    items = []
    for i,num in enumerate(nums):
        if i != nums[i]-1:
            swap(nums,i,nums[i]-1)
    
    for i,num in enumerate(nums):
        if i != nums[i]-1:
            items.append(nums[i])
            items.append(i+1)
    return (items[0],items[1])


if __name__ == "__main__":
    print(missing_dup([3, 1, 3]))