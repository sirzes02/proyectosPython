from collections import Counter

num_friends = [100, 49, 41, 40, 25]


# Calculating the mean value
def mean(x):
    return sum(x) / len(x)


print(mean(num_friends))


# Calculating the median value

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        low = midpoint - 1
        high = midpoint
        return (sorted_v[low] + sorted_v[high]) / 2


print(median(num_friends))


# Calculating the quantile

def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]


print(quantile(num_friends, 0.10))


# Calculating mode

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems() if count == max_count]


print(mode(num_friends))
