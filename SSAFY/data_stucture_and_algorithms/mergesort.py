def merge_sort(m):
    if len(m)<=1:
        return m
    mid=len(m)//2
    l=m[:mid]
    r=m[mid:]
    l=merge_sort(l)
    r=merge_sort(r)
    return merge(l,r)

def merge(l,r):
    result=[]
    while(len(l)>0 and len(r)>0):
        if l[0]<=r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))
    if len(l)>0:
        result+=l
    else:
        result+=r
    return result

print(merge_sort([69,10,30,2,16,8,31,22]))