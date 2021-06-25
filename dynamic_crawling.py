#!/usr/bin/env python
# coding: utf-8

# In[41]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import time


# In[ ]:


#xpath 測試
#One way to solve this problem is to use explicit waits. An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code. Maybe the button takes time to become visible and before it is visible, Selenium looks for it and cannot find it, therefore throwing an error
'''

driver = webdriver.Chrome()
driver.get('https://law.judicial.gov.tw/FJUD/data.aspx?ty=JD&id=PCDM%2c108%2c%e6%99%ba%e8%a8%b4%2c18%2c20200702%2c1')
button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="JudHis"]/div[2]/ul/li[1]/a')))
button.click()

'''


# In[42]:


#爬蟲function
def get_pdf(key_words):
    driver = webdriver.Chrome()
    driver.get('https://law.judicial.gov.tw/FJUD/default.aspx')
    #找到搜尋位置
    search_place = driver.find_element_by_id("txtKW")
    #送入關鍵字
    search_place.send_keys(key_words)
    #找到查詢按鈕
    button = driver.find_element_by_id("btnSimpleQry")
    button.click()
    driver.switch_to.frame(0)
    page_html = driver.page_source
    link_list = get_details(page_html)
    driver.get('https://law.judicial.gov.tw/FJUD/'+ link_list[0])
    #找到歷年審判的第一個
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="JudHis"]/div[2]/ul/li[1]/a')))
    button.click()
    #此時會跳一個新視窗出來，要切換過去，切換過後才下載pdf
    first_window = driver.current_window_handle
    all_handles = driver.window_handles
    for handle in all_handles:
        if handle != first_window:
            driver.switch_to.window(handle)
    driver.find_element(By.ID, "hlExportPDF").click()
    driver.close()
#獲取第三個頁面的link_list，但在此只用第一個link_list[0] 
def get_details(page_html):
    soup = BeautifulSoup(page_html,'html.parser')
    a = soup.find_all('a',id = 'hlTitle')
    link_list = []
    for i in a:
        link = i.get('href')
        link_list.append(link)
    return(link_list)
#從找一審檔案中的 judje2.txt 找到檔案中的搜尋keywords
def get_judge2_keywords(full_path):         
    f = open(full_path,'r',encoding = 'utf-8')
    kw1 = f.readline().splitlines()
    kw = f.readline().splitlines()
    s = kw1[0]+kw[0]
    return s 


# In[43]:


#拿到keywords(二審) 放入 judge2_keywords list
judge2_keywords = []
folder_path = r'C:\Users\USER\Documents\資訊創新應用競賽\找一審'
folder_content = os.listdir(folder_path)
for i in folder_content:
    full_path = os.path.join(folder_path,i)
    if os.path.isfile(full_path):
        print("..................................")
        print("doing:"+full_path)
        print("..................................")
        f2 = open(full_path,'r')
        for line in f2.readlines():
            path = line.split("\\")
            path = folder_path+"\\"+path[-2]+"\\"+path[-1]
            path = path.splitlines()
            print(get_judge2_keywords(path[0]))
            judge2_keywords.append(get_judge2_keywords(path[0]))
        f2.close()


# In[4]:


judge2_keywords


# In[46]:


#放入迴圈
error_key = []
for i in range(len(judge2_keywords)):
    time.sleep(2)
    try:
        print("diong"+":"+judge2_keywords[i])
        get_pdf(judge2_keywords[i])
    except Exception as e :
        print(e)
        error_key.append(judge2_keywords[i])
        continue


# In[ ]:
