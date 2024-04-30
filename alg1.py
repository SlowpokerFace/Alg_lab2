import time

repeats = 10
time_amounts = [0]*13
for _ in range(repeats):


    for tmp in range(13):
        begin = time.time()
        rectangles = []
        n = 2 ** tmp
        for i in range(0, 2 * n, 2):
            rectangles.append([[10 * i, 10 * i], [10 * (2 * n - i), 10 * (2 * n - i)]])
        m = 10000
        k = 0
        for j in range(m):
            x = (2999*j)**31 % (n*20)
            y = (5323 * j) ** 31 % (n * 20)
            for i in rectangles:
                if i[0][0] <= x < i[1][0] and i[0][1] <= y < i[1][1]:
                    k += 1
        end = time.time()
        time_amounts[tmp] += end-begin
for i in time_amounts:
    i /=repeats
print(time_amounts)
