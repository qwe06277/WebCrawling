import requests
from bs4 import BeautifulSoup
subjects = [] #배열 선언


class Conversation:
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer
    def __str__(self):
        return "질문: " + self.question + "\n답변: " + self.answer




    #패턴 암기
req = requests.get("https://basicenglishspeaking.com/daily-english-conversation-topics/")
html = req.text # text화
soup = BeautifulSoup(html,'html.parser') # 읽어들이기

divs = soup.findAll('div',{'class':'thrv_wrapper thrv_text_element tve-froala fr-box'})
#print('divs = ',divs)

for div in divs:
    links = div.findAll('a') #div안의 a들의 집합
    print('links = ', links)
#     for link in links :
#         subjects.append(link.text)

#     return subjects

# subjects = get_subjects()
# print("총",len(subjects),"개의 주제를 찾았습니다.")
# i = 1
# for sub in subjects:
#     print("(",i,"/",len(subjects),")",sub)
#     req = requests.get('https://basicenglishspeaking.com/'+sub)
#     html = req.text
#     soup = BeautifulSoup(html,'html.parser')

#     qnas = soup.findAll('div',{'class':'sc_player_container1'})
#     for qna in qnas :
#         if qnas.index(qna) % 2 == 0:
#             q = qna.next_sibling
#         else:
#             a = qna.next_sibling
#             c = Conversation(q,a)
#             print(str(c))
#             print()

#     i = i + 1
#     if i == 5:
#         break
