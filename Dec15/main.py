import heapq


def parse(fp):
    for line in fp:
        line = line.rstrip('\n')
        yield [int(x) for x in line]


def dijkstra(adjacent, start, end):
    dist = {start: 0}

    q = [(0, start)]

    heapq.heapify(q)

    while q:
        cost, u = heapq.heappop(q)
        if cost <= dist[u]:
            for v, weight in adjacent(u):
                alt = cost + weight
                if v not in dist or alt < dist[v]:
                    dist[v] = alt
                    heapq.heappush(q, (alt, v))

    return dist[end]


def part1(inputData):
    board = list(parse(open(inputData)))
    m = len(board)
    n = len(board[0])

    def adjacent(u):
        i, j = u
        for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ii < m and 0 <= jj < n:
                yield (ii, jj), board[ii][jj]

    result = dijkstra(adjacent, (0, 0), (m - 1, n - 1))
    print(result)


def part2(inputData):
    board = list(parse(open(inputData)))
    mm, nn = len(board), len(board[0])
    m, n = 5 * mm, 5 * nn

    def add_wrap(c, idx):
        return (c - 1 + idx) % 9 + 1

    def adjacent(u):
        i, j = u
        for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ii < m and 0 <= jj < n:
                weight = add_wrap(board[ii % mm][jj % nn], ii // mm + jj // nn)
                yield (ii, jj), weight

    result = dijkstra(adjacent, (0, 0), (m - 1, n - 1))
    print(result)


if __name__ == "__main__":
    input_data = "./data.txt"
    # part1(input_data)
    part2(input_data)

    # source: Zealousideal-Pen9091 from https://www.reddit.com/r/adventofcode/comments/rgqzt5/2021_day_15_solutions/
