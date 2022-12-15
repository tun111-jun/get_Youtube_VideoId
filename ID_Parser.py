from selenium import webdriver
import time
from openpyxl import Workbook
import pandas as pd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os

print(os.getcwd())
import warnings 
warnings.filterwarnings('ignore')

wb = Workbook(write_only=True)
ws = wb.create_sheet()
keyword = 'No Fear Of Falling, I Am Kloot'
#https://www.youtube.com/watch?v=A88N8CVcnR8
#req = requests.get('https://www.youtube.com/results?search_query=' + keyword)
driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.youtube.com/results?search_query=' + keyword)
#driver.implicitly_wait(3)

#time.sleep(1.5)

driver.execute_script("window.scrollTo(0, 1)")
#time.sleep(3)

last_height = driver.execute_script("return document.documentElement.scrollHeight")
count=0
while (count!=1):
    driver.execute_script("window.scrollTo(0, 1);")
    #time.sleep(1.5)
    
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    count=count+1

#time.sleep(1.5)

try:
    driver.find_element_by_css_selector("#dismiss-button > a").click()
except:
    pass


html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

my_titles = soup.select("h3 > a")
#comment_list = soup.select("yt-formatted-string#content-text")
#print(id_list)
id_final = []
comment_final = []
title = []
url = []

for idx in my_titles:
    if idx.get('href')[:7] != '/watch?':
        pass
    else:
        title.append(idx.text)
        url.append(idx.get('href'))
print(url)
# for i in range(len(comment_list)):
#     temp_id = id_list[i].text
#     temp_id = temp_id.replace('\n', '')
#     temp_id = temp_id.replace('\t', '')
#     temp_id = temp_id.replace('    ', '')
#     id_final.append(temp_id) # 댓글 작성자

#     temp_comment = comment_list[i].text
#     temp_comment = temp_comment.replace('\n', '')
#     temp_comment = temp_comment.replace('\t', '')
#     temp_comment = temp_comment.replace('    ', '')
#     comment_final.append(temp_comment) # 댓글 내용
#pd_data = {"아이디" : id_final , "댓글 내용" : comment_final}
#youtube_pd = pd.DataFrame(pd_data)