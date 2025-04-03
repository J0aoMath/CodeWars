#Extract the domain name from a URL
# Write a function that when given a URL as a string, parses out just
# the domain name and returns it as a string. For example:
# url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    f = int(is_first(url))
    domain = ''
    for x in range(f, len(url)):
        if url[x] == '.':
            break
        domain += url[x]
        
    return domain

def is_first(url):
    resultado = ''
    string = ''
    c = 0
    for x in url:
        string += x
        if x == '.':
            if url[c-1] == '/':
                resultado += str(c+1)
            if url[c-1] == 'w':
                if url[c-2] == url[c-3] == 'w':
                    resultado += str(c+1) 
                else:
                    resultado += is_http(string)
            else:
                resultado += is_http(string)
            break
        else:
            c += 1
    return int(resultado)
def is_http(string):
    z = 0
    for y in string:
        if y == '/':
            resultado += str(z+2)
            break
        z += 1
        resultado = '0'
    return resultado

print(domain_name('https://27b8bvb3gpmode7y8hgoro9anw.tv/'))

#Others Solution:
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
#
import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
#

