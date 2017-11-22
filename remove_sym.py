from nltk import sent_tokenize
import re

sent = "não bộ, nhiều bạn cảm thấy hứng thú và hỏi cách tạo ra chúng tự động. Dưới đây là câu trả lời nhé. Tool này sẽ giúp bạn tạo teencode sành điệu, siêu dễ thương. Song dùng chơi chơi thôi chứ đừng lạm dụng nhé. Cùng giữ gìn sự trong sáng của tiếng Việt :)"
sym = "~`!@#$%^&*()_-+=[]\{}|;':\",./<>?"

sente = sent_tokenize(sent)

for char in sym:
    sent[0] = sent[0].replace(char, "")


for s in sente:
    print(s)

#for s in sente:
#    for char in sym:
#        s = s.replace(char, '')
    
print(sente)
