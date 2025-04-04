def generate_hashtag(s):
    ss = s.split(' ')
    result = ''
    for x in ss:
        z = 0
        for c in x:
            if c != ' ':
                if z == 0:
                    result += c.upper()
                else:
                    result += c.lower()
            else:
                c.replace(' ','')
            z += 1
    if result == '' or len(result) > 139:
        return False
    return '#' + result

# Others Results:
def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
#
def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False
#
def generate_hashtag(s):
    s='#'+s.title().replace(' ','')
    return s if s!='#' and len(s)<=140 else False
