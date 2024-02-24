from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

# how to find the price from amazon as we did in the previous exercise
# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")


# easy way to find nested elements using CSS selector
doc_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(doc_link.get_attribute("href"))

# if nothing else work , we can use Xpath to find the element. in the browser we can right click on the element and select inspect element and copy the xpath


doc_link_xpath = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a')
print(doc_link_xpath.get_attribute("href"))

# Excercise: find the upcoming events list from the python.org website
events = {}
upcoming_events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul').find_elements(By.TAG_NAME, "li")
for ix,event in enumerate(upcoming_events):

    events[ix]= ({'time':event.text.split("\n")[0], 'name':event.text.split("\n")[1]})


    #print(event.find_element(By.TAG_NAME, "a").get_attribute("href"))

print(events)

# driver.close() -- close only one tab

# driver.quit() -- close all tabs