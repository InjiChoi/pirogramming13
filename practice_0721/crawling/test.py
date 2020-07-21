from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')

# 2. 파파고 사이트에 접속 (자동번역 해제)
driver.get('https://papago.naver.com/')
time.sleep(2)
auto_complete_btn = driver.find_element_by_css_selector('#root > div > div.wrap___1rX6i.rwd.rwd___3Qe-c.banner_active___3MQbf > section > div > div:nth-child(1) > div:nth-child(2) > div > div.autocomplete_area___2alwE.active___3VPGL > label')
auto_complete_btn.click()

time.sleep(1)

driver.implicitly_wait(5)
input_box = driver.find_element_by_css_selector('textarea#txtSource')
input_box.send_keys('안녕하세요. 피로그래밍입니다.')
time.sleep(2)
translation_btn = driver.find_element_by_css_selector('button#btnTranslate')
translation_btn.click()

time.sleep(2)
# 5. 번역된 결과 출력
output_area = driver.find_element_by_css_selector('div#txtTarget').text
print(output_area)

time.sleep(10)
driver.close()