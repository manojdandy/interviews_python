
def reverse_str(s):
    return s[::-1]

def reverse_without_indx(s):
    revr_str=""
    for char in s:
        revr_str = char + revr_str
    return revr_str

def is_palindrome(s):
    s = s.replace(" ","").lower()
    return s == s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count=0
    try:
            for char in s:
                if char in vowels:
                    count = count + 1
            return count
    except Exception as e:
        raise e

def fib_seq(n):
    fib_seq = [0,1]
    for i in range(2,n):
        next_term = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_term)
    return fib_seq

def find_max_ele(nums:list) -> int:
    if not nums:
        raise ValueError("no elements")
    max_ele = nums[0]
    for n in nums:
        if n > max_ele:
            max_ele = n
    return max_ele

def sum_of_digits(nums):
    if not nums:
        raise ValueError("not a valid number")
    sums = 0
    digits = str(nums)
    for digit in digits:
        sums = sums + int(digit)
    return sums

if __name__=="__main__":
    if is_palindrome("A man, a plan, a canal, Panama"):
        print("str is palindrome")
    else:
        print("not palindrome")

    vowels_cnt = f"vowles count :: {str (count_vowels("ram is a good person"))}" 

    print(vowels_cnt)
    print(fib_seq(5))
    print(f"max ele :: {find_max_ele([0,-1,12,0,87])}")


