class Anagram:
    def anagram(self,s:str,t:str) -> bool:
        n = len(s)
        if len(s) != len(t):
            return False 
        arr = [0]*26
        for i in range(n):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a') ] -= 1
        for i in range(26):
            if arr[i] != 0:
                return False
        return True


if __name__=='__main__':
    obj = Anagram()
    print(obj.anagram("hello","lleoh"))