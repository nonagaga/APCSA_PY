# Imports Packages
import time
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Opens up web driver and goes to Google Images
driver = webdriver.Safari()
driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')
driver.maximize_window()

box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')

box.send_keys("Mexican Flag")
box.send_keys(Keys.ENTER)

# Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

urlList = []
for i in range(1, 20):
    try:

        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img').click()
        print("Clicking image #" + str(i))

        src = driver.find_element_by_xpath('//*[@class="v4dQwb"]/a/img').get_attribute("src")
        print("Getting the source of image #" + str(i))

        urlList.append(src)
        print("Url is backed up to a list!")



        # driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img').screenshot('Images/flag(' + str(i) + ').png')

    except:
        pass
for url in urlList:
    try:
        urllib.request.urlretrieve(url, 'Images/flag(' + str(i) + ').jpg''')
        print("Successfully downloaded image #" + str(i))
        continue
    except:
        print("Image link is encrypted, falling back on screenshots!")
        try:
            driver.get(url)
            driver.find_element_by_xpath('/html/body/img').screenshot('Images/flag(' + str(urlList.index(url)) + ').png')
        except:
            print("Image link is bad! Skipping!")
        continue

driver.close()
print("Completed: ")
print("Url list is: " + str(urlList))
