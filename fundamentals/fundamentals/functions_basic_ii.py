def countdown(x):
    li = []
    for i in range(x,-1,-1):
        li.append(i)
    return li

print(countdown(10))

def p_and_r(x):
    print(x[0])
    return x[1]

result = p_and_r([4,5])
print(result)

def fst_plus_len(x):
    return x[0] + len(x)

print(fst_plus_len([1,2,3,4]))

def val_great_than_sec(x):
    li = []
    if len(x) < 2:
        return False
    for i in range(0,len(x)):
        if x[i] > x[1]:
            li.append(x[i])
    return li

print(val_great_than_sec([5,2,3,2,1,4]))

def len_and_val(x,y):
    li = []
    for i in range(x):
        li.append(y)
    return li

print(len_and_val(4,7))
