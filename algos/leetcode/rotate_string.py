class RotateString:
    def __init__(self,name):
        self.name = name
    def is_string_rotated(self,a:str,b:str) -> bool:
        print(f" function call :: {self.name}")

        pass

    def rotate(self,a:str,k:int) -> str:
        i = len(a)-1
        j = i-k
        b = a[:j+1]
        while i > j:
            b = a[i] + b
            i -= 1
        return b

if __name__ == "__main__":
    rs = RotateString("check is another string rotated string?")
    print(rs.rotate("abcde",3))
    print(rs.is_string_rotated("abcde","cdeab"))
