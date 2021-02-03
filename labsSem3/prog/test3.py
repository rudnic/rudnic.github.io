def two_sum(lst, target):

    d = {}

    res = []
    pair = ()

    for i in range(len(lst)):

        d[lst[i]] = i

    print(d.keys(), d.values())

    for key in d.keys():
        if ( (target - key) in d.keys() ) and (d[key] > d[target-key]):
            pair = ( d[target-key], d[key] )
            res.append(tuple(pair))


    return res

if __name__ == "__main__":

    print(two_sum([5, 1, 4, 10, 3, 0], 4))
