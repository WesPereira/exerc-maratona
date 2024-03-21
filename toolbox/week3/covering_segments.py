from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def intersects(start1, end1, start2, end2):
    if end2 >= end1:
        seg2 = (start2, end2)
        seg1 = (start1, end1)
    else:
        seg1 = (start2, end2)
        seg2 = (start1, end1)
    if seg2[0] <= seg1[1]:
        return True
    return False


def optimal_points(segments):
    points = []

    sorted_seg = sorted(segments, key=lambda x: x.end)

    marked = [0] * len(segments)

    for idx1 in range(len(sorted_seg)):
        if marked[idx1] == 0:
            to_exclude = [idx1]
            start1, end1 = sorted_seg[idx1]
            for idx2 in range(len(sorted_seg)):
                if idx2 != idx1 and marked[idx2] == 0:
                    start2, end2 = sorted_seg[idx2]
                    if intersects(start1, end1, start2, end2):
                        to_exclude.append(idx2)
                        if start2 > start1:
                            start1 = start2
                            
            for idx in to_exclude:
                marked[idx] = 1
            points.append(start1)

    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
