# uva-146 ID Codes


def find_next(data): # time cost: O(n) + O(n) = O(n)
    length = len(data)
    if length == 1:
        return None
    for i in range(length-1,0,-1): # max O(n) i = len -> 0
        if data[i-1] >= data[i]:
            continue
        if i == length-1:
            return data[:-2]+data[-1]+data[-2]
        bigger = i
        for j in range(i+1,length): # max O(n) j = i -> len
            if data[j] > data[i-1] and data[j] <= data[bigger]:
                bigger = j
        return data[:i-1]+data[bigger]+data[:bigger:-1]+data[i-1]+data[bigger-1:i-1:-1]
    return None


while((data := input()) != "#"):
    print(find_next(data) or "No Successor")