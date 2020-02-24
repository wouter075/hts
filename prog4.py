import xmltodict

from settings import *
from selenium import webdriver
import os
import bz2, shutil
import xml.dom.minidom
import math
from PIL import Image, ImageDraw

# downloaddir = os.getcwd() + "/prog4"
#
# profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.folderList', 2) # custom location
# profile.set_preference('browser.download.manager.showWhenStarting', False)
# profile.set_preference('browser.download.dir', downloaddir)
# profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
#
# driver = webdriver.Firefox(profile)
# driver.get("https://www.hackthissite.org/")
#
# u = driver.find_element_by_name("username").send_keys(username)
# p = driver.find_element_by_name("password").send_keys(password)
# driver.find_element_by_name("btn_submit").click()
#
# driver.get("https://www.hackthissite.org/missions/prog/4/")


# download file:
# driver.get("https://www.hackthissite.org/missions/prog/4/XML")
width = 1000
height = 1000

im = Image.new('RGB', (width, height), (0, 0, 0))


with bz2.BZ2File("prog4/plotMe.xml.bz2") as fr, open("prog4/output.xml", "wb") as fw:
    shutil.copyfileobj(fr, fw)

doc = xml.dom.minidom.parse("prog4/output.xml")
lines = doc.getElementsByTagName("Line")
# print(arcs[0].getElementsByTagName('XStart')[0].firstChild.nodeValue)
for l in lines:
    xstart = float(l.getElementsByTagName('XStart')[0].firstChild.nodeValue)
    xend = float(l.getElementsByTagName('XEnd')[0].firstChild.nodeValue)

    ystart = float(l.getElementsByTagName('YStart')[0].firstChild.nodeValue)
    yend = float(l.getElementsByTagName('YEnd')[0].firstChild.nodeValue)

    color = "white"
    try:
        color = l.getElementsByTagName('Color')[0].firstChild.nodeValue
    except IndexError:
        pass

    draw = ImageDraw.Draw(im)
    draw.line((xstart, ystart, xend, yend), fill=color)

arcs = doc.getElementsByTagName("Arc")
for a in arcs:
    xcenter = float(a.getElementsByTagName('XCenter')[0].firstChild.nodeValue)
    ycenter = float(a.getElementsByTagName('XCenter')[0].firstChild.nodeValue)
    arcextend = float(a.getElementsByTagName('ArcExtend')[0].firstChild.nodeValue)
    radius = float(a.getElementsByTagName('Radius')[0].firstChild.nodeValue)
    arcstart = float(a.getElementsByTagName('ArcStart')[0].firstChild.nodeValue)

    draw = ImageDraw.Draw(im)
    draw.arc((xcenter-radius, height-(ycenter+radius), xcenter+radius, height-(ycenter-radius)),
             -1*(arcstart + arcextend), -1*arcstart, fill=255)
#     https://github.com/alicansa/HackThisSite/blob/3b2e6fdc0a2702fe67fbbf6918fdb8cb9dca6abd/Mission4_XMLDraw/XMLDraw.py

im.show()