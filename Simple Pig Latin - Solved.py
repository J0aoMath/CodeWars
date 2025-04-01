#Simple Pig Latin: Move the first letter of each word to the end of it,
#then add "ay" to the end of the word. Leave punctuation marks untouched.
#pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    words = []
    new_words = []
    not_words = []
    word = ''
    new_text = ''
    for c in text:
            if c.lower() not in alphabet:
                words.append(word)
                word = ''
                not_words.append(c)
            else:
                word += c
    if word != '': words.append(word)
    for d in words:
        new_words.append(transform_word(d))
    if len(new_words) < len(not_words):
        n = len(not_words)
    else:
        n = len(new_words)
    for i in range(0, n):
        try:
            new_text += str(new_words[i])
        except:
            pass
        try:
            new_text+= str(not_words[i])
        except:
            pass
        
    return new_text

def transform_word(word):
    new_word = ''
    for z in word[1:len(word)]:
        new_word += z
    try:
        new_word += word[0]+'ay'
    except:
        pass
    return new_word

#Others Solution
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
#
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
#
def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)
#
def pig_it(text):
    for result in pig_itRev(text):
        return result

def pig_itRev(text):
    array = text.split()
    result = []

for word in array:

    if word.isalpha():
         result.append(word[1:] + word[:1] + 'ay')
    else:
         result.append(word)

yield ' '.join(result)
#
def pig_it(text):
    #your code here
    n = 0
    x = 0
    text = text.split() #split the text into words
    text = list(text) #make the words a list
    pig_text = [] #make an empty list
    for word in text:
        a = list(word) #set a to be the list of word (the letters on their own)
        print(a)
        if len(a) > 1:
            a.append(a[0]) #add the first letter to the end
            del a[0] #delete the first letter
            a.append('ay') #add ay to the end
        if '!' in a:
            n += 1
        elif '?' in a:
            x += 1
        elif len(a) == 1:
            print(a)
            a.append('ay') 
        a = ''.join(a) #rejoin the word
        pig_text.append(a) #put the word in the empty list
    pig_text = ' '.join(pig_text) #join the words up with spaces
    return pig_text #return the sentence



