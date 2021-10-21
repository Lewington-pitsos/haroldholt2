from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd

total_tweets=0
SCROLL_PAUSE_TIME = 1
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
#options.add_argument('--headless')  #not using headless spin
driver = webdriver.Chrome("/Users/jt/Downloads/chromedriver-2", chrome_options=options) #download and put the local link for chrome driver in here
tweet_mp_url="https://twitter.com/AlboMP"  # twitter handle for the politician
driver.get(tweet_mp_url)
time.sleep(3)
tweets=[]
#a = driver.find_elements_by_tag_name("span")



#x=driver.find_elements_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]")
time.sleep(1)



# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    driver.implicitly_wait(1)
    try:
        elements = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located(
        (By.XPATH, "//main//article")))
        for ele in elements:
            print(ele.text)
            tweets.append(ele.text)
            total_tweets = total_tweets+1
    except:
        pass

    time.sleep(SCROLL_PAUSE_TIME)
    driver.implicitly_wait(1)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    time.sleep(SCROLL_PAUSE_TIME)
    driver.implicitly_wait(1)
    last_height = new_height

df = pd.DataFrame(tweets, columns=["tweets"])
df.to_excel("test.xlsx")#test file




