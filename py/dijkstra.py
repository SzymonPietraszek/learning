def dijkstra(g, start):
    d = {v: 999999 for v in g}
    d[start] = 0
    vs = list(g.keys())
    while vs:
        min_i = min(range(len(vs)), key=lambda i: d[vs[i]])
        m = vs.pop(min_i)
        for n, c in g[m]:
            d[n] = min(d[n], d[m] + c)
    return d


print(
    dijkstra(
        {
            0: [(1, 1), (2, 4)],
            1: [(0, 1), (2, 2), (3, 6)],
            2: [(0, 4), (1, 2), (3, 3)],
            3: [(1, 6), (2, 3)],
        },
        0,
    )
)
