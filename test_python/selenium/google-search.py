from selenium import webdriver
import time
import pandas as pd

#食べログのURL
TABELOG_URL = 'https://tabelog.com/'

#変数
AREA_NAME = '東京'
KEY_WORD = 'ケバブ'
DATE = '2020/5/20(水)'
NUM_OF_PPL = '2'
TIME = '19:00'

#webdriverの指定
driver = webdriver.Chrome(r'C:\Users\nakamura.yo\chromedriver_win32\chromedriver.exe')




#driver.get('https://www.google.com/')
driver.get(TABELOG_URL)
time.sleep(1)

#フィールドに値をセット
driver.find_element_by_id("sa").send_keys(AREA_NAME)
driver.find_element_by_id("sk").send_keys(KEY_WORD)

#検索実行
#driver.find_element_by_class_name('gb_g').click()
driver.find_element_by_id("js-global-search-btn").click()

#店舗情報のデータフレームを用意
df =pd.DataFrame(columns=['name', 'star_val', 'dinner_price', 'lunch_price', 'url'])

#店舗数とページ数を取得
shop_num = int(driver.find_elements_by_class_name("c-page-count__num")[2].text)
page_num = int(shop_num / 20)
if page_num == 0:
    page_num = 1

"""
# 店の情報を取得
shop_num = 1
for page in range(page_num):
    restaurants = driver.find_elements_by_class_name("list-rst")
    for restraunt in restaurants:
        shop_name = restraunt.find_element_by_class_name("cpy-rst-name").text
        shop_url = restraunt.find_element_by_class_name("cpy-rst-name").get_attribute("href")
        is_ranked = restraunt.find_elements_by_class_name("list-rst__rating-val")
        dinner_price = restraunt.find_element_by_class_name("cpy-dinner-budget-val").text
        lunch_price = restraunt.find_element_by_class_name("cpy-lunch-budget-val").text
        shop_star_val = is_ranked[0].text if is_ranked != [] else np.nan
        df.loc[shop_num] = [shop_name,shop_star_val,dinner_price,lunch_price,shop_url]
        shop_num += 1

    if page_num != 1:
        driver.find_elements_by_class_name("c-pagination__arrow--next")[0].location_once_scrolled_into_view
        sleep(1)
        driver.find_elements_by_class_name("c-pagination__arrow--next")[0].click()

# 星の数をもとにソートする
shops = df.sort_values('star_val',ascending=False)



# csvファイルに書き出す
#shops.to_csv("restaurant.csv")
print(shops)

"""
print(page_num)

# ブラウザを終了する。
driver.close()