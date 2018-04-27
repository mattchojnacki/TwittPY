import config
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import WebDriverException
import time
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#

driver = webdriver.Chrome("/Users/mateuszchojnacki/Applications/chromedriver")
def login_twitter(username, password):
    driver.get("https://twitter.com/login")

    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")

    username_field.send_keys(username)
    driver.implicitly_wait(1)

    password_field.send_keys(password)
    driver.implicitly_wait(1)

    driver.find_element_by_class_name("EdgeButtom--medium").click()

def sendTwitt(twitt):
    inputElement = driver.find_element_by_id("tweet-box-home-timeline")
    inputElement.send_keys(twitt)

    driver.implicitly_wait(1)
    driver.find_element_by_class_name("tweeting-text").click()
def openHashtag(hashtag):
    inputElement = driver.find_element_by_id("search-query")
    inputElement.send_keys(hashtag)
    driver.find_element_by_class_name("nav-search").click()


def likeAll():
    css = "button.ProfileTweet-actionButton.js-actionButton.js-actionFavorite"
    #css = "div.ProfileTweet-action.ProfileTweet-action--favorite.js-toggleState"
    manyElements = driver.find_elements_by_css_selector(css)
    print(manyElements)
    for element in manyElements:
        print("LIKE")
        try:
            element.click()
        except ElementNotVisibleException, WebDriverException:
            return None


if __name__ == "__main__":
    username = config.DATACOUP_USERNAME
    password = config.DATACOUP_PASSWORD
    twitt = "Test tweet"
    login_twitter(username, password)
    openHashtag("#InfinityWar")
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "AdaptiveFiltersBar-item")))
    finally:
        while True:
            print("5secound -> scrool -> like")
            time.sleep(2)
            likeAll()
            time.sleep(10)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
