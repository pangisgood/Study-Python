from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
driver = webdriver.Chrome()


driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
elem = driver.find_element_by_name("q")

elem.send_keys("한동대 김준혁")  #검색할 키워드
elem.send_keys(Keys.RETURN)
SCROLL_PAUSE_TIME = 1



foldername="한동대김준혁"



# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try: 
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images= driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

count=1
for image in images:
    try:
        image.click()
        time.sleep(2) 
        img_url = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
        # urllib.request.urlretrieve(img_url, str(count)+".jpg")
        urllib.request.urlretrieve(img_url, foldername +"/"+ str(count)+".jpg")
        count=count+1
    except:
        pass
driver.close()


#이미지 주소 다운 방법 search
#python download image url로 검색했음

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
