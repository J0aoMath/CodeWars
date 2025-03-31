#Simple Pig Latin: Move the first letter of each word to the end of it,
#then add "ay" to the end of the word. Leave punctuation marks untouched.
#pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#pig_it('Hello world !')     # elloHay orldway !


#Infelizmente não consegui realizar o desafio.



def pig_it(text):
    palavras = []
    simbolos = []
    novas_palavras = []
    comeco = [0]
    w = 0
    for c in range(0,len(text)-1):
        palavra = ''
        if text[c] != ' ':
            palavra.join(text[c])
        else:
            palavras.append(palavra)
            simbolos.append(text[c])
            palavra = ''
    palavras.append(palavra)
    for c in palavras:
        novas_palavras.append(transformar_palavra(c))
    return formar_resultado(novas_palavras, sinais)
def transformar_palavra(palavra):
    nova_palavra = ''
    for c in range(1,int(len(palavra)-1)):
        nova_palavra.join(palavra[c])
    nova_palavra.join(palavra[0] +'ay')
def formar_resultado(novas_palavras, sinais):
    resultado = ''
    d = 0
    for c in novas_palavras:
        resultado.join(c)       try:
            sinal = sinais[d]
            resultado.join(sinal)
            d += 1
        except:
            pass
    return resultado


#

