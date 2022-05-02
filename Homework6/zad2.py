from selenium import webdriver
import time
import requests

driver = webdriver.Chrome()
driver.get('https://www.pap.pl/')
time.sleep(2)

# 1. Accept Cookies
cookies_accept = driver.find_element_by_xpath('//*[@id="cookie"]/div/div/div/div/div/div[1]')
cookies_accept.click()
time.sleep(1)

# 2. Full Screen
driver.maximize_window()
time.sleep(1)

# 3. Change Language
change_language = driver.find_element_by_xpath('//*[@id="navbar"]/ul[2]/li[3]/a')
change_language.click()
time.sleep(1)

# 4. Go to Business section
change_language = driver.find_element_by_xpath('//*[@id="block-mainnavigationen"]/ul/li[3]/a')
change_language.click()
time.sleep(1)

# 5. Download all titles to list 
section = driver.find_element_by_class_name('view-list-of-articles')
titles_raw = section.find_elements_by_class_name('title')
titles = []
for title_raw in titles_raw:
    title = title_raw.text
    titles.append(title)
    print(title)

# 6. Download images
images = section.find_elements_by_tag_name('img')

for i, image in enumerate(images):
    response = requests.get(image.get_attribute('src'))
    with open('Homework6/image' + str(i) + '.jpg', 'wb') as f:
        f.write(response.content)
# 7. Scroll down
driver.execute_script(f'window.scrollBy(0,10000)')
time.sleep(1)
# 8. Last page
last_page_button = driver.find_element_by_xpath('/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/nav/ul/li[5]/a/span[2]')
last_page_button.click()
time.sleep(1)
print(driver.find_element_by_xpath('/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/nav/ul/li[5]/a').text)

driver.quit()