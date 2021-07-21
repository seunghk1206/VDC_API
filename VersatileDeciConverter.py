import string
def Arr2Unf(arr2):
    retL = [var for each in arr2 for var in each]
    return retL
def versatileDeci(n, TargetNum, num):
    try:
        TargetNum = eval(TargetNum)
    except:
        pass
    a = [str(each) for each in range(10)]
    for each in Arr2Unf([string.ascii_lowercase, string.ascii_uppercase]):
        for eachLetter in each:
            a.append(eachLetter)
    a.append('#')
    a.append('@')
    ans = ''
    hexaL = a
    if TargetNum >= 1:
        intP = str(TargetNum).split('.')[0]
        if num**(n+1) > int(intP) >= num**n:
            for each in range(n+1):
                ans += hexaL[int(intP)//(num**abs(each-n))]
                intP = str((int(intP)%(num**abs(each-n))))
            try:
                decP = str(TargetNum).split('.')[1]
                decP = '.' + decP
                return ans + versatileDeci(-1, float(decP), num)
            except:
                return ans
        else:
            return versatileDeci(n+1, TargetNum, num)
    elif TargetNum < 0:
        return '-' + versatileDeci(0, -TargetNum, num)
    elif TargetNum == 0 or TargetNum == '0':
        return '.0'

    elif 1 > TargetNum > 0:
        if num**(n+1) > TargetNum >= num**n:
            if TargetNum%(num**n) == 0:
                return '.' + hexaL[int(TargetNum//(num**n))]
            return '.' + hexaL[int(TargetNum//(num**n))] + versatileDeci(n-1, TargetNum%(num**n), num)
        else:
            return '0' + versatileDeci(n-1, TargetNum, num)
print(versatileDeci(0, float(input()), int(input())))