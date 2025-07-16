## # Input: ["row", "a", "wor", "test", "ttes", "tset"]
# # Output: [["row", "wor"], ["a"], ["test", "ttes", "tset"]

from collections import defaultdict

def groupAnagram(input:list) -> list[list]:
    mp = defaultdict(list)
    for word in input:
        arr = [0]*26
        for ch in word:
            arr[ord(ch) - ord('a')] += 1
        mp[tuple(arr)].append(word)
    print(mp) 

    return mp.values()


if __name__=='__main__':
    lst = groupAnagram(["row", "a", "wor", "test", "ttes", "tset"])
    print(lst)