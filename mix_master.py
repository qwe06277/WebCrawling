import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#login
ID = '아이디'
PW = '비밀번호'
driver = webdriver.Chrome()
driver.get('http://www.mixmaster.co.kr/')
driver.find_element_by_xpath('//*[@id="AuroraPopupLayer_Set01"]/span[3]').click()
driver.find_element_by_name('id').send_keys(ID)
driver.find_element_by_name('passwd').send_keys(PW)
driver.find_element_by_xpath('//*[@id="input_box"]/div[2]/p/input').click()
driver.find_element_by_xpath('//*[@id="snb03"]/div/a/img').click()


items = []
i = 1
req = driver.page_source
soup = BeautifulSoup(req,'html.parser')
divs = soup.findAll('div',{'class':'top_tit'})
#print(divs)
for div in divs : 
    paragraphs = div.findAll('p','top_text')
    items.append(paragraphs[0].text)
print("총 ",len(items),"개의 아이템을 찾았습니다.")
for item in items:
    print(i,". 아이템명 :", item)
    i += 1






