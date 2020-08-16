from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#  def data_list1():
#      for i in range(1,21):
#         s_elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/section/article[1]/div/text()[%s]"%i)
#         s = s_elem.get_attribute('text')
#         if i%2 == 1 :
#             f.write("    Q :%s\n" % s)
#         else:
#             f.write("    A :%s\n" % s)  

#  def data_list2():
#      for i in range(1,21):
#         f.write("%d : "%i)
#         s_elem = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/section/article[1]/div/text()[@*]")
#         for t in s_elem :
#             s = t.text
#             f.write(s)
#             f.write("\n")

# def data_list3():
#     for i in range(1,21):
#         f.write("%d : "%i)
#         s_elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/section/article[1]/div/text()[%s]"%i)
#         t = s_elem.text
#         f.write(t)

# def data_list4():
#     s_elem = driver.find_elements_by_css_selector("br.article:nth-child(1) > .awr")
#     for i in s_elem: 
#         f.write("\n    %d"%i)   
#         s = s_elem.text
#         f.write(s)

# def data_list5():
#     css = driver.find_element_by_class_name("awr")
#     Q_elem = css.find_elements_by_tag_name("br")
#     for y in Q_elem:
#         f.write("    Q :%s\n" % y.text)
#     A_elem = css.find_elements_by_tag_name("p")
#     for z in A_elem:
#         f.write("    A :%s\n" % z.text)

# def data_list6():
#     css = driver.find_element_by_class_name("awr")
#     Q_elem = css.find_elements_by_tag_name("br")
#     Questions = [Q.text for Q in Q_elem]
#     for y in Questions:
#         f.write("    Q :%s\n" % y)
#     A_elem = css.find_elements_by_tag_name("p")
#     Answers = [A.text for A in A_elem]
#     for z in Answers:
#         f.write("    A :%s\n" % z)
    
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://basicenglishspeaking.com/daily-english-conversation-topics/')
f = open("test.txt","a")
for x in range(1,76):
    driver.find_element_by_xpath('//*[@id="tve_editor"]/div[3]/div/div[1]/div/div/p/a[%s]'%x).click()
    title = driver.find_element_by_class_name("entry-title")
    title_data = title.text
    f.write("%d. title: %s"%(x, title_data) + "\n")
    #data_list()
    css = driver.find_element_by_class_name("awr")
    Q_elem = css.find_elements_by_tag_name("br")
    for y in Q_elem:
        f.write("    Q : %s\n" % y.get_attribute('text'))
    A_elem = css.find_elements_by_tag_name("p")
    for z in A_elem:
        f.write("    A : %s\n" % z.get_attribute('text'))
    driver.back()
        