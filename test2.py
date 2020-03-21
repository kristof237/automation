import time
from selenium import webdriver

link='http://youtube.com'

driver=webdriver.Firefox()
driver.get(link)

driver.find_element_by_name('search_query').send_keys('wygral jebany')
driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/button/yt-icon').click()
driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a/yt-formatted-string').click()

time.sleep(5)
driver.quit()

