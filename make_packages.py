

def totalGiftsWeight(gifts):
    print(f"total gifts weight:  {sum([i[1] for i in gifts])}")

def totalGiftsVolum(gifts):
    print(f"total gifts volum:  {sum([i[2] for i in gifts])}")

def makePackages(gifts, showTotalInfo=False):
    if showTotalInfo:
        totalGiftsWeight(gifts)
        totalGiftsVolum(gifts)
        print()
        print()
    gifts.sort(key= lambda x: x[1])
    res = []
    tmp = []
    r,l = len(gifts) - 1, 0
    cnt = 0
    while r != l:

        if cnt % 2 == 0:
            if sum([j[2] for j in tmp]) + gifts[l][2] < 100 and sum([j[1] for j in tmp]) + gifts[r][1] < 200:
                tmp.append(gifts[l])
            else:
                res.append(tmp)
                tmp = []
                tmp.append(gifts[l])
            l += 1
        else:
            if sum([j[2] for j in tmp]) + gifts[r][2] < 100 and sum([j[1] for j in tmp]) + gifts[r][1] < 200:
                tmp.append(gifts[r])
            else:
                res.append(tmp)
                tmp = []
                tmp.append(gifts[r])
            r -= 1
        cnt += 1
    res.append(tmp)

    return res