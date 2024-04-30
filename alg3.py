import bisect
import time


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Event:
    def __init__(self, x=0, y_start=0, y_end=0, state=1):
        self.x = x
        self.y_start = y_start
        self.y_end = y_end
        self.state = state


repeats = 10
time_amounts = [0] * 13

for _ in range(repeats):
    for tmp in range(13):
        begin = time.time()
        rectangles = []
        n = 2 ** tmp
        for i in range(0, 2 * n, 2):
            rectangles.append([[10 * i, 10 * i], [10 * (2 * n - i), 10 * (2 * n - i)]])

        y_coords = []
        x_coords = []
        for rectangle in rectangles:
            y_coords.append(rectangle[0][1])
            y_coords.append(rectangle[1][1])
            x_coords.append(rectangle[0][0])
            x_coords.append(rectangle[1][0])

        events = []
        for i in rectangles:
            events.append(Event(i[0][0], i[0][1], i[1][1], 1))
            events.append(Event(i[1][0], i[0][1], i[1][1], -1))
        events.sort(key=lambda x: x.x)


        def build_segment_tree(arr, start, end):
            if start + 1 == end:
                # print(Node(arr[start]),1)
                return Node(arr[start])

            mid = (start + end) // 2
            left_child = build_segment_tree(arr, start, mid)
            right_child = build_segment_tree(arr, mid, end)

            node = Node(0)
            node.left = left_child
            node.right = right_child
            # print(node,2)
            return node


        x_set = sorted(x_coords)
        y_set = sorted(list(set(y_coords)))


        def add(state, left, right, curr_left, curr_right, node):
            if curr_left >= left and curr_right <= right:
                return Node(node.value + state, node.left, node.right)
            if curr_left >= right or curr_right <= left or curr_right <= curr_left + 1:
                return node
            mid = (curr_left + curr_right) // 2
            left_copy = add(state, left, right, curr_left, mid, node.left)
            right_copy = add(state, left, right, mid, curr_right, node.right)
            new_node = Node(node.value, left_copy, right_copy)
            return new_node


        if n > 0:
            root = build_segment_tree([0] * len(y_coords), 0, len(y_coords))
            length = len(y_set)
            versions = [root]

            for i in events:
                versions.append(add(i.state, y_set.index(i.y_start), y_set.index(i.y_end), 0, length, versions[-1]))


        def get_answer(x, y, versions):
            current = versions[x]
            sm, left_border, right_border = 0, 0, length
            while current:
                sm += current.value
                mid = (left_border + right_border) // 2
                if y < mid:
                    current = current.left
                    right_border = mid
                else:
                    current = current.right
                    left_border = mid
            return sm


        m = 10000
        for i in range(m):
            x = (2999 * i) ** 31 % (n * 20)
            y = (5323 * i) ** 31 % (n * 20)
            x = bisect.bisect_right(x_set, x)
            y = bisect.bisect_right(y_set, y) - 1
            if n > 0:
                a = get_answer(x, y, versions)
            else:
                a = 0
        end = time.time()
        time_amounts[tmp] = end - begin

for i in time_amounts:
    i /= repeats
print(time_amounts)
