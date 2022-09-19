
abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(text):
    new = ""
    for word in text:
        if word in abc:
            index = abc.find(word)
            new += abc[index - 1]
        else:
            new += word
    return new

def shift(text, shift_count):
    shift = shift_count % len(text)
    text = text[-shift:] + text[:-shift]
    return text

my_text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/' \
       'dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/' \
       'ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/' \
       'qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/' \
       'hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
       'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /' \
       'ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /' \
       'jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
       'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.split()

new_text = []
shift_count = 3
for word in my_text:
    text_decrypt = decrypt(word)
    shift_text = shift(text_decrypt, shift_count)
    if shift_text.endswith("/"):
        shift_count += 1
        new_text.append(shift_text)
    else:
        new_text.append(shift_text)

new_text = " ".join(new_text)
new_text = new_text.replace("+", "*")
new_text = new_text.replace("-", ",")
new_text = new_text.replace("(", "'")
new_text = new_text.replace("..", "--")
new_text = new_text.replace('"', "!")
new_text = new_text.replace("/", ".\n")

print('\n', new_text)
