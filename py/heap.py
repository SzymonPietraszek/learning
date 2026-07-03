def add(h, a):
    i = len(h)
    h.append(a)
    while i > 0:
        pi = (i - 1) // 2
        if h[pi] > h[i]:
            h[pi], h[i] = h[i], h[pi]
        else:
            break
        i = pi


def pop(h):
    if len(h) == 1:
        return h.pop()
    ret = h[0]
    h[0] = h.pop()
    i = 0
    while True:
        l = 2 * i + 1
        if l >= len(h):
            break
        s = l
        r = 2 * i + 2
        if r < len(h) and h[l] > h[r]:
            s = r
        if h[i] <= h[s]:
            break
        h[i], h[s] = h[s], h[i]
        i = s
    return ret


def print_heap(h):
    step = 1
    for i, v in enumerate(h):
        print(v, end=" ")
        if i + 1 == step:
            print()
            step += 2 * step
    print()


#         0
#       /   \
#      1     2
#     / \   /
#    3   4 5


heap = []

add(heap, 0)
add(heap, 1)
add(heap, 2)
add(heap, 3)
add(heap, 4)
add(heap, 5)

print_heap(heap)
print(pop(heap))
print_heap(heap)

# from heapq import heappop, heappush
