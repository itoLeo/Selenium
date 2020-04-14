from selenium import webdriver #Selenium Webdriverをインポートして

driver = webdriver.Chrome("/usr/local/bin/chromedriver") #Chromeを動かすドライバを読み込み

driver.get("https://google.co.jp") #googleを開く！


