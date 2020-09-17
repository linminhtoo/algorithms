# https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_r=internal-search
def countMergeSort(arr,start,end):
    if start >= end: return (0, arr[start:end + 1])
    
    if start == end - 1:
        # simpler case to avoid one recursive call
        if arr[start] > arr[end]:
            return (1, [arr[end],arr[start]])
        else:
            return (0, arr[start:end + 1])
    
    mid = (start + end) // 2
    
    lSwaps, lSorted = countMergeSort(arr, start, mid)
    rSwaps, rSorted = countMergeSort(arr, mid + 1,end)
    # swaps in this merge
    mSwaps = 0
    sortedArr = []
    lIndex , rIndex = 0, 0
    while(lIndex < len(lSorted) and rIndex < len(rSorted)):
        if lSorted[lIndex] <= rSorted[rIndex]:
            sortedArr.append(lSorted[lIndex])
            lIndex += 1
        else:
            sortedArr.append(rSorted[rIndex])
            rIndex += 1
            mSwaps += len(lSorted) - lIndex
    
    sortedArr += lSorted[lIndex:]
    sortedArr += rSorted[rIndex:]
    totalSwaps = lSwaps + rSwaps + mSwaps
    # print(totalSwaps, sortedArr)
    return totalSwaps, sortedArr

def count_inversions(a):
    return countMergeSort(a, 0, len(a) - 1)[0]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(count_inversions(arr))