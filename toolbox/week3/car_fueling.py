from sys import stdin


def min_refills(distance, tank, stops):
    stops = [0] + stops
    tot_tank = tank
    count = 0
    for dist1, dist2 in list(zip(stops, stops[1:] + [distance])):
        dist = (dist2 - dist1)
        if dist > tank:
            return -1
        tot_tank -= dist

        if tot_tank < 0:
            #print(dist1, dist2)
            count += 1
            tot_tank = tank - dist
    return count


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
