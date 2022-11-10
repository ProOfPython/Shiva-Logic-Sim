def NOT(a):
    if a == '0':
        return '1'
    else:
        return '0'
def AND(a, b):
    if a == '1' and b == '1':
        return '1'
    else:
        return '0'
def OR(a, b):
    if a == '1' or b == '1':
        return '1'
    else:
        return '0'

ind = 0
operLst = []
operStr = input()

# Turns string to list
for val in operStr:
    operLst.append(val)

# ! (not) logic
for val in operLst:
    if val == '!':
        operLst[ind] = NOT(operLst[ind + 1])
        operLst.pop(ind + 1)
    ind += 1
# & (and) logic
ind = 0
for val in operLst:
    if val == '&':
        operLst[ind] = AND(operLst[ind + 1], operLst[ind - 1])
        operLst.pop(ind + 1)
        operLst.pop(ind - 1)
    ind += 1
# / (or) logic
ind = 0
for val in operLst:
    if val == '/':
        operLst[ind] = OR(operLst[ind + 1], operLst[ind - 1])
        operLst.pop(ind + 1)
        operLst.pop(ind - 1)
    ind += 1

# Turns list to string
operStr = ''
for val in operLst:
    operStr += val

print(operStr)