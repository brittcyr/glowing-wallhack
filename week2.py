compares = 0

def qsort(l):
    global compares
    if len(l) <= 1:
        return l
    else:
        first = l[0]
        

        y = first

        if y == first:
            lesser, equal, greater = partition(l[1:], [], [first], [])
        #if y == last:
        #    lesser, equal, greater = partition(l[:-1], [], [last], [])
        #if y == mid:
         #   lesser, equal, greater = partition(list[:mid] + list[mid+1:], [], [mid], [])

        #compares += len(l) - 1
        return qsort(lesser) + equal + qsort(greater)

def partition(lst, l, e, g):
    while lst != []:
        global compares
        compares += 1
        p = lst.pop()
        if p < e[0]:
            l = [p] + l
        else:
            g = [p] + g
    return (l, e, g)

arr = []
f = open('QuickSort.txt')
for line in f:
    arr.append(int(line))

qsort(arr)
print compares

