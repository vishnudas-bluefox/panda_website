
# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# Establish chrome driver and go to report site URL
url = "https://twitter.com/engineers_feed/status/1592207414367252480/photo/1"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
source = driver.page_source
data = driver.find_elements_by_class_name('r-1p0dtai r-1pi2tsx r-1d2f490 r-u8s1d r-ipm5af r-13qz1uu')

for i in data:
    print(i)
#all_links = driver.find_element(By.XPATH('//img[contains(@src="pbs.twimg.com")]'));
#print(all_links)
#data = source.find_elements(By.TAG_NAME,"img")
#print(data)
