from selenium import webdriver
from getpass import getpass
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

driver = webdriver.Chrome()

def login(url):
    driver.get(url)
    email_field = driver.find_element_by_id("m_login_email")
    password_field = driver.find_element_by_id("m_login_password")
    login_btn = driver.find_element_by_css_selector('._2pie div')
    email = "annasrizwan2003@gmail.com"
    password = "" #put Your Password Here.
    email_field.send_keys(email)
    password_field.send_keys(password)
    login_btn.click()
    while (True):   
        try:
            ok_button = driver.find_element_by_css_selector('._2pis')
            ok_button.click()
            break
        except:
            continue
    print("login Successfull\n")

def share_post (caption):

    share_button = driver.find_element_by_css_selector("._15kr")
    share_button.click()
    
    share_button_2 = driver.find_element_by_id("share-with-message-button")
    share_button_2.click()
    
    while (True):   
        try:
            text_area = driver.find_element_by_id("share_msg_input")
            text_area.send_keys(caption)
            break
        except:
            continue
    print("Post Shared \n")
    driver.find_element_by_id("share_submit").click()

def get_to_post():
    global driver
    post_url = "https://m.facebook.com/groups/380137593049071/permalink/389411455455018/"
    driver.get(post_url)

def like_post():
    print("Posted Liked \n")
    like_btn = driver.find_element_by_css_selector("div[data-sigil='ufi-inline-actions'] div")
    like_btn.click()
    
def comment(text):
    while(True):
        try:    
            comment_box = driver.find_element_by_css_selector("div[data-sigil='m-composer'] textarea#composerInput")
            comment_box.send_keys(text)
            break
        except:
            continue
    
    post_button = driver.find_element_by_css_selector("div[data-sigil='m-composer'] button[data-sigil='touchable composer-submit']")
    for i in range(15):
        post_button.click()

def main():
    login("https://m.facebook.com")
    get_to_post()
    like_post()
    share_post("From Zero to hero, Here I am Sharing this using Selenium. #DSC_DSU #Tarun")
    get_to_post()
    for i in range(50):
        comment("Well Ths BootCamp Have Been Great For Me. Just A New Student Learning To code Discovered this bootcamp and suddendly started scrapping website. Great Teachers With Great fellows Goodluck Everyone")

if __name__ == '__main__' :
    main()