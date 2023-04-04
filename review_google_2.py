import pandas as pd
from seleniumwire import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import time

# 웹 드라이버 실행
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument("--start-maximized") # add
chrome_options.add_argument("--window-size=1920,1080") # add

driver = webdriver.Chrome('chromedriver', options=chrome_options)
# driver.maximize_window()

driver.get('https://www.google.com/maps/place/Akiba+Kart+Osaka+in+Namba/@34.661192,135.5048999,17z/data=!4m8!3m7!1s0x6000e742bdb224c1:0xd73cfed04903c699!8m2!3d34.6611876!4d135.5070939!9m1!1b1!16s%2Fg%2F11c6dm0c6m')
sleep(20)

# #리뷰더보기 클릭
# try:
#     more_btn = driver.find_elements(By.CLASS_NAME,'M77dve')
# except:
#     print("버튼을 못찾음")
# a=more_btn[3]
# a_text=a.text
# a.click()
# time.sleep(2)

#확정..!
to_scroll=driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]')

#review 총 몇개 크롤링할지
review_total=1000
result_list = []

while(True):
    driver.execute_script("arguments[0].scrollBy(0,2000)", to_scroll)
    time.sleep(4)
    breaks = driver.find_elements(By.CLASS_NAME, 'wiI7pd')

    #긴 리뷰의 더보기 클릭
    to_pushs=driver.find_elements(By.CLASS_NAME,'w8nwRe.kyuRq')
    for push in to_pushs:
        push.click()
        time.sleep(0.5)

    print(len(breaks))
    if (len(breaks)>=review_total):
        break
#리뷰 담기
to_adds=driver.find_elements(By.CLASS_NAME,'wiI7pd')
for add in to_adds:
    result_list.append(add.text)
# csv로 저장
df = pd.DataFrame(result_list)
df.to_csv("오사카 성 공원.csv",index=False)
print("end")
driver.quit()