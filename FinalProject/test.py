from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.flashscore.com/team/g2-esports-league-of-legends/ER93S8GO/results/')
time.sleep(2)

cookies_accept = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
#div2 = div.find_element_by_xpath('//*[@id="notice"]')
#div2 = div.find_element_by_xpath('/html/body/div/div[1]')
#div3 = driver.find_element_by_xpath('/html/body/div/div[2]/div[6]/div[2]/button')
cookies_accept.click()
test = driver.find_element_by_xpath('//*[@id="g_36_nVVZdUTN"]/span[2]').text
print(test)
time.sleep(100)
