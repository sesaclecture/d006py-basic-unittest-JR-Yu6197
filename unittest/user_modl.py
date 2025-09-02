def mult_two_analy(a):
    if a%2 == 0:
        c = True
        return c
    else:
        return False
    
def avg(ll):

    if not ll:
        return 0
    total = sum(ll)
    ave = total/len(ll)

    return ave

def max_value(ll):
    if not ll:
        return None  
    max_val = ll[0]
    for num in ll:
        if num > max_val:
            max_val = num
    return max_val