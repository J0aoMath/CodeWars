#In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.
#Examples:
#"one" => 1
#"twenty" => 20
#"two hundred forty-six" => 246
#"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
#Additional Notes:
#The minimum number is "zero" (inclusively)
#The maximum number, which must be supported is 1 million (inclusively)
#The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
#All tested numbers are valid, you don't need to validate them


def transform_list(answer):
    if len(answer) == 1:
        return sum(answer)
    answer_ = []
    remove_ = []
    if len(answer) == 1:
        return answer
    for f,value in enumerate(answer):
        if value == 100:
                answer_.append(value * answer[f-1])
                remove_.append(f-1)
        elif 10 <= value < 100:
            try:
                if answer[f+1] < 10:
                        answer_.append(value + answer[f+1])
                        remove_.append(f+1)
                else:
                    answer_.append(value)
            except:
                answer_.append(value)
        else:
            answer_.append(value)
    c = 0
    for i in remove_:
        try:
            answer_.pop(i - c)
            c += 1
        except:
            pass
    answer_2 = []
    for f,value in enumerate(answer_):
        if 100 <= value < 1000:
            try:
                if answer_[f+1] < 100:
                    answer_2.append(value+answer_[f+1])
                else:
                    answer_2.append(value)
            except:
                print(value)
                answer_2.append(value)
        else:
            if value > 100:
                answer_2.append(value)
            elif f== len(answer_) - 1 and answer_[f-1] >= 1000:
                    answer_2.append(value)
            else:
                if f == 0:
                    answer_2.append(value)                        
                else:
                    pass
    answer_.clear()
    for f,value in enumerate(answer_2):
        if value >= 1000:
            try:
                answer_.append(value * answer_2[f-1])
            except:
                answer_.append(value)
        else:
            try :
                answer_2[f+1] += 0
            except:
                answer_.append(value)
    return sum(answer_)
                

        

def parse_int(string):
    string = string.replace('-', ' ')
    answer_ = []
    natural_= {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,
               'eight':8,'nine':9}
    ten_= {'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,
                'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19}
    decimal_={'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,
              'eighty':80,'ninety':90}
    others_={'hundred':100,'thousand':1000,'million':1000000}
    all_= [natural_, ten_, decimal_, others_]
    for f in string.split():
        if f in natural_:
            answer_.append(natural_[f])
        elif f in ten_:
            answer_.append(ten_[f])
        elif f in decimal_:
            answer_.append(decimal_[f])
        elif f in others_:
            answer_.append(others_[f])
    return transform_list(answer_)

# Others Solutions:
ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
        'eighteen', 'nineteen']
TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def parse_int(string):
    print(string)
    numbers = []
    for token in string.replace('-', ' ').split(' '):
        if token in ONES:
            numbers.append(ONES.index(token))
        elif token in TENS:
            numbers.append((TENS.index(token) + 2) * 10)
        elif token == 'hundred':
            numbers[-1] *= 100
        elif token == 'thousand':
            numbers = [x * 1000 for x in numbers]
        elif token == 'million':
            numbers = [x * 1000000 for x in numbers]
    return sum(numbers)
#
words = {w: n for n, w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
words.update({w: 10 * n for n, w in enumerate('twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(), 2)})
thousands = {w: 1000 ** n for n, w in enumerate('thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion'.split(), 1)}
def parse_int(strng):
    num = group = 0
    for w in strng.replace(' and ', ' ').replace('-', ' ').split():
        if w == 'hundred': group *= words[w]
        elif w in words: group += words[w]
        else:
            num += group * thousands[w]
            group = 0
    return num + group
