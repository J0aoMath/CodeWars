#String incrementer

def increment_string(strng):
    integers_={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
    result = []
    result_ = 0
    digits = 0
    for value in strng[::-1]:
        if value in integers_:
            result.append(integers_[value])
            digits += 1
        else:
            break
    for i,value in enumerate(result[::1]):
        result_ += value * 10**i
        if result_ < 10**i:
            digits -= 1
    if digits > len(result):
        digits -= 1
    return strng[0:len(strng) - digits] + str(result_ + 1)
            
