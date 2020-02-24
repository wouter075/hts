from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.hackthissite.org/")

u = driver.find_element_by_name("username").send_keys(username)
p = driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("btn_submit").click()

driver.get("https://www.hackthissite.org/missions/prog/12/")

text = driver.find_elements_by_tag_name("input")[0].get_attribute("value")
print(text)

driver.close()
