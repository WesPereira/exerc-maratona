from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    max_capacity = capacity

    fracs = [v/w for v, w in list(zip(values, weights))]

    while max_capacity > 0:
        if all([f < 0 for f in fracs]):
            return value
        max_frac = max(fracs)
        idx = fracs.index(max_frac)
        to_rmv = 1 if max_capacity >= weights[idx] else max_capacity/weights[idx]
        value += to_rmv * values[idx]
        max_capacity -= to_rmv * weights[idx]
        fracs[idx] = -1

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
