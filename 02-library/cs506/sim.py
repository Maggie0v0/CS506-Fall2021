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
    sum1, sum2, sum3 = 0
    for i in range(len(x)):
        a = x[i]
        b = y[i]
        sum1 += a*a
        sum2 += b*b
        sum3 += a*b
    result = sum3/((sum1*sum2)^(1/2))

# Feel free to add more
