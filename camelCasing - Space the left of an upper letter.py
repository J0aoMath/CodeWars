#Break camelCase: Complete the solution so that the function -
#- will break up camel casing, using a space between words.
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

#My Solution
def solution(s):
    t = s
    c = 0
    for i in range(0, len(s)):
         if s[i] == s[i].upper() and i != 0:
                t = t[0:i+c] + ' ' + t[i+c:len(t)]
                c += 1
    return t

#Others Solution
def solution1(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
# ---
def solution2(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += " "
        newStr += letter
    return newStr
