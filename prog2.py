import urllib

from settings import *
from selenium import webdriver
from PIL import Image
from prog2.morse import *

driver = webdriver.Firefox()
driver.get("https://www.hackthissite.org/")

u = driver.find_element_by_name("username").send_keys(username)
p = driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("btn_submit").click()

driver.get("https://www.hackthissite.org/missions/prog/2/")

images = driver.find_elements_by_tag_name("img")
for i in images:
    if "/2/PNG" in i.get_attribute("src"):
        elem = i
        break

element_png = i.screenshot_as_png
with open("prog2/prog2.png", "wb") as file:
    file.write(element_png)


# image needs to be 100x30

im = Image.open('prog2/prog2.png')
im = im.resize((100, 30))
im = im.convert('1')
im.save('prog2/prog2.png')
counter = 0
solution = ""
for pixel in list(im.getdata()):
    if pixel == 255:
        if counter == 31:
            solution += " "
        else:
            solution += chr(counter)

        counter = 1
    else:
        counter += 1

# print(solution)
solution = decrypt(solution).lower()[:-1]
print(solution)
driver.find_element_by_name("solution").send_keys(solution)
driver.find_element_by_name("submitbutton").click()
