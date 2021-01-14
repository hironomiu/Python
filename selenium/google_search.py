import time
from selenium import webdriver

url = 'https://www.google.com/'
driver = webdriver.Chrome()
driver.get(url)

time.sleep(2)

# Topページで検索ボックスを特定しキーワード検索
search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()

time.sleep(2)

# 検索結果ページに遷移後xpathで検索ボックスを特定し再度検索
search_box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input')
search_box.clear()
search_box.send_keys('hironomiu github')
search_box.submit()

# 検索結果１件目を特定しリンクをクリック
search_boxes = driver.find_elements_by_class_name('g')
search_boxes[0].find_elements_by_tag_name('a')[0].click()

driver.quit()