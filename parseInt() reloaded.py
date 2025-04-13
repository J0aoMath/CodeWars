def transform_list(answer):
        #[40, 4, 1000000, 3, 100, 80, 6, 1000, 1, 100, 50, 6]
        print(f'---------------------- \n essa é a lista: {answer}')
        others = []
        for f,value in enumerate(answer):
                if len(str(value)) == 2:
                        try:
                                if answer[f+1] < value:
                                        answer[f] = value + answer[f+1]
                                        answer.pop(f+1)
                        except:
                                pass
        print(f'nova lista: {answer}')
        for f,value in enumerate(answer[::-1]):
                z = len(answer)-f
                if value >= 100:
                        try:
                                if not answer[z-1] < answer[z-2]:
                                        print(f'answer:{answer} value: {value}')
                                        answer[z-1] = value * answer[z-2]
                                        print(f'números sendo multiplicados: {value} e {answer[z-2]}')
                                        answer.pop(z-2)
                                        print(f'esse é o answer[z-2] {answer[z-2]}')
                                elif len(str(answer[z-2])) == 3:
                                        if value == 100:
                                                break
                                        print(f'answer:{answer} value: {value}')
                                        print(f'z-3,z-2 e z-1: {answer[z-3]}x{answer[z-2]}+{answer[z-1]}')
                                        answer[z-2] = answer[z-3] * answer[z-2] + answer[z-1]
                                        answer.pop(z-1)
                                        answer.pop(z-3)
                                        answer[z-2] = answer[z-3] * answer[z-2]
                                        answer.pop(z-3)
                        except:
                                try:
                                        answer[z] = value * answer[z-2]
                                        answer.pop(z-2)
                                        print(f'tentou {value} * {answer[z-2]}')
                                except:
                                        pass
        
        print(f'essa é a resposta: {answer}')

        

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
parse_int('two hundred forty-six')
parse_int('forty-four million three hundred eighty-six thousand one hundred fifty-six')

