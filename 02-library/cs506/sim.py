def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    m = zip(x,y)
    s = 0
    for i,j in m:
        a = abs(i-j)
        s += a
    return s

def jaccard_dist(x, y):
    x = set(x)
    y = set(y)
    intersect = x.intersection(y)
    union = x.union(y)
    return float(len(intersect)/len(union))

def cosine_sim(x, y):
    raise NotImplementedError()

# Feel free to add more
