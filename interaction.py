from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading


def my_function():
    score = driver.find_element(By.CSS_SELECTOR, "#money")
    #print(score.text)
    return int(score.text)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element(By.ID, "mp-welcomecount").find_element(By.CSS_SELECTOR, '[title="Special:Statistics"]')
# find element by id=articlecount and then find the a element inside it
count2 = driver.find_element(By.CSS_SELECTOR, '#articlecount a')

print(count.text)
print(count2.text)

# search input elemt of search bar and type text to search + enter
search = driver.find_element(By.NAME, "search")
search.send_keys("python" + Keys.ENTER)

# Challenge type name and email into the form in https://secure-retreat-92358.herokuapp.com

driver.get("https://secure-retreat-92358.herokuapp.com")

fnameinput = driver.find_element(By.NAME, "fName")
fnameinput.send_keys("Yuval")
lnameinput = driver.find_element(By.NAME, "lName")
lnameinput.send_keys("Cohen")
emailinput = driver.find_element(By.NAME, "email")
emailinput.send_keys("yuvalco1@gmail.com")
button = driver.find_element(By.CSS_SELECTOR, "button")
button.click()

# Day project cookie clicker - https://orteil.dashnet.org/experiments/cookie/

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

inc_index =0
timer = threading.Timer(5, my_function)
timer.start()
while True:
    cookie.click()
    if timer.is_alive():
        pass
    else:
        if my_function() > 100+inc_index * 15:
            buygrandma = driver.find_element(By.ID, "buyGrandma")
            buygrandma.click()
            inc_index += 1
        elif my_function() > 15:
            buycursor = driver.find_element(By.ID, "buyCursor")
            buycursor.click()
        timer = threading.Timer(5, my_function)
        timer.start()
# This function will be called after the delay


#
# # Create a timer that will call 'my_function' after 5 seconds
# timer = threading.Timer(5, my_function)
#
# # Start the timer
# timer.start()
#
# # driver.quit()
