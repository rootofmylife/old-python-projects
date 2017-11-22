from nltk import sent_tokenize
from pprint import pprint

#sent = "não bộ, nhiều bạn cảm thấy hứng thú và hỏi cách tạo ra chúng tự động. Dưới đây là câu trả lời nhé. Tool này sẽ giúp bạn tạo teencode sành điệu, siêu dễ thương. Song dùng chơi chơi thôi chứ đừng lạm dụng nhé. Cùng giữ gìn sự trong sáng của tiếng Việt :)"
senta = open('./Roy_VnTokenizer-master/scripts/input1.tkn', 'r').read()

sym = r"~`!@#$%^&*()_-+=[]{}|;':\"”“,./<>?"

sent = sent_tokenize(senta)

sent = [s.lower() for s in sent]

sent = [s.translate({ord(c): "" for c in sym}) for s in sent]

text = open('./Roy_VnTokenizer-master/scripts/input2.txt', 'w')

for s in sent:
    text.write(s + '\n')

text.close()




