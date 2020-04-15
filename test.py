import time                            # スリープを使うために必要
from selenium import webdriver #Selenium Webdriverをインポートして

driver = webdriver.Chrome("/usr/local/bin/chromedriver") #Chromeを動かすドライバを読み込み

#ブラウザ起動、ページ遷移
driver.get("URL")

#ブラウザバック
driver.back()

#すすむ
driver.forward()

#更新
driver.refresh()

#現在のurlを知りたいとき
driver.current_url

#タイトルを知りたいとき
driver.title

#ページのソースを知りたいとき
driver.page_source

#ウィンドウを閉じるとき
driver.close()

#全てのウィンドウを閉じるとき
driver.quit()

# 要素の指定
# classでの指定
driver.find_element_by_class_name("classname")
# idでの指定
driver.find_element_by_id("id")
# xpathでの指定
driver.find_element_by_xpath("xpath")

# 要素のクリック
driver.find_element_by_xpath("XPATH").click()

# ある要素までスクロールしたいとき
from selenium.webdriver.common.action_chains import ActionChains

element = driver.find_element_by_id("ID")
actions = ActionChains(driver)
actions.move_to_element(element)
actions.perform()

# ドロップダウンを選択したいとき（select supportをimportする必要あり）
element = driver.find_element_by_xpath("xpath")
Select(element).select_by_index(indexnum) # indexで選択
Select(element).select_by_value("value") # valueの値
Select(element).select_by_visible_text("text") # 表示テキスト

# テキストを入力したいとき
driver.find_element_by_id("ID").send_keys("strings")

# テキストを取得したいとき
driver.find_element_by_id("ID").text

# 属性を取得したいとき
driver.find_element_by_id("ID").get_attribute("value")

# アラートをハンドリングしたいとき
Alert(driver).accept()

# ウィンドウサイズを最大にしたいとき
driver.maximize_window()

# 要素が表示されているかを判定したいとき
driver.find_element_by_xpath("xpath").is_displayed()

#要素が有効化どうかを判定したいとき
driver.find_element_by_xpath("xpath").is_enabled()

#要素が選択されているかどうかを判定したいとき
driver.find_element_by_xpath("xpath").is_selected()


