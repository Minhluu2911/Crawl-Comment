# library we will use in this project
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# open browser
browser = webdriver.Chrome(executable_path="chromedriver.exe") # choose what browser you use
browser.get("https://www.facebook.com/groups/miaigroup/permalink/730028114435130/") # the link of post you want to crawl
sleep(3)

# go to where you want to click by xpath
showcomment_link = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a")
showcomment_link.click()
sleep(3)

showmore = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div/div/div[2]/div[2]/form/div/div[3]/div[1]/div/a/div/span")
showmore.click()
sleep(3)
showmore.click()

# find any div with this attribute
comment_list = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")

# print list of comments
for comment in comment_list:
    #hien thi ten nguoi va noi dung
    poster = comment.find_element_by_class_name("_6qw4")
    content = comment.find_element_by_class_name("_3l3x")
    print("_",poster.text ,": ", content.text)

sleep(10)
# close browser
browser.close()
