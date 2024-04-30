import bisect
import time

time_amounts = []

for tmp in range(12):
    print(time_amounts)
    begin = time.time()
    rectangles = []
    n = 2 ** tmp
    for i in range(0, 2 * n, 2):
        rectangles.append([[10 * i, 10 * i], [10 * (2 * n - i), 10 * (2 * n - i)]])
    m = 10000
    x_coords = set()
    y_coords = set()
    for rectangle in rectangles:
        x_coords.add(rectangle[0][0])
        x_coords.add(rectangle[1][0])
        y_coords.add(rectangle[0][1])
        y_coords.add(rectangle[1][1])
    x_coords = sorted(list(x_coords))
    y_coords = sorted(list(y_coords))
    x_index = {}
    y_index = {}
    ind = 0
    for i in range(len(x_coords)):
        x_index[x_coords[i]] = ind
        ind += 1
    ind = 0
    for i in range(len(y_coords)):
        y_index[y_coords[i]] = ind
        ind += 1

    map = [[0] * len(y_index) for i in range(len(x_index))]
    for i in rectangles:
        x_max = x_index[i[1][0]]
        y_max = y_index[i[1][1]]
        for x in range(x_index[i[0][0]], x_max):
            for y in range(y_index[i[0][1]], y_max):
                map[x][y] += 1
    m = 10000

    for j in range(m):
        x = (2999 * j) ** 31 % (n * 20)
        y = (5323 * j) ** 31 % (n * 20)
        x = bisect.bisect_right(x_coords, x) - 1
        y = bisect.bisect_right(y_coords, y) - 1
        a = map[x][y]
    end = time.time()
    time_amounts.append(end - begin)
print(time_amounts)
