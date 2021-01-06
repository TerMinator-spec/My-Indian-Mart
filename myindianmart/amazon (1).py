from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.support.ui import Select
def get_chrome_web_driver():
    return webdriver.Chrome("chromedriver.exe")


driver=get_chrome_web_driver()
url="http://www.amazon.in/"
driver.get(url)

data=driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
link=data.get_attribute('href')
driver.get(link)

form=driver.find_element_by_id('ap_email')
form.send_keys('amansingh110000@gmail.com')
form.send_keys(Keys.ENTER)

pwd=driver.find_element_by_id('ap_password')
pwd.send_keys('########')
pwd.send_keys(Keys.ENTER)


search=driver.find_element_by_id('twotabsearchtextbox')
search.send_keys(grocery[0])
#search.send_keys(Keys.BACKSPACE)
search.clear()
search.send_keys(Keys.ENTER)


result=driver.find_elements_by_class_name('s-result-list')


try:
    results = result[0].find_elements_by_xpath(
                    "//div/span/div/div/div[2]/h2/a")
    
    links = [link.get_attribute('href') for link in results]
    
except Exception as e:
            print("Didn't get any products...")
            print(e)

def get_asin(product_link):
        return product_link[product_link.find('/dp/') + 4:product_link.find('/ref')]
    
def shorten_url(asin):
    url="http://www.amazon.in/"
    return url + 'dp/' + asin     

for link in links:
    asin=get_asin(link)
    product_short_url = shorten_url(asin)
    driver.get(product_short_url)    
    time.sleep(1)

'''//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[2]

//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[3]/div/span/div/div/div[2]/div[1]/div/div/span/a

//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[3]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a

//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[4]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a

//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[1]

amul
//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[3]/div/span/div/div/div[2]/h2/a
//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[4]/div/span/div/div/div[2]/h2/a'''

driver.get('https://www.amazon.in/Amul-Cheese-Slice-750g-Pack/dp/B01JZNUWQ4/ref=sr_1_14?almBrandId=ctnow&dchild=1&fpw=alm&keywords=amul&qid=1595853943&sr=8-14')
#driver.get('https://www.amazon.in/dp/B018E0HQPE')


press=driver.find_element_by_xpath('//*[@id="amzn-ss-text-image-link"]/span/span/strong/a')
press.send_keys(Keys.ENTER)
link2=driver.find_element_by_class_name("amzn-ss-text-image-textarea")

name=[]
elements=[]
grocery=['Parle','ITC','everest','haldiram','bikanerwala','marico','mason & co', 'kissan',
         'emami','mtr','mdh','fortune','daawat']

for i in range(len(grocery)):
    btn=Select(driver.find_element_by_xpath('//*[@id="searchDropdownBox"]'))

    text=driver.find_element_by_xpath('//*[@id="searchDropdownBox"]/option[21]').text
    btn.select_by_visible_text(text)
    search=driver.find_element_by_id('twotabsearchtextbox')
    search.clear()
    search.send_keys(grocery[i])
    search.send_keys(Keys.ENTER)
    result=driver.find_elements_by_class_name('s-result-list')
    
    try:
        results = result[0].find_elements_by_xpath(
                        "//div/span/div/div/div[2]/h2/a")
        
        links = [link.get_attribute('href') for link in results]
        
    except Exception as e:
                print("Didn't get any products...")
                print(e)
    try: 
        for k in range(len(results)):
            name.append(results[k].text)            
        for j in range(len(results)):
            
            asin=get_asin(links[j])
            product_short_url = shorten_url(asin)
            driver.get(product_short_url)  
            press=driver.find_element_by_xpath('//*[@id="amzn-ss-text-image-link"]/span/span/strong/a')
            press.send_keys(Keys.ENTER)
            link2=driver.find_element_by_class_name("amzn-ss-text-image-textarea")
            elements.append(link2.text)
            
    except StaleElementReferenceException as e:
            print('sorry')
            
    
//*[@id="amzn-ss-text-image-link"]/span/span/strong/a  
dicts={'product':name,'ids':elements}
import pandas as pd
df=pd.DataFrame(dicts)
df.to_csv('grocery.csv')

grocery=['amul','dabur','patanjali','Mother Dairy','cafe coffee day','Britannia','Parle','ITC','everest','haldiram','bikanerwala','marico','mason & co', 'kissan',
         'emami','mtr','mdh','fortune','daawat']