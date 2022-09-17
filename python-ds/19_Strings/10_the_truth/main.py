# TODO здесь писать код

# vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip
#
# Расшифровка (со сдвигом на 1 символ влево):
# utifulBea si terbet ntha y/ugl icitExpl is erbett than icit/impl eSimpl si rbette hant ex/compl xComple is better anth cated/compli tFla si etterb ntha nested/ arseSp is tterbe than nse/de tyReadabili unts/co cialSpe cases (taren cialspe ghenou to break het s/rule houghAlt ypracticalit eatsb ty/puri Errors should verne pass ently/sil nlessU licitlyexp nced/sile In eth cefa of guity-ambi fusere eth tationtemp to ess/gu There uldsho eb one.. and rablyprefe yonl one ous..obvi way ot od it/ Although that ayw aym otn be viousob at irstf ssunle reyou( h/Dutc wNo si rbette hant /never thoughAl ernev is enoft better anth ht++rig w/no fI het mentationimple si dhar ot lain-exp sit( a adb /idea If eth entationimplem is easy to ain-expl it yma be a good idea/ amespacesN are one honking reatg deai .. et(sl od orem fo se"tho
# Получается надо выработать алгоритм решения такой задачи:
# 1. На 1 влево
# 2. 3 последние буквы ставим вперед, остальные за ними до первого знака /
# 3. 4 последние ставим вперед до второго знака /
# 4. 5 последние ставим вперед до третьего знака / и т.д.
#
#
#
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
print(text)
print(len(text))
print('abc.index(text[6]) = ', abc.index(text[6]))
abc += 'LLL'
print(abc)

print('text[6] = ', text[6])
print('abc.index(text[6]) = ', abc.index(text[6]))
print('text[abc.index(text[6])] = ', text[abc.index(text[6])])
print('abc[abc.find(text[6])-1] = ', abc[abc.find(text[6])-1])

print()
new_text = ''
# num = int(input('Введите сдвиг: '))
num = 1
shift_count = 3


for i in text:
    if i in abc:
        new_text += abc[abc.find(i) - num]
    else:
        new_text += i
        if i == '/':
            shift_count += 1

print(text)
print(new_text)

def shift(str, count):
    if count > len(str):
        new_str = [str[i % count - 1] for i in range(len(str))]
    else:
        new_str = [str[i - count] for i in range(len(str))]
    return ''.join(new_str)


# print('new_text   = ', new_text)

num_count = 3
for word in new_text.split():
    print(shift(word, num_count), end=' ')
    if '/' in word:
        num_count += 1
        print()


# new_text_2 = []
# new_word = []
# for word in new_text.split():
#     new_word = shift(word)
#     new_text_2 += new_word

# print('new_text_2 = ', ''.join(new_text_2))
