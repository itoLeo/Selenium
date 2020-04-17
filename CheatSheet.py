#Selenium Webdriverをインポート
from selenium import webdriver

# スリープを使うために必要
import time

# キーボード操作
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/usr/local/bin/chromedriver") #Chromeを動かすドライバを読み込み

# 単純な待機。最初に設定しておくと要素が見つかるまで指定した最大時間待機してくれる（一回の記述でよい）
driver.implicitly_wait(10)

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


# 要素の指定この後にcleck等のアクションをつけるのでこれ単体では使用しない
# classでの指定
driver.find_element_by_class_name("classname")
# idでの指定
driver.find_element_by_id("id")
# xpathでの指定　検証で要素をcopyするときにxpathをcopyで使用できる
driver.find_element_by_xpath("xpath")

# 要素のクリック
driver.find_element_by_xpath("XPATH").click()
driver.find_element_by_id('id').click()
# name属性指定
driver.find_element_by_name('name').click()

# title属性を出力
driver.find_element_by_tag_name('p').get_attribute('title')

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

#　テキストを入力してエンターキーを押したいとき
driver.find_element_by_id("ID").send_keys("strings", Keys.ENTER)

#　エンターキーを押しながらテキストを入力したいとき
driver.find_element_by_id("ID").send_keys(Keys.ENTER, "strings")

# タグに挟まれたテキストを取得したいとき
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
# disabled属性かどうか
driver.find_element_by_xpath("xpath").is_enabled()

#要素が選択されているかどうかを判定したいとき
driver.find_element_by_xpath("xpath").is_selected()

#ボタンがクリック可能になるまで待機
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

element = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.ID, "")));

# スクショを撮る
# 写真を保存するフォルダを作成しておく
import os
import sys
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/screen.png")


# get width and height of the page
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")

# set window size
driver.set_window_size(w,h)

# Get Screen Shot
driver.save_screenshot(FILENAME)