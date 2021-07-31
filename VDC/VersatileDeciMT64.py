def versatileDeci(n, TargetNum, num):
    a = []
    for each in range(num):
        a.append('(' + str(each) + ')')
    ans = ''
    hexaL = a
    if float(TargetNum) >= 1:
        intP = str(TargetNum).split('.')[0]
        if num**(n+1) > int(intP) >= num**n:
            for each in range(n+1):
                ans += hexaL[int(intP)//(num**abs(each-n))]
                intP = str((int(intP)%(num**abs(each-n))))
            try:
                decP = str(TargetNum).split('.')[1]
                decP = '0.' + decP
                return ans + '.' + versatileDeci(-1, float(decP), num)
            except:
                return ans
        else:
            return versatileDeci(n+1, TargetNum, num)
    elif float(TargetNum) < 0:
        return '-' + versatileDeci(0, -TargetNum, num)
    elif float(TargetNum) == 0 or TargetNum == '0':
        return '0'
    elif 1 > float(TargetNum) > 0:
        if num**(n+1) > TargetNum >= num**n:
            if TargetNum%(num**n) == 0:
                return hexaL[int(TargetNum//(num**n))]
            return hexaL[int(TargetNum//(num**n))] + versatileDeci(n-1, TargetNum%(num**n), num)
        else:
            return '0' + versatileDeci(n-1, TargetNum, num)
val = float(input('the value you want to convert in decimal! '))
Nnary = int(input('which code? binary? '))
print(str(val), ' in ', Nnary, '^ n is ', versatileDeci(0, val, Nnary))