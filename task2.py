import random

def binary_search(ndata, ns):
    mid = 0
    steps = 0
    low = 0
    high = len(ndata) - 1

    while low <= high:
        mid = (high + low) // 2
        steps += 1
        if ndata[mid] < ns :
            low = mid + 1
        elif ndata[mid] >= ns:
            high = mid - 1
        else:
            return mid
    #print(mid, ndata[mid])
    #print(mid if ndata[mid] >= ns else mid + 1)
    return steps, ndata[mid if ndata[mid] >= ns else mid + 1]

if __name__ == "__main__":
    ndata = []
    for i in range(20):
        ndata.append(random.uniform(1,5))
    #ndata.append(3)
    ndata.sort()
    #print(ndata)
    print(binary_search(ndata, 3))
