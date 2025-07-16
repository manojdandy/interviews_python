##paris_code = ['*#%$', '2345678']
#sample scooter code from above inputs are - '*2', '*3', '*4','*5','*6','*7','*8','#2','#3','#4','#5' and so on.
#uk_code = ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', '-/', '012']
#sample scooter code from above inputs are - 'aa-0', 'aa-1', 'aa-2','aa/0','aa/1','aa/2','ab-0','ab-1','ab-2' and so on.


def helper(codes:list[str],idx:int,result:list[str],path:str,count:int):
    if len(result) >= count:
        return
    if idx == len(codes):
        result.append(path)
        return
    for ch in codes[idx]:
        helper(codes,idx+1,result,path + ch,count)

if __name__ == "__main__":
    result = []
    paris_code = ['*#%$', '2345678']
    helper(paris_code,0,result,"",5)
    print(result)