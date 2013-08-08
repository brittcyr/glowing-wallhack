

def count_t(arr, lo, hi):
    count = 0
    arr = frozenset(arr)
    for t in xrange(lo, hi + 1):
        for a in arr:
            if (t - a) in arr:
                count += 1
                break
        if not t % 100:
            print t
    print count

arr = [0] * 1000000
ind = 0
for row in open('2sum.txt'):
    arr[ind] = int(row)
    ind += 1

arr.sort()
count_t(arr, -10000, 10000)


import heapq

X = [int(l) for l in open('Median.txt')]
H_low  = []
H_high = []

sum = 0
for x_i in X:
  if len(H_low) > 0:
    if x_i > -H_low[0]:
      heapq.heappush(H_high, x_i)
    else:
      heapq.heappush(H_low, -x_i)
  else:
    heapq.heappush(H_low, -x_i)

  if len(H_low) > len(H_high) + 1:
    heapq.heappush(H_high, -(heapq.heappop(H_low)))
  elif len(H_high) > len(H_low):
    heapq.heappush(H_low, -(heapq.heappop(H_high)))

  sum += -H_low[0]

print sum % 10000
