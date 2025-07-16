#Given two arrays A = [1,2,3,5,6,9] and 2-d array B = [[0,3],[1,2]]
#Calculate the sum of the elements from array A with index positions mentioned in B. 
#Output = [11, 5]
#Ex, 0 - first index, 3 - last index
#sum(1,2,3,5) = 11
#Its time complexity, and optimised solution.#

def sum(nums:list[int],query:list[list[int]]) -> list[int]:
    res = []
    prefix_sum = [0]*len(nums)
    prefix_sum[0] = nums[0]
    for i in range(1,len(nums)):
        prefix_sum[i] = prefix_sum[i-1] + nums[i]
    

    for q in query:
        start = q[0]
        end = q[1]
        sum = 0
        if start == 0:
            sum += prefix_sum[end]
        else:
            sum = prefix_sum[end] - prefix_sum[start-1]
        res.append(sum)
    return res


if __name__ == "__main__":
    res = sum([1,2,3,5,6,9],[[0,3],[1,2]])
    print(res)