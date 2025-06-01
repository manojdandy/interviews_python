def merge_two_list(a,b):
    c=[]
    i = 0
    j = 0
    if not a or not b:
        raise ValueError("please pass proper list")
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
        elif b[j] > a[i]:
            c.append(a[i])
            i += 1
   
    while i < len(a):
        c.append(a[i])
        i+=1

    while j < len(b):
        c.append(b[j])
        j+=1
    return c


if __name__=="__main__":
    a=[]
    b=[2,4,6]
    c = merge_two_list(a,b)
    print(c)