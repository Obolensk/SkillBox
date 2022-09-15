# TODO здесь писать код

# vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip
#
# Расшифровка (со сдвигом на 1 символ влево):
# utifulBea si terbet ntha y/ugl icitExpl is erbett than icit/impl eSimpl si rbette hant ex/compl xComple is better anth cated/compli tFla si etterb ntha nested/ arseSp is tterbe than nse/de tyReadabili unts/co cialSpe cases (taren cialspe ghenou to break het s/rule houghAlt ypracticalit eatsb ty/puri Errors should verne pass ently/sil nlessU licitlyexp nced/sile In eth cefa of guity-ambi fusere eth tationtemp to ess/gu There uldsho eb one.. and rablyprefe yonl one ous..obvi way ot od it/ Although that ayw aym otn be viousob at irstf ssunle reyou( h/Dutc wNo si rbette hant /never thoughAl ernev is enoft better anth ht++rig w/no fI het mentationimple si dhar ot lain-exp sit( a adb /idea If eth entationimplem is easy to ain-expl it yma be a good idea/ amespacesN are one honking reatg deai .. et(sl od orem fo se"tho
# Получается надо выработать алгоритм решения такой задачи:
# 1. На 1 влево
# 2. 3 последние буквы ставим вперед, остальные за ними
#
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
print(text)
print(len(text))
print(abc.index(text[6]))
abc += 'LLL'
print(abc)

new_text = ''
num = int(input('Введите сдвиг: '))
for i in range(len(text)):
    new_text += abc.index(text[i-num])
print(new_text)