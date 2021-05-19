from bs4 import BeautifulSoup
import requests
# import re

results = []
original_website_of_results = []
# counter = -1
# code_to_change = input("Input code_to_change:")
original_url = input("請輸入第一個裁判書的連結:")


def url_spliting(original_url_):
    a = original_url_.split("q=")
    b = a[1].split("&sort")
    return b[0]


def def_url(counter_, code_to_change_):
    url_front = "https://law.judicial.gov.tw/FJUD/data.aspx?ro="
    url_mid = "&q="
    url_last = "&sort=DS&ot=in"
    return url_front + str(counter_) + url_mid + code_to_change_ + url_last


def html_retrieving():
    url = def_url(counter, url_spliting(original_url))
    html = requests.get(url)
    html.encoding = "UTF-8"
    bSoup = BeautifulSoup(html.text, 'html5lib')
    to_decode = bSoup.find_all(class_="htmlcontent")
    if (len(to_decode)) == 0:
        print("Check Your Address!")
        exit(0)
    if to_decode[0].text == "":
        to_decode = bSoup.find_all(class_="text-pre text-pre-in")
    original_website_of_results.append(def_url(counter, url_spliting(original_url)))
    results.append(to_decode[0].text)


def get_url(num: int):
    print(def_url(num - 1, url_spliting(original_url)))
    exit(0)


# 若要查看特定判決對應的原始URL，將下列的#號移除，並將括號中的數字改為目標判決所標示之號碼
# get_url(eval(input("請輸入判決主文上方的數字:")))
num_to_search = eval(input("請輸入要查詢的資料數:"))
for counter in range(0, num_to_search, 1):
    # counter = counter + 1
    print(counter + 1)
    html_retrieving()
    print(results[counter])
    print("\n")
