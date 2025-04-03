# Split Strings
# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the
# missing second character of the final pair with an underscore ('_').


def solution(s):
    result = []
    step = ''
    c = 1
    for x in s:
        step += x
        if c%2 == 0:
            result.append(step)
            step = ''
            c += 1
        else:
            c += 1
    if step != '':
        result.append(step)
        result[len(result)-1] += '_'
    return result

#Others Solution
def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result
