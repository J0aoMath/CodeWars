def transform_list(answer):
    
        print(answer)

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

parse_int('one')
parse_int('eleven')
parse_int('twenty'),
parse_int('two hundred forty-six')
parse_int('forty-four million three hundred eighty-six thousand one hundred fifty-six')

