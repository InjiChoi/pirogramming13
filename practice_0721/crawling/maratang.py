from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')
driver.get('https://map.kakao.com/')
time.sleep(2)

#이상한 것 없애기
driver.find_element_by_css_selector('div.view_coach').click()

#강남 마라탕 입력
input_box = driver.find_element_by_css_selector('#search\.keyword\.query')
input_box.send_keys('강남 마라탕')
input_box.send_keys(Keys.ENTER)
#검색 버튼 클릭
# search_btn = driver.find_element_by_css_selector('#search\.keyword\.submit')
# search_btn.click()
time.sleep(2)

#15개의 가게 선택
stores = driver.find_elements_by_css_selector('.PlaceItem')
#가게 하나씩 추출
for store in stores:
    name = store.find_element_by_css_selector('a.link_name').text
    try:
        phone = store.find_element_by_css_selector('span.phone').text
    except:
        phone = '번호 없음'
    try:
        addr = store.find_element_by_css_selector('p').text
    except:
        addr = '주소 없음'

    print(name, phone, addr)

more_btn = driver.find_element_by_css_selector('#info\.search\.place\.more')
more_btn.send_keys(Keys.ENTER)

time.sleep(2)

for p in range(2, 11):
    time.sleep(2)

    stores = driver.find_elements_by_css_selector('li.PlaceItem')
    time.sleep(2)

    for store in stores:
        name = store.find_element_by_css_selector('a.link_name').text
        try:
            phone = store.find_element_by_css_selector('span.phone').text
        except:
            phone = '번호 없음'
        try:
            addr = store.find_element_by_css_selector('p').text
        except:
            addr = '주소 없음'

        print(name, phone, addr)

    # '이전' 버튼, 1, 2, 3, 4, 5, '다음' 버튼을 모두 포함한 것들 한꺼번에 추출
    page_bar = driver.find_elements_by_css_selector('div#info\.search\.page div.pageWrap > *')
    time.sleep(2)
    # 5로 나눈 나머지가 0이 아닐 때만 1, 2, 3, 4, 5에 해당하는 index에 맞게 페이지 이동
    if p % 5 != 0:
        page_bar[p % 5 + 1].click()

    # 5로 나눈 나머지가 0일 때는 현재 페이지가 5, 10, ... 페이지라는 뜻이므로 '다음' 버튼 클릭
    else:
        page_bar[6].click()


time.sleep(5)
driver.close()