from settings import *
from selenium import webdriver

with open('prog1/wordlist.txt') as f:
    lines = [line.rstrip() for line in f]

driver = webdriver.Firefox()
driver.get("https://www.hackthissite.org/")

u = driver.find_element_by_name("username").send_keys(username)
p = driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("btn_submit").click()

driver.get("https://www.hackthissite.org/missions/prog/1/")

items = driver.find_elements_by_tag_name("li")[-10:]

anwser = ""
for i in items:
    es = sorted(i.text)

    for l in lines:
        ls = sorted(l)

        if es == ls:
            anwser += l + ","

anwser = anwser[:-1]

driver.find_element_by_name("solution").send_keys(anwser)
driver.find_element_by_name("submitbutton").click()
driver.close()


