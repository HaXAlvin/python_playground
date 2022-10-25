# uva-146 ID Codes

def find_next(data): # time cost: O(n) + O(n) = O(n)
    length = len(data)
    if length == 1:
        return None
    for i in range(length-1,0,-1): # max O(n)
        if data[i-1] >= data[i]:
            continue
        bigger = i
        for j in range(i+1,length): # max O(n)
            if data[bigger] >= data[j] > data[i-1]:
                bigger = j
        return data[:i-1]+data[bigger]+data[:bigger:-1]+data[i-1]+data[bigger-1:i-1:-1]
    return None


while((data := input()) != "#"):
    print(find_next(data) or "No Successor")
